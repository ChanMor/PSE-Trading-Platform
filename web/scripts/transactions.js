async function updateTransactions() {
    var userId = getUserId();
    var transactionsApiUrl = `http://127.0.0.1:8000/users/${userId}/transaction`;


    try {
        // Fetch data from the API
        var response = await fetch(transactionsApiUrl);

        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }

        var transactions = await response.json();

        const transactionsContainer = document.getElementById('transactions-content');

        // Clear existing content
        transactionsContainer.innerHTML = '';

        // Group transactions by month
        const transactionsByMonth = groupTransactionsByMonth(transactions);

        // Iterate through each month's transactions
        for (const [month, monthTransactions] of transactionsByMonth.entries()) {
            const sanitizedMonth = month.replace(/\s/g, ''); 
        
            const monthLabel = document.createElement('div');
            monthLabel.innerHTML = `${month}`;
            monthLabel.classList.add(`month`);
        
            const monthTable = createMonthTable(month, monthTransactions);
        
            transactionsContainer.appendChild(monthLabel);
            transactionsContainer.appendChild(monthTable);
        }
        
    } catch (error) {
        console.error('Error updating transactions:', error);
    } 
}

function groupTransactionsByMonth(transactions) {
    // Group transactions by month using a Map
    const transactionsByMonth = new Map();

    transactions.reverse().forEach(trans => {
        const transactionDate = new Date(trans.transaction_date);
        const month = transactionDate.toLocaleString('en-US', { month: 'long', year: 'numeric' });

        if (!transactionsByMonth.has(month)) {
            transactionsByMonth.set(month, []);
        }

        transactionsByMonth.get(month).push(trans);
    });

    return transactionsByMonth;
}

function createMonthTable(month, transactions) {
    const sanitizedMonth = month.replace(/\s/g, ''); // Remove spaces to create a valid HTML ID
    
    const monthTable = document.createElement('table');
    monthTable.innerHTML = `
        <thead>
            <tr>
                <th>Date</th>
                <th>Transaction</th>
                <th>Stock</th>
                <th>Shares</th>
                <th>Price</th>
                <th>Gross Amount</th>
            </tr>
        </thead>
        <tbody id="userTransactions-${sanitizedMonth}">
        </tbody>
    `;

    const monthBody = monthTable.querySelector(`#userTransactions-${sanitizedMonth}`);

    transactions.forEach(trans => {

        const transactionClass = trans.transaction_type === 'BUY';
        const typeClass = transactionClass ? 'buy' : 'sell';

        const date = trans.transaction_date.split("T")[0];

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${date}</td>
            <td class=${typeClass}>${trans.transaction_type}</td>
            <td>${trans.symbol}</td>
            <td>${trans.total_shares}</td>
            <td>${trans.price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
            <td>${trans.gross_amount.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
        `;
        monthBody.appendChild(row);
    });

    return monthTable;
}





window.onload = updateTransactions();

function signOut() {
    window.location.href = "index.html";
}

function trade() {
    saveUserId("trade.html")
}

function listings() {
    saveUserId("listings.html")
}

function transactions() {
    saveUserId("transactions.html")
}

function dashboard() {
    saveUserId("dashboard.html")
}

function account() {
    saveUserId("account.html");
}  


function getUserId() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const encodedData = urlParams.get('data');
    const apiData = JSON.parse(decodeURIComponent(encodedData));
    return apiData.key
}


async function saveUserId(html) {
    const apiData = { key: getUserId() };
    const queryString = `?data=${encodeURIComponent(JSON.stringify(apiData))}`;

    window.location.href = `${html}${queryString}`;
}