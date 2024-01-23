// Copyright (c) 2023, Hublms and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Hublms Course", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Hublms Course', {
    refresh: function(frm) {
        // Add a trigger on child_field to update options
       
        frm.fields_dict['course_topics'].grid.get_field('prerequisite').get_query = function(doc, cdt, cdn) {
            var child_row = locals[cdt][cdn];
                // Filter options based on the parent's value
                return {
                    filters: {
                        'parent': frm.doc.name,
                        'name': ['!=', child_row.name]
                    }
                };
            
            
        };
    }
});