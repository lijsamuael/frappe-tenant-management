import frappe

def on_submit(doc, method):
    frappe.msgprint("Contract has been submitted successfully!")

    if doc.house:
        house = frappe.get_doc("House", doc.house)
        house.status = "Rented"
        house.save()
        frappe.db.commit()

    # Ensure commission is only set if it's currently 0
    if not doc.commission_amount and doc.broker:
        broker = frappe.get_doc("Broker", doc.broker)
        if broker.commission_type == "Fixed":
            commission_value = broker.commission_value
        elif broker.commission_type == "Percentage":
            commission_value = (broker.commission_value / 100) * doc.rent_amount
        else:
            commission_value = 0  # Default if no valid type

        frappe.logger().info(f"Final Commission Set on Submit: {commission_value}")

        # Directly update the field in the database
        doc.db_set("commission_amount", round(commission_value, 2))
