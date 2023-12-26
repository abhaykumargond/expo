<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Member Registration - HEAL-HUB Medicine Donation System</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        header {
            background-color: #336699;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 24px;
        }

        form {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }

        label {
            display: block;
            margin: 10px 0;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #336699;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #255580;
        }

        footer {
            margin-top: 20px;
            color: #888;
        }
    </style>
</head>

<body>
    <header>
        <h1>HEAL-HUB Member Registration</h1>
    </header>

    <form action="member-dashboard.html" method="post">
        <!-- Member registration form fields -->
        <label for="memberName">Member Name:</label>
        <input type="text" id="memberName" name="memberName" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" name="confirmPassword" required>

        <button type="submit">Register</button>
    </form>

    <footer>
        <p>&copy; 2023 HEAL-HUB Medicine Donation System</p>
    </footer>
</body>

</html>
