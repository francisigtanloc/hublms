import frappe


def execute():
	frappe.reload_doc("lms", "doctype", "lms_question")

	fields = ["name", "question", "type", "multiple"]
	for num in range(1, 5):
		fields.append(f"option_{num}")
		fields.append(f"is_correct_{num}")
		fields.append(f"explanation_{num}")
		fields.append(f"possibility_{num}")

	questions = frappe.get_all(
		"Hublms Quiz Question",
		fields=fields,
	)

	for question in questions:
		print(question.name)
		doc = frappe.new_doc("Hublms Question")
		doc.update(
			{
				"question": question.question,
				"type": question.type,
				"multiple": question.multiple,
			}
		)

		for num in range(1, 5):
			if question.get(f"option_{num}"):
				doc.update(
					{
						f"option_{num}": question[f"option_{num}"],
						f"is_correct_{num}": question[f"is_correct_{num}"],
						f"explanation_{num}": question[f"explanation_{num}"],
						f"possibility_{num}": question[f"possibility_{num}"],
					}
				)

		doc.save()
		print(doc.name)
		frappe.db.set_value("Hublms Quiz Question", question.name, "question", doc.name)
