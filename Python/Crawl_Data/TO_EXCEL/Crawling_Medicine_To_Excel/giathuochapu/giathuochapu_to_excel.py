import requests
from bs4 import BeautifulSoup

import re

from lxml import html

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

from timeit import default_timer as timer
from datetime import timedelta, date
import json

# pip3 install fuzzywuzzy
# pip3 install python-Levenshtein

class ToExcel:
  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def create_headers_to_excel(sheet_name, excel_name_file):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    headers = ("Product Id", "Product Name", "Product Price", 'Product URL', 'Img URL', 'Packing')
    bsheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      bsheet.row(0).write(col, header_name, style)
    book.save(excel_name_file)

class GiaThuocHapu:
  def requests_get(url):
    req = requests.get(url, stream=True, timeout=20)
    soup = BeautifulSoup(req.text, 'html.parser')
    return req

  def get_thumbs_data(script_replace):
    thumbs = re.findall(r'"thumb":"(.*?)",', script_replace)
    thumbs_data = []

    for item in range(len(thumbs)):
      thumb_soup = BeautifulSoup(thumbs[item], 'html.parser')
      find_img = thumb_soup.find('img', class_='lazy')

      img_url = ''
      packing = ''
      product_url = ''
      detail_product = {'product_url': product_url, 'img_url': img_url, 'packing': packing}

      if find_img is not None:
        img_url = find_img.get('data-original')
        detail_product['img_url'] = img_url

      try:
        # go to detail url vd: https://giathuochapu.com/san-pham/actiso-ong-hau-giang/
        detail_url = thumb_soup.find('a', re.compile(r'button more-product'))
        req_detail_url = requests.get(detail_url.get('href'), timeout=20, stream=True)
        detail_soup = BeautifulSoup(req_detail_url.text, 'html.parser')

        if detail_url is None and find_img is None:
          thumbs_data.append(detail_product)
        else:
          product_url = detail_url.get('href')
          detail_product['product_url'] = product_url

          find_table = detail_soup.find('table')
          # print(">>>>>> find table {}", find_table)

          if find_table is None:
            thumbs_data.append(detail_product)

          if find_table is not None:
            find_tr = find_table.find('tr')

            if find_tr is None:
              thumbs_data.append(detail_product)
            else:
              find_td = find_tr.find('td', text=re.compile(r'Quy cách:'))

              if find_td is not None:
                find_next_td = find_tr.td.find_next_sibling('td')

                if find_next_td is not None:
                  packing = find_next_td.get_text(strip=True) # quy cach dong goi
                  detail_product['packing'] = packing
                  # print(">>>>>>> Go to packing?", packing)
                  thumbs_data.append(detail_product)
                else:
                  thumbs_data.append(detail_product)
              else:
                thumbs_data.append(detail_product)
      except requests.exceptions.Timeout as e:
        print('>>> Error Exception: {}'.format(e))
        detail_url = thumb_soup.find('a', re.compile(r'button more-product'))
        req_detail_url = requests.get(detail_url.get('href'), timeout=20, stream=True)
        detail_soup = BeautifulSoup(req_detail_url.text, 'html.parser')

        if detail_url is None and find_img is None:
          thumbs_data.append(detail_product)
        else:
          product_url = detail_url.get('href')
          detail_product['product_url'] = product_url

          find_table = detail_soup.find('table')
          # print(">>>>>> find table {}", find_table)

          if find_table is None:
            thumbs_data.append(detail_product)

          if find_table is not None:
            find_tr = find_table.find('tr')

            if find_tr is None:
              thumbs_data.append(detail_product)
            else:
              find_td = find_tr.find('td', text=re.compile(r'Quy cách:'))

              if find_td is not None:
                find_next_td = find_tr.td.find_next_sibling('td')

                if find_next_td is not None:
                  packing = find_next_td.get_text(strip=True) # quy cach dong goi
                  detail_product['packing'] = packing
                  # print(">>>>>>> Go to packing?", packing)
                  thumbs_data.append(detail_product)
                else:
                  thumbs_data.append(detail_product)
              else:
                thumbs_data.append(detail_product)
      except requests.exceptions.ConnectionError as e:
        thumbs_data.append(detail_product)
      except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
        thumbs_data.append(detail_product)
        continue
      print("stt....... {} ------- detail {}".format(item, detail_product))
    return thumbs_data

  def get_results_giathuochapu(req):
    tree = html.fromstring(req.content)

    script = tree.xpath('//script[contains(., "var DVShop =")]/text()')[0]
    scripts = re.sub(r'(\\+n|\\+t|\\)', '', script)

    script_replace_1 = scripts.replace('\n/* <![CDATA[ */\nvar DVShop = {"Products":', '')
    script_replace_2 = script_replace_1.replace(',"ajaxUrl":"https://giathuochapu.com/wp-admin/admin-ajax.php"};\n/* ]]> */\n', '')

    thumbs_data = GiaThuocHapu.get_thumbs_data(script_replace_2)
    data_remove_thumb = re.sub(r'"thumb":"(.*?)",', "", script_replace_2)
    data_remove_expire_date = re.sub(r'"expiration_date":"(.*?)",', "", data_remove_thumb)#.replace(r'<i class="fa fa-line-chart"></i>', '').replace(r'<i class="fa fa-long-arrow-up"></i>', '').replace('<i class="fa fa-long-arrow-down red"></i>', '')
    real_data = re.sub(r'<i (.*?)></i>', "", data_remove_expire_date)

    data = json.loads(real_data)

    results = []
    for i in range(len(data)):
      data[i].update(thumbs_data[i])
      results.append(data[i])

    return results

  def save_data_to_excel(results):
    line = 1
    count_item = 0

    print(">>>> Total: {}".format(len(results)))

    for item in range(len(results)):
      data = results[item]

      product_id = data['product_id']
      product_name = data['name']
      product_price = float(data['item_vip_price']) * 1000
      product_type = data['loai_sp']
      product_url = data['product_url']
      product_image = data['img_url']
      product_packing = data['packing']

      open_wb = open_workbook(excel_name_file, formatting_info=True)
      wb_copy = xl_copy(open_wb)
      sheet = wb_copy.get_sheet(0)

      ToExcel.write_row_to_excel(sheet, product_id, line, 0)
      ToExcel.write_row_to_excel(sheet, product_name, line, 1)
      ToExcel.write_row_to_excel(sheet, product_price, line, 2)
      ToExcel.write_row_to_excel(sheet, product_url, line, 3)
      ToExcel.write_row_to_excel(sheet, product_image, line, 4)
      ToExcel.write_row_to_excel(sheet, product_packing, line, 5)

      # print(f">>>>>>> id: {product_id} ----- Name: {product_name} -------- Price: {product_price}")

      count_item = count_item + 1
      wb_copy.save(excel_name_file)
      line = line + 1
    print('Total products is: {}'.format(count_item))

if __name__ == "__main__":
  sheet_name = 'giathuochapu'
  excel_name_file = '{}.xls'.format(sheet_name)

  form_data = {
    "log": 'loctai1995',
    "pwd": 'loctai95',
    "redirect_to": 'https://giathuochapu.com/dat-hang/'
  }

  ToExcel.create_headers_to_excel(sheet_name, excel_name_file)

  url_order = form_data["redirect_to"]
  req = GiaThuocHapu.requests_get(url_order)

  start = timer()
  print("Start crawling at 00:00:00")

  results = GiaThuocHapu.get_results_giathuochapu(req)
  GiaThuocHapu.save_data_to_excel(results)

  end = timer()
  print("Finished Crawling Data at: {}".format(timedelta(seconds=end-start)))





