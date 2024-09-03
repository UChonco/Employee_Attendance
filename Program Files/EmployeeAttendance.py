#importing datetime, will be used to get the date and time from the computer 
from datetime import datetime

#Initailizing my Employee Class
class Employee:
    def __init__(self,employee_id,name,hourly_wage):
        self.employee_id =employee_id
        self.name = name
        self.hourly_wage = hourly_wage
        self.attendance =[]
   
    #Clock-in function    
    def clock_in(self):
        clock_in_time = datetime.now() # Get clock-in time from the compter
        self.attendance.append({'clock_in': clock_in_time, 'clock_out': None})
        print(f"{self.name} (ID :{self.employee_id}) clocked in at {clock_in_time.strftime('%Y-%m-%d %H:%M:%S')}")
   
    #Clock-Out function
    def clock_out(self):
        clock_out_time = datetime.now()
        if self.attendance and self.attendance[-1]['clock_out'] is None:
            self.attendance[-1]['clock_out'] = clock_out_time
            print(f"{self.name} (ID :{self.employee_id}) clocked out at {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
         print(f"{self.name} (ID :{self.employee_id}) have not clocked in or has already clocked out")
    
    #Calculate hours worked
    def total_hours_worked(self):
        total_hour = 0
        for record in self.attendance:
            if record['clock_out']:
                hour_worked = (record['clock_out'] - record['clock_in']).total_seconds() / 3600 
                total_hour += hour_worked
            return total_hour
        
    #calculate payment
    def calculate_payment(self):
        total_hour = self.total_hours_worked()
        payment = total_hour * self.hourly_wage
        return payment 
    
    def test_calculatepayment(total_hour,hourly_wage):
        return total_hour * hourly_wage
     #Display Report
    def report(self):
        
        total_hours = self.total_hours_worked()
        payment = self.calculate_payment()
        print(f"{self.name} (ID: {self.employee_id} worked {total_hours:.2f} hours today and will be paid R{payment:.2f}.)")
#___________________________________________________________________________________________________________________________________________ 
class Employe_System:
    def __init__(self):
        self.employees = {}
    #adding employee id and name to employee
    def add_employee(self):
        employee_id = input("Enter Employee ID : ")
        name = input("Enter Employee name: ")
        hourly_wage  = 50 
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(employee_id,name,hourly_wage)
            print(f'Employee {name} (ID: {employee_id} added successfully)')
        else:
            print(f"Employee ID {employee_id} already exists. ")

    def employee_clock_in(self):
        employee_id = input("Enter Employee Id: ")
        if employee_id in self.employees:
            self.employees[employee_id].clock_in()
        else:
            print(f"Employee Id {employee_id} not found")

    def employee_clock_out(self):
        employee_id = input("Enter Employee Id: ")
        if employee_id in self.employees:
            self.employees[employee_id].clock_out()
        else:
            print(f"Employee Id {employee_id} not found")

    def generate_report(self):
        print("\n Daily Report")
        print("_" * 40)
        for employee in self.employees.values():
            employee.report()
        print("_" * 40)

def main():
    system =Employe_System()
    
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Clock In")
        print("3. Clock Out")
        print("4. Generate Daily Reports")
        print("5. Exit")

        options = input("Enter your options: ")

        if options == "1":
            system.add_employee()

        elif options == "2":
            system.employee_clock_in()
        elif options == "3":
            system.employee_clock_out()
        elif options == "4":
            system.generate_report()
        elif options == "5":
            print("Program Closed")
            break
        else:
            print("invalid input")

# this line of code is used to check if the right python file/function is the only one running 
if __name__ == "__main__":
    main()


        
    





        
