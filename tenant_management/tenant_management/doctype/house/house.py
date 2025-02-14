# Copyright (c) 2025, Samuael Ketema and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class House(Document):
	pass


@frappe.whitelist()
def make_contract(source_name, target_doc=None):
	
	contract = frappe.new_doc("Contract")
	contract.house = source_name
	return contract
#  default status of the  to rent
class House(Document):
    def before_insert(self):
        if not self.status:
            self.status = "Open for rent"
