import sqlite3 as sqlite
import random
import os

def initialize_tables():
    con = sqlite.connect('database.db')
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Employees")
    cur.execute("DROP TABLE IF EXISTS Careers")
    cur.execute("DROP TABLE IF EXISTS EmployeeBosses")

    cur.execute('''CREATE TABLE Employees (
        EmployeeID integer PRIMARY KEY,
        FirstName text,
        LastName text
    )''')
    cur.execute('''CREATE TABLE Careers (
        EmployeeID integer,
        CareerID integer,
        Field text,
        Salary real,
        PRIMARY KEY(EmployeeID, CareerID),
        FOREiGN KEY(EmployeeID) REFERENCES Employees
    )
    ''')
    cur.execute('''CREATE TABLE EmployeeBosses (
        EmployeeID integer PRIMARY KEY,
        BossFirstName text,
        BossLastName text
    )
    ''')
    con.commit()
    con.close()

def testDatabase():
    initialize_tables()
    employeeIds = range(8)
    careerIds = employeeIds[::-1]
    firstNames = ['Harry', 'John', 'Rachel', 'Ross', 'John', 'Jonathan', 'Sherlock', 'John']
    lastNames  = ['Truman', 'Doe', 'Green', 'Geller', 'Cena', 'Joestar', 'Holmes', 'Watson']
    fieldsTypes = ['Engineering', 'Sales', 'HR',  'IT', 'Sales', 'IT', 'HR', 'Investments']
    salaries = ['17.10', '20.50', '50.00', '49.99', '100.01', '2.00', '19.50', '39.00']

    bossEmployeeIds = range(4, 12)
    bossFirstNames = ['Cant C.', 'Will', 'Inspector', 'Sherlock', 'Oski', 'John', 'Richard', 'George']
    bossLastNames = ['Mei', 'Zeppeli', 'Lestrade', 'Holmes', 'Bear', 'Hammond', 'Feynman', 'Lucas']

    con = sqlite.connect('database.db')
    cur = con.cursor()

    employees = [
        (employeeIds[i], 
        firstNames[i], 
        lastNames[i]) 
    for i in range(len(employeeIds))]
    careers = [
        (employeeIds[i], 
        careerIds[i], 
        fieldsTypes[i], 
        salaries[i]) 
    for i in range(len(employeeIds))]
    bosses = [
        (bossEmployeeIds[i],
        bossFirstNames[i],
        bossLastNames[i])
    for i in range(len(bossEmployeeIds))]

    cur.executemany('INSERT INTO Employees VALUES (?, ?, ?)', employees)
    cur.executemany('INSERT INTO Careers VALUES (?, ?, ?, ?)', careers)
    cur.executemany('INSERT INTO EmployeeBosses VALUES (?, ?, ?)', bosses)

    con.commit()
    con.close()