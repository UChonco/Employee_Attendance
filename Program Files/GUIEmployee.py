from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Employee:
    def __init__(self, employee_id, name, hourly_wage):
        self.employee_id = employee_id
        self.name = name
        self.hourly_wage = hourly_wage
        self.attendance = []

    def clock_in(self):
        clock_in_time = datetime.now()
        self.attendance.append({'clock_in': clock_in_time, 'clock_out': None})
        return f"{self.name} clocked in at {clock_in_time.strftime('%Y-%m-%d %H:%M:%S')}"

    def clock_out(self):
        clock_out_time = datetime.now()
        if self.attendance and self.attendance[-1]['clock_out'] is None:
            self.attendance[-1]['clock_out'] = clock_out_time
            return f"{self.name} clocked out at {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            return f"{self.name} has not clocked in or has already clocked out."

    def total_hours_worked(self):
        total_hour = 0
        for record in self.attendance:
            if record['clock_out']:
                hour_worked = (record['clock_out'] - record['clock_in']).total_seconds() / 3600
                total_hour += hour_worked
        return total_hour

    def calculate_payment(self):
        total_hour = self.total_hours_worked()
        payment = total_hour * self.hourly_wage
        return payment

    def report(self):
        total_hours = self.total_hours_worked()
        payment = self.calculate_payment()
        return f"{self.name} worked {total_hours:.2f} hours and will be paid R{payment:.2f}."


class EmployeeSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Attendance System")
        self.master.geometry("500x400")

        self.employees = {}

        # Title label
        self.title_label = Label(master, text="Employee Attendance System", font=("Arial", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        self.add_employee_button = Button(master, text="Add Employee", command=self.add_employee_gui, width=20)
        self.add_employee_button.grid(row=1, column=0, padx=10, pady=5)

        self.clock_in_button = Button(master, text="Clock In", command=self.clock_in_gui, width=20)
        self.clock_in_button.grid(row=2, column=0, padx=10, pady=5)

        self.clock_out_button = Button(master, text="Clock Out", command=self.clock_out_gui, width=20)
        self.clock_out_button.grid(row=3, column=0, padx=10, pady=5)

        self.generate_report_button = Button(master, text="Generate Daily Report", command=self.generate_report, width=20)
        self.generate_report_button.grid(row=4, column=0, padx=10, pady=5)
        
        self.help_btn = Button(master,text="Help",width=20,command=self.help_info).grid(row=5,column=0)

    def add_employee(self, employee_id, name, hourly_wage=50):
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(employee_id, name, hourly_wage)
            messagebox.showinfo("Success", f"Employee {name} (ID: {employee_id}) added successfully!")
        else:
            messagebox.showerror("Error", "Employee ID already exists.")

    def clock_in(self, employee_id):
        if employee_id in self.employees:
            result = self.employees[employee_id].clock_in()
            messagebox.showinfo("Clock In", result)
        else:
            messagebox.showerror("Error", "Employee ID not found.")

    def clock_out(self, employee_id):
        if employee_id in self.employees:
            result = self.employees[employee_id].clock_out()
            messagebox.showinfo("Clock Out", result)
        else:
            messagebox.showerror("Error", "Employee ID not found.")

    def generate_report(self):
        report_text = "\n".join([emp.report() for emp in self.employees.values()])
        messagebox.showinfo("Daily Report", report_text)

    def add_employee_gui(self):
        add_window = Toplevel(self.master)
        add_window.title("Add Employee")

        Label(add_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
        employee_id_entry = Entry(add_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(add_window, text="Employee Name:").grid(row=1, column=0, padx=10, pady=5)
        name_entry = Entry(add_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        def submit_employee():
            employee_id = employee_id_entry.get()
            name = name_entry.get()
            self.add_employee(employee_id, name)
            add_window.destroy()

        submit_button = Button(add_window, text="Add", command=submit_employee)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def clock_in_gui(self):
        clock_in_window = Toplevel(self.master)
        clock_in_window.title("Clock In")

        Label(clock_in_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
        employee_id_entry = Entry(clock_in_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit_clock_in():
            employee_id = employee_id_entry.get()
            self.clock_in(employee_id)
            clock_in_window.destroy()

        submit_button = Button(clock_in_window, text="Clock In", command=submit_clock_in)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def clock_out_gui(self):
        clock_out_window = Toplevel(self.master)
        clock_out_window.title("Clock Out")

        Label(clock_out_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
        employee_id_entry = Entry(clock_out_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit_clock_out():
            employee_id = employee_id_entry.get()
            self.clock_out(employee_id)
            clock_out_window.destroy()

        submit_button = Button(clock_out_window, text="Clock Out", command=submit_clock_out)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)
    def help_info(self):
        helpInfo = Toplevel(self.master)
        mylbl=Label(helpInfo,text="""How to Use the program \n \n 1. Run the program on the terminal \n \n 2. Menu Options(The program will display the Menu):\n \n 1  Employee \n \n 2.Clock In \n \n 3.Clock Out \n \n 4.Generate Report \n \n
        1 Add Employee:\n
        Choose 1 to add new employee.\n The Employee enter The Employee Id and Name and the program will print Successful\n
   
        2. Clock In:\n
            Choose 2 to clock-In. \n Employee Enter his/Her employee Id to clockin and program will print employee name , Id and Date,time clocked-in.\n

        3. Clock-Out:\n
            Choose 3 to clock-Out. \n Employee Id to clock-out and program will print employee name , Id and Date,time clocked-out.\n

        4. Generate Report\n
            choose 4 to generate report.\n Once employe has clock-in and clock-out they can generate a daily report, the program will print the Employee ID, Employee Name, ID and Date,Time clock-in and clock-out, hours worked and payment on the reports""")
        mylbl.grid(row=0,column=0)
        


def main():
    root = Tk()
    app = EmployeeSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
