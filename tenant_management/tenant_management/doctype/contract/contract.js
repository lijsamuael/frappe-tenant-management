// Copyright (c) 2025, Samuael Ketema and contributors
// For license information, please see license.txt

cur_frm.add_fetch("house", "serial_number", "house_serial_number");


frappe.ui.form.on('Contract', {
    start_date: function(frm) {
        if (frm.doc.start_date) {
            let startDate = frappe.datetime.str_to_obj(frm.doc.start_date);
            let endDate = frappe.datetime.add_months(startDate, 1);
            frm.set_value('end_date', frappe.datetime.obj_to_str(endDate));
        }
    }
});




frappe.ui.form.on("Contract", {
    refresh: function(frm) {
        frm.set_query("house", function() {
            return {
                filters: {
                    status: ["!=", "Rented"]  // Exclude rented houses
                }
            };
        });
    }
});
frappe.ui.form.on('Contract', {
    start_date: function(frm) {
        if (frm.doc.start_date) {
            let startDate = frappe.datetime.str_to_obj(frm.doc.start_date);
            let endDate = frappe.datetime.add_months(startDate, 1);
            frm.set_value('end_date', frappe.datetime.obj_to_str(endDate));
        }
    }
});
