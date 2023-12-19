import frappe
from frappe import _
import random

def get_context(context):
    context.no_cache = 1
    
    quiz_name = "quiz-1"
    quiz = frappe.db.get_value(
    "Hublms Quiz",
    quiz_name,
    [
    "name",
    "time",
    "title",
    "randomize_questions",
    "subset",
    "max_attempts",
    "show_answers",
    "show_submission_history",
    "passing_percentage",
    ],
    as_dict=True,
    )
    quiz.questions = []
    fields = ["name", "question", "type", "multiple"]
    for num in range(1, 5):
        fields.append(f"option_{num}")
        fields.append(f"is_correct_{num}")
        fields.append(f"explanation_{num}")
        fields.append(f"possibility_{num}")

    questions = frappe.get_all(
		"Hublms Quiz Question",
		filters={"parent": quiz.name},
		fields=["question", "marks"],
		order_by="idx",
	)
    if quiz.randomize_questions == True:
        random.shuffle(questions)

    submission = frappe.get_value(
        "Hublms Quiz Submission",
        {
            "quiz": quiz.name,
            "member": frappe.session.user,
            "name" : "c435e1f244"
        },
        ["name", "score", "creation"],
        order_by="creation desc",
        as_dict=True,
    )
    answers = frappe.get_all(
        "Hublms Quiz Result",
        {
            "parent" : submission.name
        },
        ["*"],
        order_by="creation desc",
    )
    questions = questions[:int(quiz.subset)]
    for question in questions:
        details = frappe.db.get_value("Hublms Question", question.question, fields, as_dict=1)
        details["marks"] = question.marks
        for answer in answers:
            if answer.question == details.question:
                details["answer"] = answer.answer
                details["is_correct"] = answer.is_correct
        quiz.questions.append(details)

    no_of_attempts = frappe.db.count(
        "Hublms Quiz Submission", {"owner": frappe.session.user, "quiz": quiz_name}
    )

    
        
    context.submission = submission
    context.answers = answers
    context.quiz = quiz
    context.no_of_attempts = no_of_attempts
    
    context.hide_quiz = False
    