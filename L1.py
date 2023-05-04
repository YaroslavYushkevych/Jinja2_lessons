from jinja2 import Template

def temp_1(name = "Yaroslav", age = 22):
    tm = Template("I`m {{ a }} old & my name {{ n }}.")
    return tm.render(n = name, a = age)

def temp_2(name = "Yaroslav", age = 22):
    tm = Template("I`m {{ a*2 }} old & my name {{ n.upper() }}.")
    return tm.render(n = name, a = age)

def temp_6():
    per_dict = {'name': 'Yaroslav', 'age': 22}
    tm = Template("I`m {{pd.age}} old & my name {{pd.name}}.")
    return tm.render(pd = per_dict)

def temp_7():
    per_dict = {'name': 'Yaroslav', 'age': 22}
    tm = Template("I`m {{pd['age']}} old & my name {{pd['name']}}.")
    return tm.render(pd = per_dict)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def temp_3(self):
        tm = Template("I`m {{ a }} old & my name {{ n }}.")
        return tm.render(n = self.name, a = self.age)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


#Standart temp - like f-strings
print("Temp_1: ", temp_1())

#Temp & somthing operations method
print("Temp_2: ", temp_2())

#Temp & class method
per = Person("Yaroslav", 22)
print("Temp_3: ", per.temp_3())

#OR other Temp & class method
tm = Template("I`m {{ p.age }} old & my name {{ p.name }}.")
msg = tm.render(p=per)
print("Temp_4: ", msg)

#Use getters & setters class method
tm = Template("I`m {{p.getAge()}} old & my name {{ p.getName() }}.")
msg = tm.render(p=per)
print("Temp_5: ", msg)

#Use dictionary for temp version 1
print("Temp_6: ", temp_6())

#Use dictionary for temp version 2
print("Temp_7: ", temp_7())