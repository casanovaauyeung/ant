# coding = utf-8

from jinja2 import Environment
from jinja2 import FileSystemLoader


def template_data(ret):
    env = Environment(loader=FileSystemLoader('D:\workspace\ant\templates'))
    tpl = env.get_template('report.html')
    res = tpl.render(rec=ret, total=len(ret))
    return res