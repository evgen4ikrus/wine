import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint

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

    excel_data_df = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', na_values='nan', keep_default_na=False)
    products = excel_data_df.to_dict(orient='record')
    categoryes = excel_data_df['Категория'].tolist()
    
    categoryes = list(set(categoryes))
    categoryes.sort()
    all_products = collections.defaultdict(list)

    for category in categoryes:
        for product in products:
            if product['Категория'] == category:
                all_products[category].append(product)

    for produkt in products:
        produkt['title'] = produkt['Название'] 
        del produkt['Название']
        produkt['grade'] = produkt['Сорт']
        del produkt['Сорт']
        produkt['price'] = produkt['Цена']
        del produkt['Цена']
        produkt['image'] = 'images/' + produkt['Картинка']
        del produkt['Картинка']
        produkt['category'] = produkt['Категория'] 
        del produkt['Категория'] 
        produkt['promotion'] = produkt['Акция']
        del produkt['Акция'] 

    rendered_page = template.render(products=products, categoryes=categoryes, company_age = company_age, year_declension = get_declension_year(age_company) )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8008), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
if __name__ == '__main__':
    main()