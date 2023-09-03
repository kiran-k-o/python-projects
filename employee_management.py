import mysql.connector
# mydb =  mysql.connector.connect(host='localhost',user='root',password='Python@007',port=3306)
# my_curser=mydb.cursor()
# # my_curser.execute("create database employee_management")
# my_curser.execute("use employee_management")



class HR:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Python@007",
            database="employee_management_system"
        )
        self.cursor = self.connection.cursor()

    def add_employee(self, employee):
        query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
        values = (employee.name, employee.position, employee.salary)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Employee added successfully!")

    def view_employee_details(self, employee_id):
        query = "SELECT * FROM employees WHERE id = %s"
        self.cursor.execute(query, (employee_id,))
        employee = self.cursor.fetchone()
        if employee:
            print("Employee Details:")
            print("ID:", employee[0])
            print("Name:", employee[1])
            print("Position:", employee[2])
            print("Salary:", employee[3])
        else:
            print("Employee not found!")

    def update_employee_salary(self, employee_id, new_salary):
        query = "UPDATE employees SET salary = %s WHERE id = %s"
        self.cursor.execute(query, (new_salary, employee_id))
        self.connection.commit()
        print("Employee salary updated successfully!")

    def close(self):
        self.connection.close()


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


def main():
    hr = HR()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee Details")
        print("3. Update Employee Salary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, position, salary)
            hr.add_employee(employee)

        elif choice == "2":
            employee_id = int(input("Enter employee ID: "))
            hr.view_employee_details(employee_id)

        elif choice == "3":
            employee_id = int(input("Enter employee ID: "))
            new_salary = float(input("Enter new salary: "))
            hr.update_employee_salary(employee_id, new_salary)

        elif choice == "4":
            hr.close()
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
