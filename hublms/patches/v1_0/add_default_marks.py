import frappe


def execute():
	frappe.reload_doc("lms", "doctype", "lms_quiz_question")
	frappe.reload_doc("lms", "doctype", "lms_quiz")
	questions = frappe.get_all("Hublms Quiz Question", pluck="name")

	for question in questions:
		frappe.db.set_value("Hublms Quiz Question", question, "marks", 1)

	quizzes = frappe.get_all("Hublms Quiz", pluck="name")

	for quiz in quizzes:
		questions_count = frappe.db.count("Hublms Quiz Question", {"parent": quiz})
		frappe.db.set_value(
			"Hublms Quiz", quiz, {"total_marks": questions_count, "passing_percentage": 100}
		)
