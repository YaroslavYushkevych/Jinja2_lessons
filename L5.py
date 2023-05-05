#Template loaders - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader

from jinja2 import Environment, FileSystemLoader, FunctionLoader

#Many template
def temp_1():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page.htm')
    msg = tm.render(domain='http://test.ua', title="Jinja_test")
    return msg




# =====================================================================================
#Many template
print("Example_1: ", temp_1())

