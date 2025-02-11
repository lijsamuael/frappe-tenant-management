# Copyright (c) 2025, Samuael Ketema and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	def before_save(self):
		self.full_name = f' {self.title or ""} {self.first_name} {self.last_name or ""}'
