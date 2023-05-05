#Filters and macros: macro, call

from jinja2 import Template

#Sum
def temp_1():
    cars = [
        {'model': 'Audi', 'price': 23000},
        {'model': 'Shkoda', 'price': 17300},
        {'model': 'Volvo', 'price': 44300},
        {'model': 'BMW', 'price': 21300}
    ]

    tpl = "Summare count of car {{ cs | sum(attribute='price') }}"
    tm = Template(tpl)
    return tm.render(cs=cars)

#Other_filter
def temp_2():
    cars = [
        {'model': 'Audi', 'price': 23000},
        {'model': 'Shkoda', 'price': 17300},
        {'model': 'Volvo', 'price': 44300},
        {'model': 'BMW', 'price': 21300}
    ]

    tpl = "Other_filter {{ cs | max(attribute='price') }}"
    tm = Template(tpl)
    return tm.render(cs=cars)


#Filter in FOR
def temp_3():
    persons = [
        {"name": "Yaroslav", "old": 22, "weight": 78.5},
        {"name": "Olegsandr", "old": 28, "weight": 82.3},
        {"name": "Henrich", "old": 33, "weight": 94.0}
    ]

    tpl = '''
    {% for u in users -%}
    {% filter upper %}{{u.name}}{% endfilter %}
    {% endfor -%}
    '''

    tm = Template(tpl)
    return tm.render(users=persons)



#Macros
def temp_4():
    #DRY – Don’t Repeat Yourself (не повторюйся)
    html = '''
    {% macro input(name, value='', type='text', size=20) -%}
        <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
    {%- endmacro %}

    {{ input('username') }}
    {{ input('email') }}
    {{ input('password') }}
    '''
    tm = Template(html)
    return tm.render()

#Use Call
def temp_5():
    persons = [
        {"name": "Yaroslav", "old": 22, "weight": 78.5},
        {"name": "Olegsandr", "old": 28, "weight": 82.3},
        {"name": "Henrich", "old": 33, "weight": 94.0}
    ]

    html = '''
    {% macro list_users(list_of_user) -%}
    <ul>
    {% for u in list_of_user -%}
        <li>{{u.name}} {{caller(u)}}
    {%- endfor -%}
    </ul>
    {%- endmacro -%}

    {% call(user) list_users(users) %}
        <ul>
        <li>age: {{user.old}}
        <li>weight: {{user.weight}}
        </ul>
    {% endcall -%}
    '''

    tm = Template(html)
    msg = tm.render(users=persons)
    return msg


# =====================================================================================
#Sum
print("Example_1: ", temp_1())

#Other_filter
print("Example_2: ", temp_2())

#Filter in FOR
print("Example_3: ", temp_3())

#Macros
print("Example_4: ", temp_4())

#Use Call
print("Example_5: ", temp_5())
