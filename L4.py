#Template loaders - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader

from jinja2 import Environment, FileSystemLoader, FunctionLoader

"""
PackageLoader – для завантаження шаблонів із пакета;
DictLoader – для завантаження шаблонів із словника;
FunctionLoader – для завантаження з урахуванням функції;
PrefixLoader – завантажувач, який використовує словник для побудови підкаталогів;
ChoiceLoader - завантажувач, що містить список інших завантажувачів (якщо один не спрацює, вибирається наступний);
ModuleLoader – завантажувач для скомпільованих шаблонів.
"""
#Environment& FileSystemLoader
def temp_1():
    persons = [
        {"name": "Yaroslav", "old": 22, "weight": 78.5},
        {"name": "Olegsandr", "old": 28, "weight": 82.3},
        {"name": "Henrich", "old": 33, "weight": 94.0}
    ]

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('main.htm')
    msg = tm.render(users=persons)
    return msg


#Функція яка повертатиме шаблон
def loadTpl(path):
    if path == "index":
        return '''Name {{u.name}}, old {{u.old}}'''
    else:
        return '''Data: {{u}}'''

#Load with def
def temp_2():
    persons = [
        {"name": "Yaroslav", "old": 22, "weight": 78.5},
        {"name": "Olegsandr", "old": 28, "weight": 82.3},
        {"name": "Henrich", "old": 33, "weight": 94.0}
    ]
    file_loader = FunctionLoader(loadTpl)
    env = Environment(loader=file_loader)

    tm = env.get_template('index')
    msg = tm.render(u=persons[0])
    return msg


# =====================================================================================
#Environment& FileSystemLoader
print("Example_1: ", temp_1())

#Load with def
print("Example_2: ", temp_2())

