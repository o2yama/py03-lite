import requests
from bs4 import BeautifulSoup
import sys
import csv

table = sys.argv[1]
page = int(sys.argv[2])

url = 'http://localhost:8080/ex2/?table_name={}&page={}'.format(table, page)
result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')

table_name = soup.find('option', disabled_='').text
header = []
body = []


column_names = soup.find('thead').find_all('th')
for name in column_names:
    header.append(name.text)
column_count = len(column_names)

components = soup.find('tbody').find_all('td')

one_row_items = []
for row_items in components:
    if (len(one_row_items) < column_count):
        one_row_items.append(row_items.text)
    else:
        body.append(one_row_items)
        one_row_items = [row_items.text]
body.append(one_row_items)

csv_file_name = '{}{}.csv'.format(table_name, page)

with open(csv_file_name, 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in body:
        writer.writerow(row)
