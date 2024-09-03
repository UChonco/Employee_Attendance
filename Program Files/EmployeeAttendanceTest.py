import unittest,EmployeeAttendance
from EmployeeAttendance import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee(employee_id="001", name="Unathi chonco", hourly_wage=50)

    def test_clock_in(self):
        self.employee.clock_in()
        self.assertEqual(len(self.employee.attendance), 1)
        self.assertIsNotNone(self.employee.attendance[-1]['clock_in'])
        self.assertIsNone(self.employee.attendance[-1]['clock_out'])

    def test_clock_out(self):
        self.employee.clock_in()
        self.employee.clock_out()
        self.assertIsNotNone(self.employee.attendance[-1]['clock_out'])
    
    def test_calcyulate_payment(self):
        self.assertEqual(EmployeeAttendance.Employee.test_calculatepayment(2,4),8)
        self.assertTrue(EmployeeAttendance.Employee.test_calculatepayment(2,4) == 8)


if __name__ == '__main__':
    unittest.main()
