
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