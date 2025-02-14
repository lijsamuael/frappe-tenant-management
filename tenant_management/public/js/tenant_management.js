// tenant_management.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('Tenant Management JS Loaded');

    // Fetch and populate the list of doctypes
    fetchDoctypes();
});

function fetchDoctypes() {
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "DocType",
            fields: ["name"]
        },
        callback: function(response) {
            if (response.message) {
                populateDoctypeList(response.message);
            }
        }
    });
}

function populateDoctypeList(doctypes) {
    const doctypeList = document.getElementById('doctype-list');
    const listItem = document.createElement('li');
    doctypes.forEach(doctype => {
        const listItem = document.createElement('li');
        listItem.textContent = doctype.name;
        doctypeList.appendChild(listItem);
    });
}