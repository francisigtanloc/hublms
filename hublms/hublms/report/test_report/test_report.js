frappe.query_reports['Test Report'] = {
    onload: function (report) {
        // Log a message to the console to check if the onload event is triggered
        console.log('Query Report onload event triggered');

        // Attach click event to each row
        report.page.main.on('click', '.list-row', function () {
            // Log a message to the console to check if the click event is triggered
            console.log('Row clicked');
            
            // Alert message
            alert("Row clicked");

            // Uncomment the following line if you want to redirect to a form
            // frappe.set_route('Form', 'Hublms Course', doc.name);
        });
    }
};