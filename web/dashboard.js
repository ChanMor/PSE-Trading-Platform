
function getUserId() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const encodedData = urlParams.get('data');
    const apiData = JSON.parse(decodeURIComponent(encodedData));
    return apiData.key
}

async function updateDashboard() {
    var user_id = getUserId();

    var portfolioApiUrl = `http://127.0.0.1:8000/users/${user_id}/portfolio`
    var positionsApiUrl = `http://127.0.0.1:8000/users/${user_id}/positions`

    var portfolioResponse = await fetch(portfolioApiUrl);
    var portfolioData = await portfolioResponse.json();

    var positionsResponse = await fetch(positionsApiUrl);
    var positionsData = await positionsResponse.json();

    console.log(positionsData)

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
                <button class="buyButton" type="button" onclick="buyPosition();">Buy</button>  
                <button class="sellButton" type="button" onclick="sellPosition();">Sell</button>
            </td>
            <td>${position.symbol}</td>
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

window.onload = updateDashboard;

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

function buyPosition(){

}

function sellPosition(){

}

async function saveUserId(html) {
    const apiData = { key: getUserId() };
    const queryString = `?data=${encodeURIComponent(JSON.stringify(apiData))}`;

    window.location.href = `${html}${queryString}`;
}