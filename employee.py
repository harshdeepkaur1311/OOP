class Employee:

    __nbr_of_employees = 0
    def __init__(self, name = '', hours_worked = 0, rate_of_pay = 0):
        self.__name = name
        self.__hours_worked = hours_worked
        self.__rate_of_pay = rate_of_pay
        Employee.__nbr_of_employees += 1
    
    def set_name(self, name):
        self.__name = name

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def set_rate_of_pay(self, rate_of_pay):
        self.__rate_of_pay = rate_of_pay
    
    def get_name(self):
        return self.__name
    
    def get_hours_worked(self):
        return self.__hours_worked
    
    def get_rate_of_pay(self):
        return self.__rate_of_pay
    
    def calc_gross_pay(self):
        return self.__hours_worked * self.__rate_of_pay
    
    def add_hours_worked(self, hours):
        self.__hours_worked += hours
    
    def __str__(self):
        format_str = f'Name:{self.__name}\n'
        format_str += f'Hours: {self.__hours_worked}\n'
        format_str += f'Rate:${self.__rate_of_pay}\n'
        format_str += f'Gross Pay: ${self.calc_gross_pay()}\n'
        return format_str
    
    def get_number_of_employees():
        return Employee.__nbr_of_employees
    



def main():
    emp1 = Employee()
    # print(emp1)
    # print()

if __name__ == "__main__":
    main()