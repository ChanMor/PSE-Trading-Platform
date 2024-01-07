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

        const stockListings = document.getElementById('stockListings');

        // Clear existing content
        stockListings.innerHTML = '';

        // Iterate through the listings and populate the table
        listings.forEach(stock => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${stock.symbol}</td>
                <td>${stock.name}</td>
                <td>${stock.price}</td>
            `;
            stockListings.appendChild(row);
        });
    } catch (error) {
        console.error('Error updating listings:', error);
    } finally {
        // Hide loading screen
        document.getElementById('loading-screen').style.display = 'none';
    }
}

window.onload = updateListings;

function signOut() {
    window.location.href = "index.html";
}

function dashboard() {
    window.location.href = "dashboard.html";
}