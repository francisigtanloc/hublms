import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    table_fieldname = "course_topics"
    # course_name = frappe.form_dict["course"]
    context.course_list     = frappe.db.get_list('Hublms Course', "*")
    context.course_all      = frappe.db.get_all('Hublms Course', "*")
    context.course_value    = frappe.db.get_value('Hublms Course','Course 102', ["name","*"])
    
    context.course_doc      = frappe.get_doc('Hublms Course', 'Course 102')

    # Define the doctype and fieldnames
    parent_doctype = "Sales Order"
    table_fieldname = "items"

    # Specify the fields you want to retrieve, including the table field
    fields = ["name", "customer", "transaction_date", f"{table_fieldname}*item", f"{table_fieldname}*quantity", f"{table_fieldname}*rate"]
    context.test  = frappe.get_list(
        parent_doctype,
        fields=fields,
        filters={"status": "Open"},  # Add any filters as needed
        limit=10  # Limit the number of records returned (optional)
    )