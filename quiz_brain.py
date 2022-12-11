class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.correct_count = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def correct_answer(self, response, actual_answer):
        if response == actual_answer:
            print("Correct!\n")
            self.correct_count += 1
        else:
            print("Incorrect.")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q{self.question_number}. {current_question.text} True or False? ").title()
        self.correct_answer(response, current_question.answer)


    def total_score(self):
        print(f"You got {self.correct_count} out of {len(self.question_list)}!")

        if self.correct_count / len(self.question_list) == 1:
            print("Perfect score! Incredible!")
        elif self.correct_count / len(self.question_list) >= .8:
            print("Good job!")
        elif self.correct_count / len(self.question_list) >= .7:
            print("Not bad. I know you can do better.")
        else:
            print("I know you can do better.")