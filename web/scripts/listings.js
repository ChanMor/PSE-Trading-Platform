async function updateListings() {
    var listingsApiUrl = "http://127.0.0.1:8000/stocks/listings";

    // Display loading screen
    document.getElementById('loading-screen').style.display = 'flex';

    try {
        // Fetch data from the API
        var response = await fetch(listingsApiUrl);

        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }

        var listings = await response.json();

        const sanitizedMonth = "listings"; // You can adjust this based on your needs
        const listingsTable = createListingsTable(listings, sanitizedMonth);

        const listingsContainer = document.getElementById('listings-content');


        listingsContainer.innerHTML = '';

        const headingElement = document.createElement('h2');
        headingElement.textContent = 'PSE Listed Stocks';

        const headingParagraph = document.createElement('p');
        headingParagraph.textContent = 'Real time stock prices data, web scraped from pesobility.com';

        listingsContainer.appendChild(headingElement);
        listingsContainer.appendChild(headingParagraph);
        listingsContainer.appendChild(listingsTable);
    } catch (error) {
        console.error('Error updating listings:', error);
    } finally {
        // Hide loading screen
        document.getElementById('loading-screen').style.display = 'none';
    }
}

function createListingsTable(listings, sanitizedMonth) {
    const listingsTable = document.createElement('table');
    listingsTable.innerHTML = `
        <thead>
            <tr>
                <th>Symbol</th>
                <th>Name</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody id="userListings-${sanitizedMonth}">
        </tbody>
    `;

    const listingsBody = listingsTable.querySelector(`#userListings-${sanitizedMonth}`);

    listings.forEach(stock => {
        const [price, change] = stock.price.split(" ");
        const isNegative = stock.price.includes('-');
        const priceClass = isNegative ? 'negative' : 'positive';

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${stock.symbol}</td>
            <td>${stock.name}</td>
            <td>${price} <span class="${priceClass}">${change}%</span></td>
        `;
        listingsBody.appendChild(row);
    });

    return listingsTable;
}


window.onload = updateListings;

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