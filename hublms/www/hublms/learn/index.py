import frappe
from frappe import _
from frappe.utils import cstr, flt
from hublms.hublms.md import markdown_to_html
from hublms.hublms.utils import  get_membership
# from hublms.hublms.utils import (
# 	get_lesson_url,
# 	has_course_moderator_role,
# 	is_instructor,
# 	has_course_evaluator_role,
# )
# from hublms.www.utils import (
# 	get_common_context,
# 	redirect_to_lesson,
# 	get_current_lesson_details,
# )


def get_context(context):
    topic_index = frappe.form_dict.get("topic")
    content_index = frappe.form_dict.get("content")
    course_name = frappe.form_dict.get("course")
    context.topic_index = topic_index
    context.content_index = content_index
    context.course = frappe.db.get_value(
		"Hublms Course",
		frappe.form_dict["course"],
		["name", "title", "video_link", "enable_certification", "status"],
		as_dict=True,
	)
    context.topic = frappe.db.get_value(
        "Hublms Topic Reference", {"idx": topic_index, "parent": course_name}, "topics"
    )
    content = frappe.db.get_value(
        "Hublms Topic Content", {"idx": content_index, "parent": context.topic}, ["content","creation"], as_dict=True
    )
    context.topic_content = content.content
    context.creation = content.creation
    
    context.show_lesson = True
    context.page_context = {
		"course": context.course.name,
		"content": content.content if content.content else "New Content",
		"is_member": context.membership is not None,
	}
    
    membership = get_membership(context.course.name, frappe.session.user)
    context.membership = membership
    context.progress = frappe.utils.cint(membership.progress) if membership else 0
    
    

	
