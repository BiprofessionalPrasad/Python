# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:05:16 2023

@author: Prasad
"""

import pyodbc

# Database connection details
db_file = "C:/Access Database/People.accdb"  # Replace with actual database path
#username = "your_username"  # Replace with username if needed (optional)
#password = "your_password"  # Replace with password if needed (optional)

# Connect to the Access database
#conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}}?;DBQ={db_file};PWD={password}", auth=(username, password) if username else None)
conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}}?;DBQ={db_file};)
cursor = conn.cursor()

# Define table schema
employee_table = """
CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);
"""
department_table = """
CREATE TABLE IF NOT EXISTS Department (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
);
"""
salary_table = """
CREATE TABLE IF NOT EXISTS Salary (
    EmployeeID INTEGER,
    Salary DECIMAL(10, 2) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
"""

# Create tables if they don't exist
try:
    cursor.execute(employee_table)
    cursor.execute(department_table)
    cursor.execute(salary_table)
    conn.commit()
except Exception as e:
    print(f"Error creating tables: {e}")
    conn.rollback()

# Example functions for managing data (modify as needed)
def add_employee(employee_id, first_name, last_name, department_id):
    cursor.execute("""
        INSERT INTO Employee (EmployeeID, FirstName, LastName, DepartmentID)
        VALUES (?, ?, ?, ?)
    """, (employee_id, first_name, last_name, department_id))
    conn.commit()

def get_all_employees():
    cursor.execute("SELECT * FROM Employee")
    return cursor.fetchall()

# Close connection
conn.close()

# Example usage
add_employee(1, "John", "Doe", 1)

employees = get_all_employees()
for employee in employees:
    print(f"Employee ID: {employee[0]}, Name: {employee[1]} {employee[2]}")
