class ceo():
    def __init__(self,name,work,company,salary):
        self.name = name
        self.work = work 
        self.company = company
        self.salary = salary 

    def print_details(self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

class manager():
    def __init__(self,name,work,company,salary):
        self.name = name
        self.work = work 
        self.company = company
        self.salary = salary 

    def details(self):
        print (f"the name of this person is {self.name}, she is {self.work} of {self.company} and her salary is {self.salary}")

class employee(ceo,manager):
    def teller(self):
        print (f"the name of this person is {self.name}, he is {self.work} of {self.company} and his salary is {self.salary}")

    
raghav = ceo("raghav","ceo","rockstar games",2000000000)
raghav.print_details()
deepti = manager("deepti","manager","rockstar games",200000)
deepti.details()
suuu = employee("suuuu","employee","rockstar games",100000)
suuu.teller()