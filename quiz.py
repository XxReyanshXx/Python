
class Quiz:
    def __init__(self):
        self.score = 0

    def start_quiz(self):
        questions = [
            ["What is the capital of India?", "Delhi"],
            ["How many days are in a week?", "7"],
            ["What is 5 + 5?", "10"],
            ["Which planet is known as the Red Planet?", "Mars"],
            ["How many sides does a triangle have?", "3"]
        ]

        for q in questions:
            print("\n" + q[0])
            answer = input("Your answer: ")

            if answer.lower() == q[1].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Wrong! The answer is", q[1])

        print("\nYour final score is", self.score, "out of", len(questions))


quiz1 = Quiz()
quiz1.start_quiz()
