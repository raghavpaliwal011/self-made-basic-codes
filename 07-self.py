class employee:
    def my_sal(self):
        return f"the salary of this employee named {self.name} is {self.sal}"
raghav = employee()
raghav.name = "raghav"
raghav.sal = 100000000000000000000000000
print (raghav.my_sal())