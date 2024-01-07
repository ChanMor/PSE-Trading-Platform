// Sample data (replace this with your actual data)
const data = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Jane Doe', email: 'jane@example.com' },
    // Add more data as needed
];

// Function to populate the table with data
function populateTable() {
    const tableBody = document.querySelector('#data-table tbody');

    // Clear existing rows
    tableBody.innerHTML = '';

    // Populate the table with data
    data.forEach(item => {
        const row = tableBody.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);

        cell1.textContent = item.id;
        cell2.textContent = item.name;
        cell3.textContent = item.email;
    });
}

// Call the function to initially populate the table\

window.onload = populateTable;

