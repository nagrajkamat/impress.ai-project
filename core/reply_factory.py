
from constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST

def generate_final_response(session):
    PYTHON_QUESTION_LIST = [
        {"id": 1, "question": "What is Python?", "correct_answer": "A"},
        {"id": 2, "question": "What are the data types in Python?", "correct_answer": "B"},
        {"id": 3, "question": "How do you create a function in Python?", "correct_answer": "C"},
        {"id": 4, "question": "what does // operator do?", "correct_answer": "A"},
        {"id": 5, "question": "what is local and global variables?", "correct_answer": "C"},
        {"id": 6, "question": "What is difference between list and tuple?", "correct_answer": "D"},
        {"id": 7, "question": "What does regex do?", "correct_answer": "A"},
        {"id": 8, "question": "What are the frameworks in python?", "correct_answer": "B"},
        {"id": 9, "question": "What is inheritance in python?", "correct_answer": "D"}
    ]

    # Calculate the user's score based on their answers
    user_answers = session.get("user_answers", {})
    correct_count = 0

    for question_info in PYTHON_QUESTION_LIST:
        question_id = question_info["id"]
        correct_answer = question_info["correct_answer"]
        user_answer = user_answers.get(question_id)

        if user_answer and user_answer == correct_answer:
            correct_count += 1

    total_questions = len(PYTHON_QUESTION_LIST)
    score = (correct_count / total_questions) * 100

    # Create the final response message
    final_response = f"Thank you for taking the quiz!\n"
    final_response += f"Your score: {score:.2f}%\n"

    if score >= 70:
        final_response += "Congratulations! You passed the quiz."
    else:
        final_response += "try again."

    return final_response

class QuizSession:
    def __init__(self):
        self.user_answers = {}

    def generate_bot_responses(message, session):
        bot_responses = []
        current_question_id = session.get("current_question_id")

    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id)

    if not success:
        return[error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses



def record_current_answer(answer, current_question_id):
    def __init__(self):
        self.user_answers = {}
        
        if self.is_valid_answer(current_question, answer):
            if user_id not in self.user_answers:
                self.user_answers[user_id] = {}

            self.user_answers[user_id][current_question] = answer
            return True
        else:
            return False

def is_valid_answer(self, question, answer):
    valid_choices = ["A", "B", "C", "D"]
    return answer.upper() in valid_choices



def get_next_question(current_question_id):
    PYTHON_QUESTION_LIST = [
        {"id": 1, "question": "What is PEP8?"},
        {"id": 2, "question": "What are the data types in Python?"},
        {"id": 3, "question": "How do you create a function in Python?"},
        {"id": 4, "question": "what does // operator do?"},
        {"id": 5, "question": "what is local and global variables?"},
        {"id": 6, "question": "What is difference between list and tuple?"},
        {"id": 7, "question": "What does regex do?"},
        {"id": 8, "question": "What are the frameworks in python?"},
        {"id": 9, "question": "What is inheritance in python?"},
    
    ]

    # Find the index of the current question in the list
    current_index = -1
    for i, question_info in enumerate(PYTHON_QUESTION_LIST):
        if question_info["id"] == current_question_id:
            current_index = i
            break

    if current_index == -1:
        # If the current_question_id is not found in the list, return the first question
        return PYTHON_QUESTION_LIST[0]["question"], PYTHON_QUESTION_LIST[0]["id"]

    # Get the next question and its ID
    next_index = (current_index + 1) % len(PYTHON_QUESTION_LIST)
    next_question_info = PYTHON_QUESTION_LIST[next_index]
    next_question = next_question_info["question"]
    next_question_id = next_question_info["id"]

    return next_question, next_question_id

result_message = generate_final_response(session)
print(result_message) 

