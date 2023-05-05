# Escaping and raw, for, if blocks

from jinja2 import Template


# from jinja2 import Template, escape

# NO Escaping(екранування)
def temp_1(name="Yaroslav"):
    data = '''Модуль Jinja замість визначення {{ name }} підставляє відповідне значення'''
    tm = Template(data)
    return tm.render(name='Yaroslav')


# Escaping {% raw %} … {% endraw %} (екранування)
def temp_2(name="Yaroslav"):
    data = '''{% raw %}Модуль Jinja замість визначення {{ name }} підставляє відповідне значення {% endraw %}'''
    tm = Template(data)
    return tm.render(name='Yaroslav')


# NO Escaping symbols(екранування символів)
def temp_3_0():
    link = '''In HTML-documents links are defined like this: 
    <a href="#">Link</a>'''

    tm = Template("{{ link }}")
    return tm.render(link=link)


# Escaping symbols(екранування символів)
def temp_3_1():
    link = '''In HTML-documents links are defined like this: 
    <a href="#">Link</a>'''
    # add | e
    tm = Template("{{ link | e }}")
    return tm.render(link=link)


# Escaping symbols of class (екранування символів за допомогою класу)
# Не працює на нових версіях
def temp_3_2():
    link = '''In HTML-documents links are defined like this: 
        <a href="#">Link</a>'''
    # return escape(link)
    return 0


# Use FOR
def temp_4():
    cities = [{'id': 1, 'city': 'Odesa'},
              {'id': 5, 'city': 'Lviv'},
              {'id': 7, 'city': 'Kyiv'},
              {'id': 8, 'city': 'Dnipro'},
              {'id': 11, 'city': 'Kharkiv'}]

    # symbol "-" in this code it`s like "delete \n"
    link = '''<select name="cities">
    {% for c in cities -%}
        <option value="{{c['id']}}">{{c['city']}}</option>
    {% endfor -%}
    </select>'''

    tm = Template(link)
    return tm.render(cities=cities)


# Use IF
def temp_5():
    cities = [{'id': 1, 'city': 'Odesa'},
              {'id': 5, 'city': 'Lviv'},
              {'id': 7, 'city': 'Kyiv'},
              {'id': 8, 'city': 'Dnipro'},
              {'id': 11, 'city': 'Kharkiv'}]

    # symbol "-" in this code it`s like "delete \n"
    # if id city > 5, we will print it
    link = '''<select name="cities">
    {% for c in cities -%}
    {% if c.id > 5 -%}
        <option value="{{c['id']}}">{{c['city']}}</option> #if
    {%elif c.city == "Odesa" -%}
        <option>{{c['city']}}</option> #elif
    {%else -%}
        {{c['city']}} #else
    {% endif -%}
    {% endfor -%}
    </select>'''

    tm = Template(link)
    return tm.render(cities=cities)


# =====================================================================================
# NO Escaping(екранування)
print("Example_1: ", temp_1())

# Escaping {% raw %} … {% endraw %} (екранування)
print("Example_2: ", temp_2())

"""
Для того що б вивести певну інформацію так як вона записана, а не так як її прочитає, наприклад, веб-сайт
потрібно екранувати символи. Можна зробити це вручну, а можна за допомогою класу
"""
# NO Escaping symbols(екранування символів)
print("Example_3_0:", temp_3_0())

# Escaping symbols(екранування символів)
print("Example_3_1: ", temp_3_1())

# Escaping symbols of class (екранування символів за допомогою класу)
# print("Temp_3_2: ", temp_3_2())

# for
print("Example_4: ", temp_4())

# if
print("Example_5: ", temp_5())
