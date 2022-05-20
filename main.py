from collections import defaultdict
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import argparse
import isort
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_wine_cards_xlsx_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        help='Укажите путь к файлу с продукцией, по умолчанию table_sample.xlsx',
        default='table_sample.xlsx')
    args = parser.parse_args()
    return args.filepath


def get_company_age(company_foundation_year):
    today = datetime.date.today()
    company_age = today.year - company_foundation_year
    if company_age % 10 == 1 and company_age % 100 != 11:
        return f'{company_age} год'
    elif company_age % 10 in [1, 2, 3, 4]:
        if company_age % 100 // 10 == 1:
            return f'{company_age} лет'
        else:
            return f'{company_age} года'
    else:
        return f'{company_age} лет'


def main():
    env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    
    company_foundation_year = 1920
    company_age = get_company_age(company_foundation_year)
    
    products_filepath = get_wine_cards_xlsx_filepath()
    excel_data_df = pandas.read_excel(products_filepath, sheet_name='Лист1', na_values='nan', keep_default_na=False)
    products = excel_data_df.to_dict(orient='record')

    all_products = defaultdict(list)
    for product in products:
        all_products[product['Категория']].append(product)

    rendered_page = template.render(all_products=all_products, company_age = company_age)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8008), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
if __name__ == '__main__':
    main()