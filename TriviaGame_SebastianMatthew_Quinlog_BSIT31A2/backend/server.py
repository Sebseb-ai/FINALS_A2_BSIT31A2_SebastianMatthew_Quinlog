from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal
import uuid
from datetime import datetime, timezone
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# SQLAlchemy SQLite In-Memory Setup
SQLITE_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Models (for in-memory game sessions)
class GameSessionDB(Base):
    __tablename__ = "game_sessions"
    
    session_id = Column(String, primary_key=True, index=True)
    player_name = Column(String, nullable=False)
    current_question_index = Column(Integer, default=0)
    score = Column(Integer, default=0)
    total_questions = Column(Integer, default=10)
    category = Column(String, nullable=True)
    difficulty = Column(String, nullable=True)
    start_time = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

class QuestionAttemptDB(Base):
    __tablename__ = "question_attempts"
    
    id = Column(String, primary_key=True, index=True)
    session_id = Column(String, nullable=False)
    question_id = Column(String, nullable=False)
    user_answer = Column(String, nullable=True)
    is_correct = Column(Boolean, nullable=False)
    time_taken = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create tables in memory
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
@contextmanager
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# Pydantic Models
class Question(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question_text: str
    question_type: Literal["multiple_choice", "true_false", "text_input"]
    options: Optional[List[str]] = None
    correct_answer: str
    category: str
    difficulty: Literal["easy", "medium", "hard"]
    time_limit: int = 30  # seconds
    points: int = 10

class QuestionCreate(BaseModel):
    question_text: str
    question_type: Literal["multiple_choice", "true_false", "text_input"]
    options: Optional[List[str]] = None
    correct_answer: str
    category: str
    difficulty: Literal["easy", "medium", "hard"]
    time_limit: int = 30
    points: int = 10

class QuestionResponse(BaseModel):
    id: str
    question_text: str
    question_type: str
    options: Optional[List[str]] = None
    category: str
    difficulty: str
    time_limit: int
    points: int

class GameSessionCreate(BaseModel):
    player_name: str
    category: Optional[str] = None
    difficulty: Optional[str] = None
    total_questions: int = 10

class GameSession(BaseModel):
    session_id: str
    player_name: str
    current_question_index: int
    score: int
    total_questions: int
    category: Optional[str] = None
    difficulty: Optional[str] = None
    is_active: bool

class AnswerSubmission(BaseModel):
    session_id: str
    question_id: str
    user_answer: str
    time_taken: float

class AnswerResult(BaseModel):
    is_correct: bool
    correct_answer: str
    points_earned: int
    current_score: int
    is_game_over: bool

class LeaderboardEntry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    player_name: str
    score: int
    total_questions: int
    category: Optional[str] = None
    difficulty: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class LeaderboardEntryCreate(BaseModel):
    player_name: str
    score: int
    total_questions: int
    category: Optional[str] = None
    difficulty: Optional[str] = None

# Create the main app
app = FastAPI()
api_router = APIRouter(prefix="/api")

# ==================== Data Access Layer ====================

class QuestionRepository:
    """Repository for Question data (MongoDB)"""
    
    @staticmethod
    async def create_question(question: QuestionCreate) -> Question:
        question_obj = Question(**question.model_dump())
        doc = question_obj.model_dump()
        doc['timestamp'] = datetime.now(timezone.utc).isoformat()
        await db.questions.insert_one(doc)
        return question_obj
    
    @staticmethod
    async def get_questions(category: Optional[str] = None, difficulty: Optional[str] = None, limit: int = 10) -> List[Question]:
        query = {}
        if category:
            query['category'] = category
        if difficulty:
            query['difficulty'] = difficulty
        
        questions = await db.questions.find(query, {"_id": 0}).to_list(limit)
        return [Question(**q) for q in questions]
    
    @staticmethod
    async def get_question_by_id(question_id: str) -> Optional[Question]:
        question = await db.questions.find_one({"id": question_id}, {"_id": 0})
        if question:
            return Question(**question)
        return None

class LeaderboardRepository:
    """Repository for Leaderboard data (MongoDB)"""
    
    @staticmethod
    async def add_entry(entry: LeaderboardEntryCreate) -> LeaderboardEntry:
        entry_obj = LeaderboardEntry(**entry.model_dump())
        doc = entry_obj.model_dump()
        doc['timestamp'] = doc['timestamp'].isoformat()
        await db.leaderboard.insert_one(doc)
        return entry_obj
    
    @staticmethod
    async def get_top_scores(limit: int = 10) -> List[LeaderboardEntry]:
        entries = await db.leaderboard.find({}, {"_id": 0}).sort("score", -1).limit(limit).to_list(limit)
        for entry in entries:
            if isinstance(entry['timestamp'], str):
                entry['timestamp'] = datetime.fromisoformat(entry['timestamp'])
        return [LeaderboardEntry(**e) for e in entries]

class GameSessionRepository:
    """Repository for Game Session data (SQLite in-memory)"""
    
    @staticmethod
    def create_session(session_data: GameSessionCreate) -> GameSession:
        with get_db() as db_session:
            session_id = str(uuid.uuid4())
            db_session_obj = GameSessionDB(
                session_id=session_id,
                player_name=session_data.player_name,
                total_questions=session_data.total_questions,
                category=session_data.category,
                difficulty=session_data.difficulty
            )
            db_session.add(db_session_obj)
            db_session.commit()
            db_session.refresh(db_session_obj)
            
            return GameSession(
                session_id=db_session_obj.session_id,
                player_name=db_session_obj.player_name,
                current_question_index=db_session_obj.current_question_index,
                score=db_session_obj.score,
                total_questions=db_session_obj.total_questions,
                category=db_session_obj.category,
                difficulty=db_session_obj.difficulty,
                is_active=db_session_obj.is_active
            )
    
    @staticmethod
    def get_session(session_id: str) -> Optional[GameSession]:
        with get_db() as db_session:
            session = db_session.query(GameSessionDB).filter(GameSessionDB.session_id == session_id).first()
            if session:
                return GameSession(
                    session_id=session.session_id,
                    player_name=session.player_name,
                    current_question_index=session.current_question_index,
                    score=session.score,
                    total_questions=session.total_questions,
                    category=session.category,
                    difficulty=session.difficulty,
                    is_active=session.is_active
                )
            return None
    
    @staticmethod
    def update_session(session_id: str, score: int, current_question_index: int, is_active: bool) -> None:
        with get_db() as db_session:
            session = db_session.query(GameSessionDB).filter(GameSessionDB.session_id == session_id).first()
            if session:
                session.score = score
                session.current_question_index = current_question_index
                session.is_active = is_active
                db_session.commit()
    
    @staticmethod
    def add_question_attempt(session_id: str, question_id: str, user_answer: str, is_correct: bool, time_taken: float) -> None:
        with get_db() as db_session:
            attempt = QuestionAttemptDB(
                id=str(uuid.uuid4()),
                session_id=session_id,
                question_id=question_id,
                user_answer=user_answer,
                is_correct=is_correct,
                time_taken=time_taken
            )
            db_session.add(attempt)
            db_session.commit()

# ==================== Business Logic Layer ====================

class GameService:
    """Business logic for game operations"""
    
    @staticmethod
    async def start_game(session_data: GameSessionCreate) -> GameSession:
        return GameSessionRepository.create_session(session_data)
    
    @staticmethod
    async def get_next_question(session_id: str) -> QuestionResponse:
        session = GameSessionRepository.get_session(session_id)
        if not session or not session.is_active:
            raise HTTPException(status_code=404, detail="Game session not found or inactive")
        
        if session.current_question_index >= session.total_questions:
            raise HTTPException(status_code=400, detail="Game is already completed")
        
        questions = await QuestionRepository.get_questions(
            category=session.category,
            difficulty=session.difficulty,
            limit=session.total_questions
        )
        
        if session.current_question_index >= len(questions):
            raise HTTPException(status_code=404, detail="No more questions available")
        
        question = questions[session.current_question_index]
        return QuestionResponse(
            id=question.id,
            question_text=question.question_text,
            question_type=question.question_type,
            options=question.options,
            category=question.category,
            difficulty=question.difficulty,
            time_limit=question.time_limit,
            points=question.points
        )
    
    @staticmethod
    async def submit_answer(answer: AnswerSubmission) -> AnswerResult:
        session = GameSessionRepository.get_session(answer.session_id)
        if not session or not session.is_active:
            raise HTTPException(status_code=404, detail="Game session not found or inactive")
        
        question = await QuestionRepository.get_question_by_id(answer.question_id)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Check answer
        is_correct = answer.user_answer.strip().lower() == question.correct_answer.strip().lower()
        points_earned = question.points if is_correct else 0
        new_score = session.score + points_earned
        new_index = session.current_question_index + 1
        is_game_over = new_index >= session.total_questions
        
        # Update session
        GameSessionRepository.update_session(
            answer.session_id,
            new_score,
            new_index,
            not is_game_over
        )
        
        # Record attempt
        GameSessionRepository.add_question_attempt(
            answer.session_id,
            answer.question_id,
            answer.user_answer,
            is_correct,
            answer.time_taken
        )
        
        # If game over, save to leaderboard
        if is_game_over:
            await LeaderboardRepository.add_entry(
                LeaderboardEntryCreate(
                    player_name=session.player_name,
                    score=new_score,
                    total_questions=session.total_questions,
                    category=session.category,
                    difficulty=session.difficulty
                )
            )
        
        return AnswerResult(
            is_correct=is_correct,
            correct_answer=question.correct_answer,
            points_earned=points_earned,
            current_score=new_score,
            is_game_over=is_game_over
        )

# ==================== Presentation Layer (API Routes) ====================

@api_router.get("/")
async def root():
    return {"message": "Trivia Game API with Layered Architecture"}

@api_router.post("/questions", response_model=Question)
async def create_question(question: QuestionCreate):
    return await QuestionRepository.create_question(question)

@api_router.get("/questions", response_model=List[Question])
async def get_questions(category: Optional[str] = None, difficulty: Optional[str] = None, limit: int = 100):
    return await QuestionRepository.get_questions(category, difficulty, limit)

@api_router.post("/game/start", response_model=GameSession)
async def start_game(session_data: GameSessionCreate):
    return await GameService.start_game(session_data)

@api_router.get("/game/{session_id}/question", response_model=QuestionResponse)
async def get_next_question(session_id: str):
    return await GameService.get_next_question(session_id)

@api_router.post("/game/answer", response_model=AnswerResult)
async def submit_answer(answer: AnswerSubmission):
    return await GameService.submit_answer(answer)

@api_router.get("/game/{session_id}", response_model=GameSession)
async def get_game_session(session_id: str):
    session = GameSessionRepository.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Game session not found")
    return session

@api_router.get("/leaderboard", response_model=List[LeaderboardEntry])
async def get_leaderboard(limit: int = 10):
    return await LeaderboardRepository.get_top_scores(limit)

@api_router.get("/categories")
async def get_categories():
    return {
        "categories": ["Science", "History", "Geography", "Sports", "Entertainment", "Literature", "Technology", "Art"]
    }

# Seed initial questions
@app.on_event("startup")
async def seed_questions():
    from seed_data import get_all_questions
    
    existing = await db.questions.count_documents({})
    if existing == 0:
        initial_questions = get_all_questions()
        
        for q in initial_questions:
            q['id'] = str(uuid.uuid4())
            q['timestamp'] = datetime.now(timezone.utc).isoformat()
        
        await db.questions.insert_many(initial_questions)
        logger.info(f"Seeded {len(initial_questions)} questions")

# Include router
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()