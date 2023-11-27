app_name = "hublms"
app_title = "Hublms"
app_publisher = "Hublms"
app_description = "Hublms"
app_email = "info@hublms.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hublms/css/hublms.css"
# app_include_js = "/assets/hublms/js/hublms.js"

# include js, css files in header of web template
# web_include_css = "/assets/hublms/css/hublms.css"
# web_include_js = "/assets/hublms/js/hublms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hublms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hublms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hublms.utils.jinja_methods",
#	"filters": "hublms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hublms.install.before_install"
# after_install = "hublms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hublms.uninstall.before_uninstall"
# after_uninstall = "hublms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hublms.utils.before_app_install"
# after_app_install = "hublms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hublms.utils.before_app_uninstall"
# after_app_uninstall = "hublms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hublms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hublms.tasks.all"
#	],
#	"daily": [
#		"hublms.tasks.daily"
#	],
#	"hourly": [
#		"hublms.tasks.hourly"
#	],
#	"weekly": [
#		"hublms.tasks.weekly"
#	],
#	"monthly": [
#		"hublms.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hublms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hublms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hublms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hublms.utils.before_request"]
# after_request = ["hublms.utils.after_request"]

# Job Events
# ----------
# before_job = ["hublms.utils.before_job"]
# after_job = ["hublms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hublms.auth.validate"
# ]

update_website_context = [
	"hublms.widgets.update_website_context",
]

# Add all simple route rules here
website_route_rules = [
	{"from_route": "/sketches/<sketch>", "to_route": "sketches/sketch"},
	{"from_route": "/hublms/<course>", "to_route": "courses/course"},
	{"from_route": "/hublms/<course>/edit", "to_route": "courses/create"},
	{"from_route": "/hublms/<course>/outline", "to_route": "courses/outline"},
	{"from_route": "/hublms/<course>/<certificate>", "to_route": "courses/certificate"},
	{"from_route": "/hublms/<course>/learn", "to_route": "batch/learn"},
	{
		"from_route": "/hublms/<course>/learn/<int:chapter>.<int:lesson>",
		"to_route": "batch/learn",
	},
	{
		"from_route": "/hublms/<course>/learn/<int:chapter>.<int:lesson>/edit",
		"to_route": "batch/edit",
	},
	{"from_route": "/quizzes", "to_route": "batch/quiz_list"},
	{"from_route": "/quizzes/<quizname>", "to_route": "batch/quiz"},
	{"from_route": "/batches/<batchname>", "to_route": "batches/batch"},
	{"from_route": "/hublms/<course>/progress", "to_route": "batch/progress"},
	{"from_route": "/hublms/<course>/join", "to_route": "batch/join"},
	{"from_route": "/hublms/<course>/manage", "to_route": "cohorts"},
	{"from_route": "/hublms/<course>/cohorts/<cohort>", "to_route": "cohorts/cohort"},
	{
		"from_route": "/hublms/<course>/cohorts/<cohort>/<page>",
		"to_route": "cohorts/cohort",
	},
	{
		"from_route": "/hublms/<course>/subgroups/<cohort>/<subgroup>",
		"to_route": "cohorts/subgroup",
	},
	{
		"from_route": "/hublms/<course>/subgroups/<cohort>/<subgroup>/<page>",
		"to_route": "cohorts/subgroup",
	},
	{
		"from_route": "/hublms/<course>/join/<cohort>/<subgroup>/<invite_code>",
		"to_route": "cohorts/join",
	},
	{"from_route": "/users", "to_route": "profiles/profile"},
	{"from_route": "/jobs/<job>", "to_route": "jobs/job"},
	{
		"from_route": "/batches/<batchname>/students/<username>",
		"to_route": "/batches/progress",
	},
	{"from_route": "/assignments/<assignment>", "to_route": "assignments/assignment"},
	{
		"from_route": "/assignment-submission/<assignment>/<submission>",
		"to_route": "assignment_submission/assignment_submission",
	},
	{
		"from_route": "/quiz-submission/<quiz>/<submission>",
		"to_route": "quiz_submission/quiz_submission",
	},
	{
		"from_route": "/billing/<module>/<modulename>",
		"to_route": "billing/billing",
	},
	{
		"from_route": "/batches/details/<batchname>",
		"to_route": "batches/batch_details",
	},
	{
		"from_route": "/certified-participants",
		"to_route": "certified_participants/certified_participants",
	},
]