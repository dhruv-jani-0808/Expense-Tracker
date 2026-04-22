# 💰 Flask Expense Tracker

A medium-level, full-stack web application built with Flask that allows users to manage their personal finances. Users can create an account, log their daily expenses, manage custom categories, and view their spending habits through interactive charts and monthly summaries.

## ✨ Features

* **User Authentication:** Secure registration, login, and logout functionality using `Flask-Login` and `Werkzeug` password hashing.
* **Dashboard & Analytics:** A central hub showing "Today's Total", "This Month's Total", recent transactions, and a dynamic pie chart of spending by category.
* **Expense Management (CRUD):** Users can add, edit, view, and delete their financial transactions.
* **Custom Categories:** Users can create and manage their own personalized spending categories (e.g., Groceries, Rent, Gaming).
* **Responsive UI:** Clean and mobile-friendly interface built with Bootstrap 5.
* **Data Visualization:** Interactive charts powered by Chart.js.

## 🛠️ Tech Stack

**Backend:**
* Python 3
* Flask (Web Framework)
* Flask-SQLAlchemy (ORM)
* Flask-Login (Session Management)
* SQLite (Database)

**Frontend:**
* HTML5 / Jinja2 Templating
* CSS3
* Bootstrap 5
* JavaScript & Chart.js

## 📂 Project Structure

```text
expense-tracker/
│
├── app.py                 # Application factory and main entry point
├── requirements.txt       # Python dependencies
│
├── database/              # SQLite database storage
│   └── database.db
│
├── models/                # SQLAlchemy database schemas
│   ├── user_model.py
│   ├── expense_model.py
│   └── category_model.py
│
├── routes/                # Flask Blueprints (Controllers)
│   ├── auth_routes.py
│   ├── dashboard_routes.py
│   ├── expense_routes.py
│   └── category_routes.py
│
├── static/                # Static assets
│   ├── css/style.css
│   └── js/charts.js
│
└── templates/             # HTML Jinja templates
    ├── base.html
    ├── auth/
    ├── dashboard/
    ├── expenses/
    └── categories/
```

🚀 How to Run Locally
Follow these steps to get the project running on your local machine.

1. Clone the repository
```Bash
git clone [https://github.com/your-username/expense-tracker.git](https://github.com/your-username/expense-tracker.git)
cd expense-tracker
```

2. Create a virtual environment
```Bash
# On Windows
python -m venv venv
venv\Scripts\activate
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```Bash
pip install -r requirements.txt
```

4. Create the database folder
Ensure there is an empty folder named database in the root directory. The SQLite database will be generated here automatically.

```Bash
mkdir database
```

5. Run the application
```Bash
python app.py
```
The server will start. Open your web browser and go to http://127.0.0.1:5000.

🌱 Future Enhancements
[ ] Add functionality to export monthly expenses to a CSV file.

[ ] Implement a "Budget Limit" feature with alerts.

[ ] Add a dark mode toggle.

[ ] Include pagination for the "All Expenses" table.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
