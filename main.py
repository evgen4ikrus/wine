from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
from functions import year_declension
import pandas
from pprint import pprint

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

today = datetime.date.today()
age_company = today.year - 1920

products = pandas.read_excel('wine2.xlsx', sheet_name='Лист1', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка'], na_values='nan', keep_default_na=False)
products = products.to_dict(orient='record')

white_wines, drinks, red_wines, all_products = [], [], [], {}
for product in products:
    if product['Категория'] == 'Белые вина':
        white_wines.append(product)
    elif product['Категория'] == 'Напитки':
        drinks.append(product)
    else:
        red_wines.append(product)       
all_products['Белые вина'] = white_wines
all_products['Напитки'] = drinks
all_products['Красные вина'] = red_wines
pprint(all_products)

for produkt in products:
    produkt['title'] = produkt['Название'] 
    del produkt['Название']
    produkt['grade'] = produkt['Сорт']
    del produkt['Сорт']
    produkt['price'] = produkt['Цена']
    del produkt['Цена']
    produkt['image'] = 'images/' + produkt['Картинка']
    del produkt['Картинка']

rendered_page = template.render(products=products, age = age_company, year_declension = year_declension(age_company) )

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
