
window.onload = showForm;


function signOut() {
    window.location.href = "index.html";
}

function trade() {
    saveUserId("trade.html");
}

function listings() {
    saveUserId("listings.html");
}

function transactions() {
    saveUserId("transactions.html");
}

function dashboard() {
    saveUserId("dashboard.html");
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


function showForm() {
    const formSelector = document.getElementById('form-selector');
    const selectedForm = formSelector.value;

    const formContainer = document.getElementById('account-content');
    formContainer.innerHTML = ''; 

    switch (selectedForm) {
        case 'update-username':
            formContainer.appendChild(createUpdateUsernameForm());
            break;
        case 'update-password':
            formContainer.appendChild(createUpdatePasswordForm());
            break;
        case 'delete-account':
            formContainer.appendChild(createDeleteAccountForm());
            break;
        case 'funds':
            formContainer.appendChild(createFundsForm());
            break;
        default:
            break;
    }
}

function createUpdateUsernameForm() {
    const form = document.createElement('form');
    form.id = 'account-form';

    form.innerHTML = `
        <h3>Update Username</h3>
        <label for="new-username">New Username:</label>
        <input type="text" id="new-username" name="new-username" required>
        <label for="current-username">Current Username:</label>
        <input type="text" id="current-username" name="current-username" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Update Username</button>
    `;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        updateUsername();
    });

    return form;
}

function createUpdatePasswordForm() {
    const form = document.createElement('form');
    form.id = 'account-form';

    form.innerHTML = `
        <h3>Update Password</h3>
        <label for="new-password">New Password:</label>
        <input type="password" id="new-password" name="new-password" required>
        <label for="current-username">Current Username:</label>
        <input type="text" id="current-username" name="current-username" required>
        <label for="current-password">Current Password:</label>
        <input type="password" id="current-password" name="current-password" required>
        <button type="submit">Update Password</button>
    `;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        updatePassword();
    });

    return form;
}

function createDeleteAccountForm() {
    const form = document.createElement('form');
    form.id = 'account-form';

    form.innerHTML = `
        <h3>Delete Account</h3>
        <label for="confirm-username">Confirm Username:</label>
        <input type="text" id="confirm-username" name="confirm-username" required>
        <label for="confirm-password">Confirm Password:</label>
        <input type="password" id="confirm-password" name="confirm-password" required>
        <button type="submit">Delete Account</button>
    `;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        deleteAccount();
    });

    return form;
}

function createFundsForm() {
    const form = document.createElement('form');
    form.id = 'account-form';

    form.innerHTML = `
        <h3>Deposit Withdraw Funds</h3>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" required>
        <label for="transaction-type">Transaction Type:</label>
        <select id="transaction-type" name="transaction-type" required>
            <option value="deposit">Deposit</option>
            <option value="withdraw">Withdraw</option>
        </select>
        <button type="submit">Submit</button>
    `;

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 
        funds(); 
    });

    return form;
}

function funds() {
    const amountInput = document.getElementById('amount');
    const transactionTypeSelect = document.getElementById('transaction-type');

    const amount = amountInput.value;
    const transactionType = transactionTypeSelect.value;

    if (isNaN(amount) || amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    const apiUrl = `http://127.0.0.1:8000/actions/${transactionType}`;
    const user_id = getUserId();

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_id: user_id,
            amount: parseFloat(amount),
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (transactionType === 'deposit') {
            alert(`Depositing ${amount} funds.\nResponse: ${JSON.stringify(data.message)}`);
        } else if (transactionType === 'withdraw') {
            alert(`Withdrawing ${amount} funds.\nResponse: ${JSON.stringify(data.message)}`);
        } else {
            alert(`Invalid transaction type.\nResponse: ${JSON.stringify(data.message)}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert(`Error during ${transactionType} transaction.`);
    });
}


async function deleteAccount() {
    const confirmUsernameInput = document.getElementById('confirm-username');
    const confirmPasswordInput = document.getElementById('confirm-password');

    const confirmUsername = confirmUsernameInput.value;
    const confirmPassword = confirmPasswordInput.value;

 
    try {
        const response = await fetch('http://127.0.0.1:8000/auth', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: confirmUsername,
                password: confirmPassword,
            }),
        });
        const data = await response.json();

        if (data.message === "User deleted successfully!"){
            alert("Account deleted succesfully!");
            signOut();
        } else {
            alert("Account deletion failed.\nCheck username and password!");
        }

    
    } catch (error) {
        console.error('Error:', error);
        alert('An unexpected error occurred.');
    }
}

async function updatePassword() {
    const newPasswordInput = document.getElementById('new-password');
    const currentUsernameInput = document.getElementById('current-username');
    const currentPasswordInput = document.getElementById('current-password');

    const newPassword = newPasswordInput.value;
    const currentUsername = currentUsernameInput.value;
    const currentPassword = currentPasswordInput.value;

    try {
        const response = await fetch('http://127.0.0.1:8000/actions/update/password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: currentUsername,
                password: currentPassword,
                new_password: newPassword,
            }),
        });

        const data = await response.json();

        if (data.message === "Password updated successfully!"){
            alert("Password updated successfully!");
            signOut();
        } else {
            alert("Invalid username and password!");
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An unexpected error occurred.');
    }
}

async function updateUsername() {
    const newUsernameInput = document.getElementById('new-username');
    const currentUsernameInput = document.getElementById('current-username');
    const passwordInput = document.getElementById('password');

    const newUsername = newUsernameInput.value;
    const currentUsername = currentUsernameInput.value;
    const password = passwordInput.value;


    try {
        const response = await fetch('http://127.0.0.1:8000/actions/update/username', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: currentUsername,
                password: password,
                new_username: newUsername,
            }),
        });

        const data = await response.json();

        if (data.message === "Username updated successfully!") {
            alert("Username updated successfully!");
            signOut();
        } else {
            alert("Invalid username and password!");
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An unexpected error occurred.');
    }
}