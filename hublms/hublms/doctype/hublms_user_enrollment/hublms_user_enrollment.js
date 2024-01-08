// Copyright (c) 2023, Hublms and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hublms User Enrollment", {
	
    view_progress: function(frm) {
        let apiUrl = `hublms.hublms.doctype.hublms_user_enrollment.hublms_user_enrollment.test`;
        frappe.call({
            method: apiUrl,
            args: {
                course: frm.doc.course,
                progress: frm.doc.progress,
            },
            callback: function(response) {
                if (response.message) {
                    frappe.msgprint(response.message);
                }
            }
        });
        
    },
    
	refresh(frm) {

	},
    preview: function(frm) {

    },
});
