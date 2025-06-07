# Think Share 💭

A modern Django web application where users can share their thoughts and ideas with the community. Think Share provides a clean, intuitive platform for creating, managing, and discovering content with full user authentication and personalization features.

## ✨ Features

### Core Functionality
- **Post Management**: Create, read, update, and delete posts (Full CRUD operations)
- **User Authentication**: Secure user registration and login system
- **Responsive Design**: Works seamlessly across desktop and mobile devices

### User Experience
- **Theme Toggle**: Switch between light and dark modes for comfortable viewing
- **Post Discovery**: Browse and explore posts from other users
- **Secure Access**: Protected routes and user-specific content management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/think-share.git
   cd think-share
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## 📱 Usage

### Getting Started
1. **Register**: Create a new account or login with existing credentials
2. **Create Posts**: Share your thoughts by creating new posts
3. **Manage Content**: Edit or delete your posts
4. **Explore**: Browse posts from other users in the community
5. **Customize**: Toggle between light and dark themes for your preferred viewing experience

### User Authentication
- **Registration**: New users can create accounts with email verification
- **Login/Logout**: Secure session management for authenticated users
- **Protected Routes**: Certain features require user authentication

## 🛠️ Technology Stack

- **Backend**: Django 
- **Database**: SQLite (default) / PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in authentication system
- **Styling**: CSS with theme switching capabilities
