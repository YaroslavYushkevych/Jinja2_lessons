from jinja2 import Template

name = "Yaroslav"

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)