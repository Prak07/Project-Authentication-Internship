# Django Authentication System

This Django-based Authentication System provides a secure and user-friendly interface for user management and access control. The project leverages Django's built-in authentication framework and extends its functionality with additional features like password recovery and profile management.

## Features

### Authentication and Authorization
- **Login**: Users can log in securely using their credentials.
- **Signup**: New users can register and create an account.
- **Logout**: Users can securely log out of the application.

### Password Management
- **Change Password**: Logged-in users can update their password securely.
- **Forgot Password**: Users who forget their password can request a reset link. The link is sent to their registered Gmail and is valid for one-time use only, ensuring enhanced security.

### User Dashboard
- **Dashboard**: Authenticated users can access a personalized dashboard displaying relevant information.

### Profile Management
- **Profile Update**: Users can view and edit their profile details from the dashboard.

## Technologies Used

- **Backend**: Django (leveraging built-in authentication and forms)
- **Frontend**: HTML, CSS, JavaScript for a user-friendly interface
- **Email Integration**: Gmail SMTP for sending password reset links

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/authentication-system.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd authentication-system
   ```

3. **Set up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up Environment Variables**:
   - Configure Gmail SMTP credentials for sending password reset emails.
   - Add `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your environment.

6. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open `http://127.0.0.1:8000` in your browser.

## Usage

1. **Signup**: Create a new account by providing an email and password.
2. **Login**: Log in using your registered email and password.
3. **Dashboard**: Access the user dashboard to manage your account.
4. **Profile**: Update profile details like name and email.
5. **Change Password**: Update your password from the dashboard.
6. **Forgot Password**: Request a password reset link if you forget your password. Use the link sent to your email to set a new password.

## Security Measures

- **One-Time Password Reset Links**: Reset links are valid for a single use only.
- **Encrypted Password Storage**: Uses Django's secure password hashing mechanism.
- **Session Management**: Ensures secure user sessions and logout functionality.

## Contributions

This project was developed solely by **Prakhar Agarwal**, implementing core authentication features, password recovery, and user management functionalities.

