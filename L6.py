#Extends Template

from jinja2 import Environment, FileSystemLoader, FunctionLoader

#Extends Template
def temp_1():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about.htm')

    output = template.render()
    return output

#Nested blocks
def temp_2():
    num = ["AAA", "BBB", "CCC"]
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_1.htm')

    output = template.render(list_table = num)
    return output


# =====================================================================================
#Extends Template
print("Example_1: ", temp_1() + "\n")

#Extends Template
print("Example_2: ", temp_2())


