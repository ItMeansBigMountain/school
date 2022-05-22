class Employee():
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@oyamaproductions.com'

    def full_name(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Affan', 'Fareed', 100000)
emp_2 = Employee('Test', 'User', 10)


print(emp_1.full_name())
print(emp_2.full_name())
