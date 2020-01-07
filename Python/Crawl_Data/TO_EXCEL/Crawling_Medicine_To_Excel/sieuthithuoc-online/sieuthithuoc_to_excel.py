import requests
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

import time
import json

from lxml import html

class ToExcel:
  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def create_headers_to_excel(sheet_name, excel_name_file):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    headers = ("id", "url", "ten_thuoc", "gia_ca", "don_vi")
    bsheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      bsheet.row(0).write(col, header_name, style)
    book.save(excel_name_file)

sheet_name = 'sieuthithuoc-online'
excel_name_file = 'sieuthithuoc-online.xls'

ToExcel.create_headers_to_excel(sheet_name, excel_name_file)

url = 'https://sieuthithuoc.online'
res = requests.get(url, timeout=20, stream=True)
soup = BeautifulSoup(res.text, "html.parser")

find_ul_class_pagination = soup.find('ul', class_='pagination')
li_tags = find_ul_class_pagination.find_all('li')

max_page = int(li_tags[-2].get_text())

line = 1
for page in range(1, max_page + 1):
  res = requests.get(f'https://sieuthithuoc.online/?page={page}', timeout=20, stream=True)
  soup = BeautifulSoup(res.text, 'html.parser')

  tree = html.fromstring(res.content)

  script = tree.xpath('//script[contains(., "app")]/text()')[1]

  remove_space_script = script.split('\n\t')[2].split('\t')[1]
  data_split = remove_space_script.split('items: ')[1]

  data = json.loads(data_split[:-1])['data']

  for item in data:
    open_wb = open_workbook(excel_name_file, formatting_info=True)
    wb_copy = xl_copy(open_wb)
    sheet = wb_copy.get_sheet(0)

    product_id = item['id']

    product_name = item['name']
    product_price = item['price']

    product_type = item['type']
    product_value = item['value']
    product_unit = f'{item["value"]}/{item["type"]}'

    print(f">>>>>>> {product_name} {product_price} {product_value} {product_unit}")

    ToExcel.write_row_to_excel(sheet, product_id, line, 0)
    ToExcel.write_row_to_excel(sheet, product_name, line, 2)
    ToExcel.write_row_to_excel(sheet, product_price, line, 3)
    ToExcel.write_row_to_excel(sheet, product_unit, line, 4)

    wb_copy.save(excel_name_file)
    line = line + 1
