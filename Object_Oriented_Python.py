#THIS IS OBJECT ORIENTED PYTHON CLASS
##Running this code and reading every line of it understading of it will help you to build basics of Object oriented Python

class Employee:
    num_of_emps=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

        Employee.num_of_emps+=1


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None

    def apply_raise(self):
        self.pay=int(self.pay+self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str('-')
        return cls(first,last,pay)
    ##===============================================================
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
    ##===special methods=============================================


    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname,self.email)

    def __add__(self, other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):
    raise_amt=1.06
    def __init__(self,first,last,pay,prog_lang):
        Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employess=None):
        Employee.__init__(self,first,last,pay)
        if employess is None:
            self.employess=[]
        else:
            self.employess=employess

    def add_emp(self,emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self,emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employess:
            print('==>',emp.fullname)






emp_1=Employee('emp1','schafer',1000)
emp_2=Employee('emp2','Emp-2',2000)
emp_3=Developer('developer1','emp-3',3000,'Python')
emp_4=Manager('manager1','emp-4',5000,[emp_1,emp_2])
emp_5=Manager('manager2','emp-5',1000000,[emp_1,emp_2,emp_4,emp_3])
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
emp_2.apply_raise()
print('----------')
print(Employee.raise_amt)
print(emp_1.pay)
print(emp_2.pay)
emp_1.set_raise_amt(10000)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
Developer.set_raise_amt(100)
print(emp_4.print_emps())
print(emp_5.print_emps())

print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())
print(str(emp_1))
print(emp_1.__str__())

print(emp_1+emp_2)
print(len(emp_1))
print(emp_1.fullname)
emp_1.fullname='Corey Johnson'
del emp_1.fullname
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.first)