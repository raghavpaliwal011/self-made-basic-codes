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
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class employee(ceo):
    def teller(self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class person(boss):
    def tels(self):
        print(f"this is the boss of suresh and manthan and his name is {self.name}")
raghav = ceo("raghav","ceo","rockstar games",1000000000)
raghav.print_details()
ramesh = boss("ramesh","boss","rockstar games",10000000)
ramesh.details()
suresh = manager("suresh","manager","rockstar games",100000)
suresh.tails()
manthan = employee("manthan","employee","rockstar games",10000000)
manthan.teller()
rams = person("ramesh","person","rockstar games",10000000)
rams.tels()