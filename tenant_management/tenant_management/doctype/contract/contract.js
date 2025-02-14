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

frappe.ui.form.on("Contract", {
    start_date: function (frm) {
        if (frm.doc.start_date) {
            let startDate = frappe.datetime.str_to_obj(frm.doc.start_date);
            let endDate = frappe.datetime.add_months(startDate, 1);
            frm.set_value("end_date", frappe.datetime.obj_to_str(endDate));
        }
    },
    //  here is the code to change the status to expired
    refresh: function (frm) {
        if (frm.doc.end_date) {
            let currentDate = frappe.datetime.get_today();
            if (frappe.datetime.str_to_obj(frm.doc.end_date) < frappe.datetime.str_to_obj(currentDate)) {
                frm.set_value("contract_status", "Expired");
                frm.save();
            }
        }
    }
});


frappe.ui.form.on("Contract", {
    refresh: function (frm) {
        if (frm.doc.contract_status === "Expired") {
            frm.add_custom_button("View Expired Contracts", function () {
                frappe.route_options = { "contract_status": "Expired" };
                frappe.set_route("List", "Contract");
            }, "Actions");
        }
        
    }
});

frappe.call({
    method: "tenant_management.tenant_management.doctype.contract.contract.get_expired_contracts",
    callback: function (response) {
        console.log(response.message); 
    }
});

// make the status of contarct cahnged to terminated 
// frappe.ui.form.on("Contract", {
//     refresh: function (frm) {
//         if (frm.doc.contract_status === "Active" && frm.doc.docstatus === 1){
//             frm.add_custom_button("Terminate Contract", function () {
//                 frappe.call({
//                     method: "tenant_management.tenant_management.doctype.contract.contract.terminate_contract",
//                     args: {
//                         contract_name: frm.doc.name
//                     },
//                     callback: function (r) {
//                         if (!r.exc) {
//                             frm.reload_doc();  
//                             frappe.msgprint("Contract has been terminated successfully.");
//                         }
//                     }
//                 });
//             });
//         }
//     }
// });
frappe.ui.form.on("Contract", {
    refresh: function (frm) {
        if (frm.doc.contract_status === "Active" && frm.doc.docstatus === 1) {
            frm.add_custom_button("Terminate Contract", function () {
                frappe.prompt(
                    [
                        {
                            fieldname: "termination_reason",
                            label: " Termination Reason",
                            fieldtype: "Small Text",
                            // reqd: 1
                        }
                    ],
                    function (values) {
                        frappe.call({
                            method: "tenant_management.tenant_management.doctype.contract.contract.terminate_contract",
                            args: {
                                contract_name: frm.doc.name,
                                termination_reason: frm.doc.termination_reason || "terminate the contract"
                            },
                            callback: function (r) {
                                if (!r.exc) {
                                    frappe.msgprint("Contract terminated successfully.");
                                    frm.reload_doc();
                                }
                            }
                        });
                    },
                    "Terminate Contract",
                    "Submit"
                );
            });
        }
    }
});


frappe.ui.form.on("House", {
    refresh: function (frm) {
        frappe.realtime.on("contract_terminated", (data) => {
            if (data.house_name === frm.doc.name) {
                frm.reload_doc(); 
            }
        });
    }
});




