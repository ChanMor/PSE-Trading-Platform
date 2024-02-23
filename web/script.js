
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
            saveUserId(username);
        } else {
            console.error("Authentication failed:", data.message);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}



async function saveUserId(username) {
    var userIdApiUrl = `http://127.0.0.1:8000/users/${username}/user_id`;
    var response = await fetch(userIdApiUrl);
    var data = await response.json();
    var userId = data.user_id;


    const apiData = { key: userId };
    const queryString = `?data=${encodeURIComponent(JSON.stringify(apiData))}`;

    window.location.href = `pages/dashboard.html${queryString}`;
}






