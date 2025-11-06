"""
Comprehensive question database for trivia game
Ensures sufficient questions for all category/difficulty combinations
"""

def get_all_questions():
    return [
        # ==================== SCIENCE ====================
        # Science - Easy
        {"question_text": "What planet is known as the Red Planet?", "question_type": "multiple_choice", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "correct_answer": "Mars", "category": "Science", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "Water freezes at 0 degrees Celsius.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "The Sun is a star.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "How many legs does a spider have?", "question_type": "multiple_choice", "options": ["8", "6", "10", "4"], "correct_answer": "8", "category": "Science", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "What gas do plants absorb from the atmosphere?", "question_type": "multiple_choice", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correct_answer": "Carbon Dioxide", "category": "Science", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "Humans have five senses.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What is the largest organ in the human body?", "question_type": "multiple_choice", "options": ["Skin", "Heart", "Liver", "Brain"], "correct_answer": "Skin", "category": "Science", "difficulty": "easy", "time_limit": 30, "points": 10},
        
        # Science - Medium
        {"question_text": "What is the chemical symbol for gold?", "question_type": "text_input", "options": None, "correct_answer": "Au", "category": "Science", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What is the speed of light in vacuum?", "question_type": "multiple_choice", "options": ["299,792 km/s", "150,000 km/s", "400,000 km/s", "250,000 km/s"], "correct_answer": "299,792 km/s", "category": "Science", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "DNA stands for Deoxyribonucleic Acid.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "What is the atomic number of carbon?", "question_type": "text_input", "options": None, "correct_answer": "6", "category": "Science", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What is the powerhouse of the cell?", "question_type": "text_input", "options": None, "correct_answer": "Mitochondria", "category": "Science", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What planet has the most moons?", "question_type": "multiple_choice", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "correct_answer": "Saturn", "category": "Science", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The human body has 206 bones.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "medium", "time_limit": 25, "points": 15},
        
        # Science - Hard
        {"question_text": "What is the Heisenberg Uncertainty Principle?", "question_type": "multiple_choice", "options": ["Position and momentum cannot be precisely known simultaneously", "Energy is quantized", "Light behaves as both wave and particle", "Matter cannot be created or destroyed"], "correct_answer": "Position and momentum cannot be precisely known simultaneously", "category": "Science", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "What is the half-life of Carbon-14?", "question_type": "text_input", "options": None, "correct_answer": "5730", "category": "Science", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The human brain uses approximately 20% of the body's energy.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Science", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "What is the name of the largest known star?", "question_type": "text_input", "options": None, "correct_answer": "UY Scuti", "category": "Science", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Photosynthesis occurs in which cell organelle?", "question_type": "text_input", "options": None, "correct_answer": "Chloroplast", "category": "Science", "difficulty": "hard", "time_limit": 35, "points": 20},
        
        # ==================== HISTORY ====================
        # History - Easy
        {"question_text": "Who was the first President of the United States?", "question_type": "multiple_choice", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "correct_answer": "George Washington", "category": "History", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "The Great Wall of China was built to protect against invasions.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "The Titanic sank in 1912.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Who was the first person to walk on the moon?", "question_type": "multiple_choice", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "correct_answer": "Neil Armstrong", "category": "History", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "Which country gifted the Statue of Liberty to the USA?", "question_type": "multiple_choice", "options": ["France", "England", "Spain", "Italy"], "correct_answer": "France", "category": "History", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "The Cold War was fought between the USA and USSR.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Christopher Columbus discovered America in 1492.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "easy", "time_limit": 20, "points": 10},
        
        # History - Medium
        {"question_text": "In what year did World War II end?", "question_type": "text_input", "options": None, "correct_answer": "1945", "category": "History", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "Who wrote the Declaration of Independence?", "question_type": "text_input", "options": None, "correct_answer": "Thomas Jefferson", "category": "History", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The Roman Empire fell in 476 AD.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Which empire built Machu Picchu?", "question_type": "multiple_choice", "options": ["Inca", "Aztec", "Maya", "Olmec"], "correct_answer": "Inca", "category": "History", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What year did the Berlin Wall fall?", "question_type": "text_input", "options": None, "correct_answer": "1989", "category": "History", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The French Revolution began in 1789.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who was the British Prime Minister during most of WWII?", "question_type": "text_input", "options": None, "correct_answer": "Winston Churchill", "category": "History", "difficulty": "medium", "time_limit": 35, "points": 15},
        
        # History - Hard
        {"question_text": "What year was the Magna Carta signed?", "question_type": "text_input", "options": None, "correct_answer": "1215", "category": "History", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The Thirty Years' War lasted exactly 30 years.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "Who was the last Tsar of Russia?", "question_type": "text_input", "options": None, "correct_answer": "Nicholas II", "category": "History", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "What battle is considered the turning point of the American Civil War?", "question_type": "text_input", "options": None, "correct_answer": "Gettysburg", "category": "History", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The Byzantine Empire fell in 1453.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "History", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== GEOGRAPHY ====================
        # Geography - Easy
        {"question_text": "What is the capital of France?", "question_type": "multiple_choice", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_answer": "Paris", "category": "Geography", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Australia is both a country and a continent.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What is the largest country by area?", "question_type": "multiple_choice", "options": ["Russia", "Canada", "China", "USA"], "correct_answer": "Russia", "category": "Geography", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Mount Everest is the tallest mountain in the world.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What ocean is between Africa and Australia?", "question_type": "multiple_choice", "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"], "correct_answer": "Indian Ocean", "category": "Geography", "difficulty": "easy", "time_limit": 30, "points": 10},
        {"question_text": "The Amazon River is in South America.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "How many continents are there?", "question_type": "multiple_choice", "options": ["7", "5", "6", "8"], "correct_answer": "7", "category": "Geography", "difficulty": "easy", "time_limit": 25, "points": 10},
        
        # Geography - Medium
        {"question_text": "What is the longest river in the world?", "question_type": "text_input", "options": None, "correct_answer": "Nile", "category": "Geography", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What is the capital of Canada?", "question_type": "text_input", "options": None, "correct_answer": "Ottawa", "category": "Geography", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "The Dead Sea is the lowest point on Earth's surface.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Which desert is the largest hot desert in the world?", "question_type": "multiple_choice", "options": ["Sahara", "Arabian", "Gobi", "Kalahari"], "correct_answer": "Sahara", "category": "Geography", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What is the smallest country in the world?", "question_type": "text_input", "options": None, "correct_answer": "Vatican City", "category": "Geography", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The Great Barrier Reef is located in Australia.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "In which country would you find the ancient city of Petra?", "question_type": "text_input", "options": None, "correct_answer": "Jordan", "category": "Geography", "difficulty": "medium", "time_limit": 35, "points": 15},
        
        # Geography - Hard
        {"question_text": "What is the capital of Bhutan?", "question_type": "text_input", "options": None, "correct_answer": "Thimphu", "category": "Geography", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Lake Baikal is the deepest lake in the world.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "What is the second longest river in the world?", "question_type": "text_input", "options": None, "correct_answer": "Amazon", "category": "Geography", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Which strait separates Europe from Africa?", "question_type": "text_input", "options": None, "correct_answer": "Gibraltar", "category": "Geography", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The Tropic of Capricorn is south of the equator.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Geography", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== SPORTS ====================
        # Sports - Easy
        {"question_text": "How many players are on a soccer team on the field?", "question_type": "multiple_choice", "options": ["11", "9", "10", "12"], "correct_answer": "11", "category": "Sports", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "The Olympics are held every four years.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "A marathon is 26.2 miles long.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What sport is known as 'the beautiful game'?", "question_type": "multiple_choice", "options": ["Soccer", "Basketball", "Tennis", "Cricket"], "correct_answer": "Soccer", "category": "Sports", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "How many points is a touchdown worth in American football?", "question_type": "multiple_choice", "options": ["6", "7", "5", "8"], "correct_answer": "6", "category": "Sports", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Tennis was originally called lawn tennis.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "In which sport would you perform a slam dunk?", "question_type": "text_input", "options": None, "correct_answer": "Basketball", "category": "Sports", "difficulty": "easy", "time_limit": 25, "points": 10},
        
        # Sports - Medium
        {"question_text": "Who holds the record for most Olympic gold medals?", "question_type": "text_input", "options": None, "correct_answer": "Michael Phelps", "category": "Sports", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "What is the diameter of a basketball hoop in inches?", "question_type": "text_input", "options": None, "correct_answer": "18", "category": "Sports", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The Tour de France is a cycling race.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "In tennis, what does 'love' mean?", "question_type": "multiple_choice", "options": ["Zero", "Tie", "First serve", "Match point"], "correct_answer": "Zero", "category": "Sports", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "How many innings are in a standard baseball game?", "question_type": "text_input", "options": None, "correct_answer": "9", "category": "Sports", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "A hockey puck is made of rubber.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "What country won the first FIFA World Cup?", "question_type": "text_input", "options": None, "correct_answer": "Uruguay", "category": "Sports", "difficulty": "medium", "time_limit": 35, "points": 15},
        
        # Sports - Hard
        {"question_text": "What year were the first modern Olympics held?", "question_type": "text_input", "options": None, "correct_answer": "1896", "category": "Sports", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The fastest recorded tennis serve exceeded 160 mph.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "Who was the first athlete to run a sub-4-minute mile?", "question_type": "text_input", "options": None, "correct_answer": "Roger Bannister", "category": "Sports", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "What is the maximum break in snooker?", "question_type": "text_input", "options": None, "correct_answer": "147", "category": "Sports", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Formula 1 cars can reach speeds over 230 mph.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Sports", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== ENTERTAINMENT ====================
        # Entertainment - Easy
        {"question_text": "Who played Iron Man in the Marvel Cinematic Universe?", "question_type": "multiple_choice", "options": ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"], "correct_answer": "Robert Downey Jr.", "category": "Entertainment", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "The movie 'Frozen' features the song 'Let It Go'.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What is the name of Harry Potter's owl?", "question_type": "multiple_choice", "options": ["Hedwig", "Errol", "Pigwidgeon", "Fawkes"], "correct_answer": "Hedwig", "category": "Entertainment", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "The Beatles were from Liverpool, England.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What streaming service is known for 'Stranger Things'?", "question_type": "multiple_choice", "options": ["Netflix", "Hulu", "Disney+", "HBO Max"], "correct_answer": "Netflix", "category": "Entertainment", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Elvis Presley was known as the King of Rock and Roll.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What is the name of the wizard in The Lord of the Rings?", "question_type": "text_input", "options": None, "correct_answer": "Gandalf", "category": "Entertainment", "difficulty": "easy", "time_limit": 30, "points": 10},
        
        # Entertainment - Medium
        {"question_text": "The movie 'Titanic' won the Academy Award for Best Picture.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who directed the movie 'Inception'?", "question_type": "text_input", "options": None, "correct_answer": "Christopher Nolan", "category": "Entertainment", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "What year was the first Star Wars movie released?", "question_type": "text_input", "options": None, "correct_answer": "1977", "category": "Entertainment", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The TV show 'Friends' aired for 10 seasons.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who sang 'Bohemian Rhapsody'?", "question_type": "text_input", "options": None, "correct_answer": "Queen", "category": "Entertainment", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "The Lord of the Rings trilogy was filmed in New Zealand.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "What animated movie features the song 'Circle of Life'?", "question_type": "text_input", "options": None, "correct_answer": "The Lion King", "category": "Entertainment", "difficulty": "medium", "time_limit": 30, "points": 15},
        
        # Entertainment - Hard
        {"question_text": "What was the first feature-length animated movie?", "question_type": "text_input", "options": None, "correct_answer": "Snow White", "category": "Entertainment", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Alfred Hitchcock never won an Oscar for Best Director.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "Who composed the music for 'The Godfather'?", "question_type": "text_input", "options": None, "correct_answer": "Nino Rota", "category": "Entertainment", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "What was the first music video played on MTV?", "question_type": "text_input", "options": None, "correct_answer": "Video Killed the Radio Star", "category": "Entertainment", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The movie 'Citizen Kane' was Orson Welles' directorial debut.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Entertainment", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== LITERATURE ====================
        # Literature - Easy
        {"question_text": "Who wrote 'Romeo and Juliet'?", "question_type": "multiple_choice", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "correct_answer": "William Shakespeare", "category": "Literature", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Harry Potter was written by J.K. Rowling.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What is the first book in the Harry Potter series?", "question_type": "multiple_choice", "options": ["Philosopher's Stone", "Chamber of Secrets", "Prisoner of Azkaban", "Goblet of Fire"], "correct_answer": "Philosopher's Stone", "category": "Literature", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Dr. Seuss wrote 'The Cat in the Hat'.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Who wrote 'The Adventures of Tom Sawyer'?", "question_type": "multiple_choice", "options": ["Mark Twain", "Charles Dickens", "Ernest Hemingway", "F. Scott Fitzgerald"], "correct_answer": "Mark Twain", "category": "Literature", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Charlotte's Web features a spider named Charlotte.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What creature is Moby Dick?", "question_type": "text_input", "options": None, "correct_answer": "Whale", "category": "Literature", "difficulty": "easy", "time_limit": 25, "points": 10},
        
        # Literature - Medium
        {"question_text": "'To Kill a Mockingbird' was written by Harper Lee.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who wrote '1984'?", "question_type": "text_input", "options": None, "correct_answer": "George Orwell", "category": "Literature", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What is the name of the whale in Moby Dick?", "question_type": "text_input", "options": None, "correct_answer": "Moby Dick", "category": "Literature", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "Jane Eyre was written by Charlotte Brontë.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who wrote 'The Great Gatsby'?", "question_type": "text_input", "options": None, "correct_answer": "F. Scott Fitzgerald", "category": "Literature", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "Pride and Prejudice was published in 1813.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "In which book would you find the character Atticus Finch?", "question_type": "text_input", "options": None, "correct_answer": "To Kill a Mockingbird", "category": "Literature", "difficulty": "medium", "time_limit": 35, "points": 15},
        
        # Literature - Hard
        {"question_text": "What is the opening line of 'A Tale of Two Cities'?", "question_type": "text_input", "options": None, "correct_answer": "It was the best of times", "category": "Literature", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "James Joyce wrote 'Ulysses'.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "Who wrote 'One Hundred Years of Solitude'?", "question_type": "text_input", "options": None, "correct_answer": "Gabriel García Márquez", "category": "Literature", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "What is the name of the fictional land in C.S. Lewis's chronicles?", "question_type": "text_input", "options": None, "correct_answer": "Narnia", "category": "Literature", "difficulty": "hard", "time_limit": 35, "points": 20},
        {"question_text": "Dante's 'Divine Comedy' has three parts: Inferno, Purgatorio, and Paradiso.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Literature", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== TECHNOLOGY ====================
        # Technology - Easy
        {"question_text": "What does CPU stand for?", "question_type": "multiple_choice", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Computer Processing Unit"], "correct_answer": "Central Processing Unit", "category": "Technology", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Python is a programming language.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "easy", "time_limit": 15, "points": 10},
        {"question_text": "WiFi uses radio waves to connect devices.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What company created the iPhone?", "question_type": "multiple_choice", "options": ["Apple", "Samsung", "Google", "Microsoft"], "correct_answer": "Apple", "category": "Technology", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "USB stands for Universal Serial Bus.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What does RAM stand for?", "question_type": "multiple_choice", "options": ["Random Access Memory", "Read Access Memory", "Rapid Application Memory", "Random Application Memory"], "correct_answer": "Random Access Memory", "category": "Technology", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "Who is the founder of Microsoft?", "question_type": "text_input", "options": None, "correct_answer": "Bill Gates", "category": "Technology", "difficulty": "easy", "time_limit": 25, "points": 10},
        
        # Technology - Medium
        {"question_text": "What does HTML stand for?", "question_type": "multiple_choice", "options": ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"], "correct_answer": "HyperText Markup Language", "category": "Technology", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What year was Google founded?", "question_type": "text_input", "options": None, "correct_answer": "1998", "category": "Technology", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "Linux is an open-source operating system.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who is the founder of Facebook?", "question_type": "text_input", "options": None, "correct_answer": "Mark Zuckerberg", "category": "Technology", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "What does API stand for?", "question_type": "text_input", "options": None, "correct_answer": "Application Programming Interface", "category": "Technology", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "Blockchain technology is used in cryptocurrency.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "What programming language is known for its use in web development?", "question_type": "text_input", "options": None, "correct_answer": "JavaScript", "category": "Technology", "difficulty": "medium", "time_limit": 30, "points": 15},
        
        # Technology - Hard
        {"question_text": "What is the time complexity of binary search?", "question_type": "text_input", "options": None, "correct_answer": "O(log n)", "category": "Technology", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The Turing Test was proposed by Alan Turing.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "What does DDOS stand for?", "question_type": "text_input", "options": None, "correct_answer": "Distributed Denial of Service", "category": "Technology", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Who invented the World Wide Web?", "question_type": "text_input", "options": None, "correct_answer": "Tim Berners-Lee", "category": "Technology", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Moore's Law predicts that transistor count doubles approximately every two years.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Technology", "difficulty": "hard", "time_limit": 30, "points": 20},
        
        # ==================== ART ====================
        # Art - Easy
        {"question_text": "Who painted the Mona Lisa?", "question_type": "multiple_choice", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], "correct_answer": "Leonardo da Vinci", "category": "Art", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "The Starry Night was painted by Vincent van Gogh.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Pablo Picasso was a Spanish painter.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "Which artist is famous for cutting off his own ear?", "question_type": "multiple_choice", "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Salvador Dalí"], "correct_answer": "Vincent van Gogh", "category": "Art", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "The Sistine Chapel ceiling was painted by Michelangelo.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "easy", "time_limit": 20, "points": 10},
        {"question_text": "What primary colors mix to make green?", "question_type": "multiple_choice", "options": ["Yellow and Blue", "Red and Blue", "Red and Yellow", "Blue and Green"], "correct_answer": "Yellow and Blue", "category": "Art", "difficulty": "easy", "time_limit": 25, "points": 10},
        {"question_text": "In which city is the Louvre Museum located?", "question_type": "text_input", "options": None, "correct_answer": "Paris", "category": "Art", "difficulty": "easy", "time_limit": 25, "points": 10},
        
        # Art - Medium
        {"question_text": "The Starry Night was painted by Vincent van Gogh.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who painted 'The Scream'?", "question_type": "text_input", "options": None, "correct_answer": "Edvard Munch", "category": "Art", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "What art movement was Pablo Picasso associated with?", "question_type": "text_input", "options": None, "correct_answer": "Cubism", "category": "Art", "difficulty": "medium", "time_limit": 35, "points": 15},
        {"question_text": "The 'Guernica' was painted by Pablo Picasso.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "Who sculpted 'David'?", "question_type": "text_input", "options": None, "correct_answer": "Michelangelo", "category": "Art", "difficulty": "medium", "time_limit": 30, "points": 15},
        {"question_text": "Impressionism originated in France.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "medium", "time_limit": 25, "points": 15},
        {"question_text": "What technique involves small dots of color?", "question_type": "text_input", "options": None, "correct_answer": "Pointillism", "category": "Art", "difficulty": "medium", "time_limit": 35, "points": 15},
        
        # Art - Hard
        {"question_text": "Who painted 'The Birth of Venus'?", "question_type": "text_input", "options": None, "correct_answer": "Sandro Botticelli", "category": "Art", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Jackson Pollock was a pioneer of abstract expressionism.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "True", "category": "Art", "difficulty": "hard", "time_limit": 30, "points": 20},
        {"question_text": "What is the technique of creating art by assembling different materials?", "question_type": "text_input", "options": None, "correct_answer": "Collage", "category": "Art", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "Who painted 'The Persistence of Memory' with melting clocks?", "question_type": "text_input", "options": None, "correct_answer": "Salvador Dalí", "category": "Art", "difficulty": "hard", "time_limit": 40, "points": 20},
        {"question_text": "The Baroque period preceded the Renaissance.", "question_type": "true_false", "options": ["True", "False"], "correct_answer": "False", "category": "Art", "difficulty": "hard", "time_limit": 30, "points": 20},
    ]
