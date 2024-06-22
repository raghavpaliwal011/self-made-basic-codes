class ceo():
    def __init__(self,name,work,company,salary):
        self.name = name
        self.work = work
        self.company = company
        self.salary = salary

    def print_details(self):
        print (f"the name of this person is {self.name} he is {self.work} of {self.company} his salary is {self.salary}")
class manager (ceo):
    def details(self):
        print (f"the name of this person is {self.name} he is {self.work} of {self.company} his salary is {self.salary}")

raghav = ceo("raghav","ceo","rockstar games",20000000000000)
raghav.print_details()
deepti = manager ("deepti","manager","rockstar games",1000000000000)
deepti.details()