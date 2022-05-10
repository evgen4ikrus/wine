from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
from functions import year_declension
import pandas

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

today = datetime.date.today()
age_company = today.year - 1920

wines = pandas.read_excel('wine.xlsx', sheet_name='wines', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])
wines = wines.to_dict(orient='record')

for wine in wines:
    wine['title'] = wine['Название'] 
    del wine['Название']
    wine['grade'] = wine['Сорт']
    del wine['Сорт']
    wine['price'] = wine['Цена']
    del wine['Цена']
    wine['image'] = 'images/' + wine['Картинка']
    del wine['Картинка']

rendered_page = template.render(wines=wines, age = age_company, year_declension = year_declension(age_company) )
print(wines)
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8008), SimpleHTTPRequestHandler)
server.serve_forever()
