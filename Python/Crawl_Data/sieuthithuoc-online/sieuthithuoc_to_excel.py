import requests
from bs4 import BeautifulSoup

import re

from lxml import html

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

import time
import json

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

class SieuThiThuocOnline:
  def requests_get_url(url, res):
    res = requests.get(url, timeout=20, stream=True)

  def requests_get_url(self):
    req_get = requests.get(self, timeout=20, stream=True)
    html_soup = BeautifulSoup(req_get.text, "html.parser")

    return html_soup

  def max_page():
    url = 'https://sieuthithuoc.online'

    soup = SieuThiThuocOnline.requests_get_url(url)

    find_ul_class_pagination = soup.find('ul', class_='pagination')
    li_tags = find_ul_class_pagination.find_all('li')

    return int(li_tags[-2].get_text())

  def save_data_sieuthithuoc_to_excel():
    line = 1
    count_item = 0

    for page in range(1, SieuThiThuocOnline.max_page() + 1):
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

        count_item = count_item + 1;
        wb_copy.save(excel_name_file)
        line = line + 1
    print('Total products is: {}'.format(count_item))

if __name__ == "__main__":
  sheet_name = 'sieuthithuoc-online'
  excel_name_file = 'sieuthithuoc-online.xls'
  ToExcel.create_headers_to_excel(sheet_name, excel_name_file)

  start = time.time()
  print("Start crawling at: {}".format(start))

  SieuThiThuocOnline.save_data_sieuthithuoc_to_excel()
  end_at = (time.time() - start) / 60

  print("Finished Crawling Data at: {} minute".format(end_at))