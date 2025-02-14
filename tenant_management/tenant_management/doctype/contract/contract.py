# Copyright (c) 2025, Samuael Ketema and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
            doc.commission_amount = broker.commission_value
        elif broker.commission_type == "Percentage":
            doc.commission_amount = (broker.commission_value / 100) * doc.rent_amount


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
from dateutil.relativedelta import relativedelta

from datetime import datetime

class Contract(Document):
    def validate(self):
        if self.contract_status == "Active":
            self.contract_status = "Active"

        elif self.contract_status == "Terminated":
            self.contract_status = "Terminated"

        elif self.end_date:
            try:
                end_date_obj = datetime.strptime(self.end_date, "%Y-%m-%d")
                current_date = datetime.now()

                if current_date > end_date_obj:
                    self.contract_status = "Expired"
            except ValueError:
                frappe.throw("Invalid end date format. Please use the correct format (yyyy-mm-dd).")
        
        if not self.contract_status:
            self.contract_status = "Active" 

        self.save()
#  feaching the expired contracts 
class Contract(Document):
    def validate(self):
        if self.end_date:
            try:
                end_date_obj = datetime.strptime(self.end_date, "%Y-%m-%d")
                current_date = datetime.now()

                if current_date > end_date_obj:
                    self.contract_status = "Expired"
            except ValueError:
                frappe.throw("Invalid end date format. Please use YYYY-MM-DD.")

    # def on_submit(self):
        
        
    #     if self.contract_status in ["Active", "Terminated", "Expired"]:
    #         self.docstatus = 1  

@frappe.whitelist()
def update_expired_contracts():
    expired_contracts = frappe.get_all(
        "Contract",
        filters={"contract_status": ["!=", "Expired"], "end_date": ["<", frappe.utils.today()]},
        fields=["name"]
    )

    for contract in expired_contracts:
        doc = frappe.get_doc("Contract", contract.name)
        doc.contract_status = "Expired"
        doc.save()
        frappe.db.commit()
        # fetch the expired contract

@frappe.whitelist()
def get_expired_contracts():
    contracts = frappe.get_all(
        "Contract",
        filters={"contract_status": "Expired"},
        fields=["name", "tenant", "house", "start_date", "end_date", "contract_status"]
    )
    return contracts

# to make the  active contracts to be terminated 


# @frappe.whitelist()
# def terminate_contract(contract_name):
#     contract = frappe.get_doc("Contract", contract_name)

#     frappe.msgprint(f"Current contract status: {contract.contract_status}")

#     if contract.contract_status == "Active":
#         frappe.db.set_value("Contract", contract_name, "contract_status", "Terminated")
        
#         if contract.house:
#             house = frappe.get_doc("House", contract.house)
#             frappe.db.set_value("House", house.name, "status", "Open for Rent")
#             frappe.publish_realtime('contract_terminated', {'house_name': contract.house})

#             frappe.db.commit()
#         frappe.msgprint("Contract has been terminated successfully and house status updated to open to rent.")
        
#     else:
#         frappe.throw("Contract status must be 'Active' to terminate it.")

from frappe.utils import nowdate

import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def terminate_contract(contract_name, termination_reason):

    contract = frappe.get_doc("Contract", contract_name)
    
    frappe.msgprint(f"Current contract status: {contract.contract_status}")

    if contract.contract_status == "Active":
      frappe.db.set_value("Contract", contract_name, "contract_status", "Terminated")
        
    termination_entry = frappe.get_doc({
        "doctype": "Terminate Contract",
        "contract": contract_name,
        "termination_date": nowdate(),
        "termination_reason": termination_reason
    })
    termination_entry.insert(ignore_permissions=True)

    # Update contract status to Terminated
    frappe.db.set_value("Contract", contract_name, "contract_status", "Terminated")

    # Update house status if linked
    if contract.house:
        frappe.db.set_value("House", contract.house, "status", "Open for Rent")

    frappe.msgprint("Contract has been terminated successfully, and the house is now open for rent.")

  