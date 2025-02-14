// Copyright (c) 2025, Samuael Ketema and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment", {
    contracts: function(frm) {
        if (frm.doc.contracts) {
            console.log("rent amount", frm.doc.amount_paid)
            console.log("commision amount", frm.doc.commission_paid)
            console.log("doc", frm.doc)
            frm.set_value("owner_payment", frm.doc.amount_paid + frm.doc.commission_paid);
            frm.refresh_field()

        }
    }
});

