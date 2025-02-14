# Copyright (c) 2025, Samuael Ketema and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Contract(Document):
	def validate(self):
		if not self.house_serial_number:
			self.house_serial_number = self.house.serial_number
		if not self.rent_amount:
			self.rent_amount = self.house.rent_amount
		# if not self.address:
		# 	self.address = self.house.address


import frappe

def calculate_commission(doc, method):
    if doc.broker:
        broker = frappe.get_doc("Broker", doc.broker)
        if broker.commission_type == "Fixed":
            commission_value = broker.commission_value
        elif broker.commission_type == "Percentage":
            commission_value = (broker.commission_value / 100) * doc.rent_amount
        else:
            commission_value = 0  # Default to 0 if no valid commission type

        # Ensure commission value is set before submission
        frappe.logger().info(f"Setting Commission for Contract {doc.name}: {commission_value}")

        # Use db_set to avoid validation errors after submission
        doc.db_set("commission_amount", round(commission_value, 2))

@frappe.whitelist()
def make_payment(contract_id, amount):
    contract = frappe.get_doc("Contract", contract_id)

    # Ensure commission_amount is fetched properly
    commission = contract.commission_amount or 0  # Avoid None values
    owner_payment = amount - commission  # Ensure proper calculation

    # Debugging: Print values before inserting
    frappe.logger().info(f"Creating Payment: Amount Paid={amount}, Commission={commission}, Owner Payment={owner_payment}")

    # Create Payment entry
    payment = frappe.get_doc({
        "doctype": "Payment",
        "contract": contract_id,
        "tenant": contract.tenant,
        "amount_paid": amount,
        "commission_paid": commission,
        "owner_payment": owner_payment  # Ensure correct subtraction
    })
    
    # Save Payment entry
    payment.insert()
    frappe.db.commit()

    return payment.name
def on_save(doc, method):
    calculate_commission(doc, method)