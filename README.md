# Expense Management System

An interactive expense tracking system built with **Streamlit** for the frontend and **FastAPI** for the backend. This tool allows users to:

- 📝 Add and update daily expenses by category  
- 📊 View detailed analytics by expense category  
- 📆 Analyze monthly expense trends 

## 🛠 Features  
- User-friendly web interface built with Streamlit  
- REST API backend powered by FastAPI  
- Track expenses by categories like Rent, Food, Shopping, Entertainment, and Others  
- Visualize expense breakdown by category and by month  
- Easily extendable and customizable
- Implemented structured logging for easier debugging and monitoring
- Included unit tests for backend to ensure reliability 
- Can be run fully locally on your machine

## 🚀 How to Run Locally  
### Prerequisites:  
- Python 3.7+
- MySQL 8.0+

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaibhavgarg2004/Expense-Tracking-System.git
   cd expense-management-system
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Set up the MySQL database**
 
   - **Import the schema and sample data:**

     Open **MySQL Workbench**, connect to your MySQL server, and use the following steps to import the database schema:

      1. Go to **File > Open SQL Script**.
      2. Navigate to the SQL file located at `database/expense_db_creation.sql` in the project folder.
      3. Open the file, then click the **Execute** button (⚡) to run the script and create the database with sample data.

   - **Update your MySQL credentials**:  
     Open the file `backend/db_helper.py` and update the following variables with your MySQL username and password:
     
     ```python
     user = "your_mysql_username"
     password = "your_mysql_password"
     ```
4. **Run the FastAPI server**:   
   ```commandline
    uvicorn backend.server:app --reload
   ```
5. **Run the Streamlit app**:   
   ```commandline
    streamlit run frontend/app.py
   ```

## 📂 Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **database/**: Contains the SQLite database file for the application.
- **tests/**: Contains the test cases for backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## 🖼️ Project Snapshots

Here are some screenshots of the application in action:

### 🔹 Add/Update Expenses Tab
![Add/Update](Add-Update-Tab.png)

### 🔹 Analytics by Category
![Category Analytics](Analytics-By-Category-Tab.png)

### 🔹 Analytics by Month
![Monthly Analytics](Analytics-By-Month-Tab.png)

---
Built with ❤️ using Streamlit and FastAPI

