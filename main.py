from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
from functions import year_declension

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

today = datetime.date.today()
age_company = today.year - 1920

rendered_page = template.render(
    age = age_company,
    year_declension = year_declension(age_company)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8008), SimpleHTTPRequestHandler)
server.serve_forever()
