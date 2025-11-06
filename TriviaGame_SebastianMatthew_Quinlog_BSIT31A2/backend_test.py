import requests
import sys
import json
from datetime import datetime

class TriviaAPITester:
    def __init__(self, base_url="https://trivia-dual-db.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.session_id = None
        self.current_question = None

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    return True, response.json()
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    print(f"   Response: {response.json()}")
                except:
                    print(f"   Response: {response.text}")

            return success, response.json() if success else {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root Endpoint", "GET", "", 200)

    def test_get_categories(self):
        """Test categories endpoint"""
        success, response = self.run_test("Get Categories", "GET", "categories", 200)
        if success and 'categories' in response:
            print(f"   Categories: {response['categories']}")
        return success, response

    def test_get_questions(self):
        """Test questions endpoint"""
        success, response = self.run_test("Get Questions", "GET", "questions", 200)
        if success:
            print(f"   Found {len(response)} questions")
        return success, response

    def test_get_questions_filtered(self):
        """Test questions with filters"""
        success, response = self.run_test(
            "Get Questions (Science, Easy)", 
            "GET", 
            "questions", 
            200, 
            params={"category": "Science", "difficulty": "easy", "limit": 5}
        )
        if success:
            print(f"   Found {len(response)} filtered questions")
        return success, response

    def test_start_game(self):
        """Test starting a new game"""
        game_data = {
            "player_name": f"TestPlayer_{datetime.now().strftime('%H%M%S')}",
            "category": "Science",
            "difficulty": "easy",
            "total_questions": 5
        }
        
        success, response = self.run_test(
            "Start Game", 
            "POST", 
            "game/start", 
            200, 
            data=game_data
        )
        
        if success and 'session_id' in response:
            self.session_id = response['session_id']
            print(f"   Session ID: {self.session_id}")
        
        return success, response

    def test_get_game_session(self):
        """Test getting game session info"""
        if not self.session_id:
            print("❌ No session ID available")
            return False, {}
        
        return self.run_test(
            "Get Game Session", 
            "GET", 
            f"game/{self.session_id}", 
            200
        )

    def test_get_next_question(self):
        """Test getting next question"""
        if not self.session_id:
            print("❌ No session ID available")
            return False, {}
        
        success, response = self.run_test(
            "Get Next Question", 
            "GET", 
            f"game/{self.session_id}/question", 
            200
        )
        
        if success:
            self.current_question = response
            print(f"   Question: {response.get('question_text', 'N/A')}")
            print(f"   Type: {response.get('question_type', 'N/A')}")
        
        return success, response

    def test_submit_answer(self):
        """Test submitting an answer"""
        if not self.session_id or not self.current_question:
            print("❌ No session ID or current question available")
            return False, {}
        
        # Use correct answer for testing
        answer_data = {
            "session_id": self.session_id,
            "question_id": self.current_question['id'],
            "user_answer": self.current_question.get('correct_answer', 'Test Answer'),
            "time_taken": 15.5
        }
        
        success, response = self.run_test(
            "Submit Answer", 
            "POST", 
            "game/answer", 
            200, 
            data=answer_data
        )
        
        if success:
            print(f"   Correct: {response.get('is_correct', False)}")
            print(f"   Points: {response.get('points_earned', 0)}")
            print(f"   Score: {response.get('current_score', 0)}")
        
        return success, response

    def test_leaderboard(self):
        """Test leaderboard endpoint"""
        success, response = self.run_test("Get Leaderboard", "GET", "leaderboard", 200)
        if success:
            print(f"   Leaderboard entries: {len(response)}")
        return success, response

    def run_full_game_flow(self):
        """Test complete game flow"""
        print("\n🎮 Testing Complete Game Flow...")
        
        # Start game
        success, _ = self.test_start_game()
        if not success:
            return False
        
        # Play through questions
        for i in range(3):  # Test first 3 questions
            print(f"\n--- Question {i+1} ---")
            
            # Get question
            success, _ = self.test_get_next_question()
            if not success:
                break
            
            # Submit answer
            success, result = self.test_submit_answer()
            if not success:
                break
            
            if result.get('is_game_over'):
                print("   Game completed!")
                break
        
        return True

def main():
    print("🚀 Starting Trivia Game API Tests...")
    tester = TriviaAPITester()
    
    # Basic API tests
    print("\n" + "="*50)
    print("BASIC API TESTS")
    print("="*50)
    
    tester.test_root_endpoint()
    tester.test_get_categories()
    tester.test_get_questions()
    tester.test_get_questions_filtered()
    
    # Game flow tests
    print("\n" + "="*50)
    print("GAME FLOW TESTS")
    print("="*50)
    
    tester.run_full_game_flow()
    
    # Leaderboard test
    print("\n" + "="*50)
    print("LEADERBOARD TESTS")
    print("="*50)
    
    tester.test_leaderboard()
    
    # Print results
    print("\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    print(f"📊 Tests passed: {tester.tests_passed}/{tester.tests_run}")
    
    success_rate = (tester.tests_passed / tester.tests_run) * 100 if tester.tests_run > 0 else 0
    print(f"📈 Success rate: {success_rate:.1f}%")
    
    if success_rate >= 80:
        print("🎉 Backend API tests mostly successful!")
        return 0
    else:
        print("⚠️  Backend API has significant issues")
        return 1

if __name__ == "__main__":
    sys.exit(main())