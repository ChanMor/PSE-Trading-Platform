
function toggleButtonText() {
    const button = document.getElementById("signinButton");
    const h2 = document.getElementById("signinText");
    button.textContent = (button.textContent === "Sign In") ? "Register" : "Sign In";
    h2.textContent = button.textContent;
}

async function auth() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const button = document.getElementById("signinButton");
    const apiUrl = (button.textContent === "Sign In") ? "http://127.0.0.1:8000/auth/login" : "http://127.0.0.1:8000/auth";

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Access-Control-Allow-Methods", "POST");
    myHeaders.append("Access-Control-Allow-Origin", true);

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ username, password }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        if (data.message === "User created successfully!" || data.message === "User login successfully!") {
            saveUserIdToLocalStorage(username);
            //window.location.href = "dashboard.html";
        } else {
            console.error("Authentication failed:", data.message);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}



async function saveUserIdToLocalStorage(username) {
    var userIdApiUrl = `http://127.0.0.1:8000/users/${username}/user_id`;
    var response = await fetch(userIdApiUrl);
    var data = await response.json();
    var userId = data.user_id;


    // Assuming you fetched data from the API and stored it in a variable named 'apiData'
    const apiData = { key: userId };

    // Convert data to a query string
    const queryString = `?data=${encodeURIComponent(JSON.stringify(apiData))}`;

    // Redirect to the second HTML page with the query string
    window.location.href = `dashboard.html${queryString}`;

}






