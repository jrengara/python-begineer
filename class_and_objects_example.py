from student import Student
from Question import Question

student1 = Student("one", "Business", "3.5", False)
student2 = Student("two", "HR", "2.1", False)

print(student1.gpa)
print(student2.gpa)

print(student1.on_honor_roll())


'''
Below code for multiple choice question
'''
question_prompts = [
    "What color are apple?\n(a) Red\n(b) Yellow\n(c) Orange\n",
    "What color are banana?\n(a) Yellow\n(b) red\n(c) blue\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        ans = input(question.prompt)
        if ans == question.answer:
            score = score + 1

    return score


#print("you score is - " + str(run_test(questions)))


