import argparse
import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_products_xlsx_filepath():
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
    
    wine_cards_filepath = get_products_xlsx_filepath()
    excel_data_df = pandas.read_excel(wine_cards_filepath, sheet_name='Лист1', na_values='nan', keep_default_na=False)
    wine_cards = excel_data_df.to_dict(orient='record')

    grouped_wine_cards = defaultdict(list)
    for wine_card in wine_cards:
        grouped_wine_cards[wine_card['Категория']].append(wine_card)

    rendered_page = template.render(grouped_wine_cards=grouped_wine_cards, company_age = company_age)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
if __name__ == '__main__':
    main()