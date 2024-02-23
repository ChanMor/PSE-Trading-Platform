
function getUserId() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const encodedData = urlParams.get('data');
    const apiData = JSON.parse(decodeURIComponent(encodedData));
    return apiData.key
}

async function updateDashboard() {
    updateData();
    var user_id = getUserId();

    var portfolioApiUrl = `http://127.0.0.1:8000/users/${user_id}/portfolio`
    var positionsApiUrl = `http://127.0.0.1:8000/users/${user_id}/positions`

    var portfolioResponse = await fetch(portfolioApiUrl);
    var portfolioData = await portfolioResponse.json();

    var positionsResponse = await fetch(positionsApiUrl);
    var positionsData = await positionsResponse.json();

    document.getElementById('cashBalance').innerText = portfolioData[0].cash_balance.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById('totalEquities').innerText = portfolioData[0].total_equities.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');


    const openPositionsElement = document.getElementById('openPositions');
    openPositionsElement.innerHTML = '';

    positionsData.forEach(position => {

        const isNegative = position.gain_loss < 0;
        const priceClass = isNegative ? 'negative' : 'positive';


        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <button class="buyButton" type="button" onclick="promptTransaction('buy');">Buy</button>  
                <button class="sellButton" type="button" onclick="promptTransaction('sell');">Sell</button>
            </td>
            <td class="symbol">${position.symbol}</td>
            <td>${position.average_price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
            <td>${position.total_shares}</td>
            <td>${position.current_market_price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
            <td>${position.market_value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
            <td class=${priceClass}>${position.gain_loss.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}</td>
            <td class=${priceClass}>${position.percentage_gain_loss}%</td>
        `;
        openPositionsElement.appendChild(row);
    });
}

window.onload = updateDashboard();

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

function account() {
    saveUserId("account.html");
}

function buyPosition(){

}

function sellPosition(){

}

async function saveUserId(html) {
    const apiData = { key: getUserId() };
    const queryString = `?data=${encodeURIComponent(JSON.stringify(apiData))}`;

    window.location.href = `${html}${queryString}`;
}

async function promptTransaction(transactionType) {
    const tableRow = event.target.closest('tr');
    const stockCodeElement = tableRow.querySelector('.symbol');
    const stockCode = stockCodeElement.textContent.trim();

    const sharesInput = prompt(`Enter the number of shares to ${transactionType}:`);

    if (sharesInput === null || sharesInput.trim() === '' || isNaN(sharesInput) || parseInt(sharesInput) <= 0) {
        alert("Invalid number of shares!");
        return;
    }

    const quantity = parseInt(sharesInput);

    const transactionApiUrl = `http://127.0.0.1:8000/actions/${transactionType}`;
    const user_id = getUserId();

    const requestData = {
        user_id: user_id,
        stock_symbol: stockCode,
        shares: quantity,
    };

    await fetch(transactionApiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
        const alertMessage = data.message;
        updateDashboard();
        alert(alertMessage);
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Transaction Failed");
    });
}

async function updateData() {
    const updateDataApiUrl = 'http://127.0.0.1:8000/actions/update/data';
    try {

        const response = await fetch(updateDataApiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },        
        });

        if (!response.ok) {
            throw new Error('Failed to update data');
        }

        console.log('Data updated successfully!');

    } catch (error) {
        console.log("tangina");

        console.error('Error:', error);
    }
}
