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
		if not self.address:
			self.address = self.house.address
