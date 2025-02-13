import frappe

def on_submit(doc, method):
    frappe.msgprint("Contract has been submitted successfully!")

    if doc.house:
        house = frappe.get_doc("House", doc.house)
        house.status = "Rented"
        house.save()
        frappe.db.commit()

    # Calculate broker commission BEFORE submission
    if not doc.commission_amount and doc.broker:
        broker = frappe.get_doc("Broker", doc.broker)
        if broker.commission_type == "Fixed":
            doc.commission_amount = round(float(broker.commission_value), 2)
        elif broker.commission_type == "Percentage":
            doc.commission_amount = round((broker.commission_value / 100) * doc.rent_amount, 2)
