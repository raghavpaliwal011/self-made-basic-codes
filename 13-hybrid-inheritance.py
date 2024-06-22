class ceo():
    def __init__(self,name,work,company,salary):
        self.name = name
        self.work = work
        self.company = company
        self.salary = salary

    def print_details(self):
        print(f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class boss(ceo):
    def details(self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class manager(ceo):
    def tails(self):
        print (f"the name of this  person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class employee(boss,manager):
    def teller(self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")
raghav = ceo("raghav","ceo","rockstar games",100000000)
raghav.print_details()
ramesh = boss("ramesh","boss","rockstar games",1000000)
ramesh.details()
suresh = manager("suresh","manager","rockstar games",10000)
suresh.tails()
manthan = employee("manthan","employee","rockstar games",10000)
manthan.teller()