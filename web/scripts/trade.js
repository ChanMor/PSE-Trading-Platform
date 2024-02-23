
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

function getStockPrice() {
    const stockCode = document.getElementById('stock-code').value;

    if (stockCode.trim() === '') {
        alert("Invalid stock code!");
        return;
    }

    fetch(`http://127.0.0.1:8000/stocks/price/${stockCode}`)
        .then(response => {

            if (!response.ok) {
                throw new Error(`Failed to fetch stock price. Status: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {

            if (data.price === null){
                alert("Invalid stock code!")
                return
            }
            
            document.getElementById('stock-price').innerText = `Price: ${data.price}`;
        })
        .catch(error => {
            console.error('Error fetching stock price:', error);
        });
}


function performTransaction() {
    const stockCode = document.getElementById('stock-code').value;

    if (stockCode.trim() === '') {
        alert("Invalid stock code!");
        return;
    }

    const transactionType = document.getElementById('transaction-type').value;
    const quantity = document.getElementById('quantity').value;

    if (quantity.trim() === '') {
        alert("Invalid shares!");
        return;
    }

    const transactionApiUrl = `http://127.0.0.1:8000/actions/${transactionType}`;
    const user_id = getUserId();

    const requestData = {
        user_id: user_id,
        stock_symbol: stockCode,
        shares: parseInt(quantity),
    };

    fetch(transactionApiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
        const alertMessage = data.message;
        if (alertMessage === `Successfully bought ${parseInt(quantity)} shares of ${stockCode}!`){
            alert(alertMessage);

        } else if (alertMessage === `Successfully sold ${parseInt(quantity)} shares of ${stockCode}!`){
            alert(alertMessage);
        } else {
            alert(alertMessage);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Transaction Failed");
    });
}
