// Copyright (c) 2025, Samuael Ketema and contributors
// For license information, please see license.txt

frappe.ui.form.on("House", {
	refresh(frm) {

        frm.add_custom_button(__('Contract'), function () {
            frappe.model.open_mapped_doc({
                method: "tenant_management.tenant_management.doctype.house.house.make_contract",
                frm: frm,
                freeze_message: __("Creating Contract...")
            })
        }, __('Create'));
        
	}, 
});
