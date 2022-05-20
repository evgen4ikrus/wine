import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import isort
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

from functions import get_declension_year


def main():
    env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    company_foundation_year = 1920
    today = datetime.date.today()
    company_age = today.year - company_foundation_year
    company_age = str(company_age) + ' ' + get_declension_year(company_age)
    
    excel_data_df = pandas.read_excel('table_sample.xlsx', sheet_name='Лист1', na_values='nan', keep_default_na=False)
    products = excel_data_df.to_dict(orient='record')

    all_products = collections.defaultdict(list)

    for product in products:
        all_products[product['Категория']].append(product)
    
    for product in products:
        product['title'] = product.pop('Название')
        product['grade'] = product.pop('Сорт')
        product['price'] = product.pop('Цена')
        product['image'] = 'images/' + product.pop('Картинка')
        product['category'] = product.pop('Категория')
        product['promotion'] = product.pop('Акция')

    rendered_page = template.render(all_products=all_products, company_age = company_age)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8008), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
if __name__ == '__main__':
    main()