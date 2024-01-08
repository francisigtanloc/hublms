# Copyright (c) 2023, Hublms and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HublmsUserEnrollment(Document):
	pass


@frappe.whitelist()
def test(course,progress):
    return frappe.render_template("templates/course_outline.html", {
			"course" : course,
			"progress" : progress,
		})
	