class ceo():
    def __init__(self,name,work,company,salary):
        self.name = name
        self.work = work
        self.company = company
        self.salary = salary

    def print_details(self):
        print(f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class manager(ceo):
    def details(self):
        print (f"the name of this person is  {self.name},he is {self.work} of {self.company} and his salary is {self.salary}")

class employee(manager):
    def teller (self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")
raghav = ceo("raghav","ceo","rockstar games",30000000)
raghav.print_details()         
ramesh = manager("ramesh","manager","rockstar games",10000000)
ramesh.details()
suresh = employee("suresh","employee","rockstar games",3000000)
suresh.teller()