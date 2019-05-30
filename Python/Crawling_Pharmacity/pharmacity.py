import requests
# import the beautiful soup library
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

import time
import sys
from datetime import datetime

class Pharmacity:
  def __init__(self, url, post_url = "", name = ""):
    self.url = url
    self.post_url = post_url
    self.name = name

  def save_to_excel(self, sheet_name, data, row, column):
    rb = open_workbook(sheet_name, formatting_info=True)

    if rb is not None:
      r_sheet = rb.sheet_by_index(0)
      wb = copy(rb)
      sheet = wb.get_sheet(0)

      i = 0
      while i < len(data):
        writing = sheet.write(row, column, data[i])
        wb.save(sheet_name)
        i = i + 1
        row = row + 1

  def save_home_to_excel(self, sheet_name, data, row, column):
    rb = open_workbook(sheet_name, formatting_info=True)

    if rb is not None:
      r_sheet = rb.sheet_by_index(0)
      wb = copy(rb)
      sheet = wb.get_sheet(0)

      writing = sheet.write(row, column, data)

      wb.save(sheet_name)

  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def check_presence_find_next_tag_by_find(tag, tag_name = "", classname = ""):
    if tag is None:
      tag = ""
    else:
      tag = tag.find_next(tag_name, class_=classname).get_text(strip=True)
    return tag

  def create_headers_to_excel(sheet_name, excel_name_file):
    wb = xlwt.Workbook(encoding='utf-8', style_compression = 0)

    ws = wb.add_sheet(sheet_name, cell_overwrite_ok=True)

    headers = ("url", "ten_thuoc", "gia_ca", "img", "nhom_thuoc", "qui_cach_dong_goi", "nha_san_xuat", "san_xuat_tai", "tinh_trang_sp", "thanh_phan", "cong_dung", "lieu_dung", "chong_chi_dinh", "luu_y_khi_su_dung", "tac_dung_phu", "tuong_tac_voi_thuoc_khac", "bao_quan", "lai_xe", "dong_goi", "thai_ky", "han_su_dung", "duoc_luc_hoc", "duoc_dong_hoc", "dac_diem")

    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')
    for col, header_name in enumerate(headers):
      ws.row(0).write(col, header_name, style)

##### Get urls href base on navbar index page

print(">>>>>>>>>>>>>>>>>> Here We Go ")
dt_now = datetime.now()
print("Start at: {}".format(dt_now))

### create Excel xls file
book = xlwt.Workbook(encoding="utf-8", style_compression=0)

headers = ("url", "ten_thuoc", "gia_ca", "img", "nhom_thuoc", "qui_cach_dong_goi", "nha_san_xuat", "san_xuat_tai", "tinh_trang_sp", "thanh_phan", "cong_dung", "lieu_dung", "chong_chi_dinh", "luu_y_khi_su_dung", "tac_dung_phu", "tuong_tac_voi_thuoc_khac", "bao_quan", "lai_xe", "dong_goi", "thai_ky", "han_su_dung", "duoc_luc_hoc", "duoc_dong_hoc", "dac_diem")
bsheet = book.add_sheet("nha-thuoc-ankhang", cell_overwrite_ok=True)
style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

for col, header_name in enumerate(headers):
  bsheet.row(0).write(col, header_name, style)
book.save("nhathuoc-pharmacity.xls")
#########################################################

url = "https://www.pharmacity.vn/danh-muc-san-pham/thuoc-khong-ke-don/"

rp = requests.get(url, timeout=10, stream=True)
soup = BeautifulSoup(rp.text, "html.parser")

prod_cate = soup.find("ul", "product-categories")
prod_child = prod_cate.find("ul", "children")

cate_items = prod_child.find_all("li", "cat-item")

line = 1
for item in cate_items:
  open_wb = open_workbook("nhathuoc-pharmacity.xls", formatting_info=True)
  wb_copy = xl_copy(open_wb)
  sheet = wb_copy.get_sheet(0)

  i = 1

  url_cate_item = item.a.get("href")
  print("url cate item", item.a.get_text(strip=True))
  name_drug_group = item.a.get_text(strip=True)

  while True:
    page = 'page/{}'.format(i)
    req_url_cate = requests.get(url_cate_item + page, stream=True, timeout=10)

    if req_url_cate.status_code == 404:
      wb_copy.save("nhathuoc-pharmacity.xls")
      break

    cate_soup = BeautifulSoup(req_url_cate.text, "html.parser")
    products = cate_soup.find("div", class_="products row row-small large-columns-4 medium-columns-3 small-columns-2 equalize-box")
    url_products = products.find_all("div", class_="box-text-products")
    print("page: ", page)
    for url in url_products:
      Pharmacity.write_row_to_excel(sheet, name_drug_group, line, 4)
      
      url_prod = url.a.get("href")
      Pharmacity.write_row_to_excel(sheet, url_prod, line, 0)
      print(url_prod)
      print("line:", line)
      ### get detail prod
      req_detail_prod = requests.get(url_prod, timeout=10, stream=True)
      detail_soup = BeautifulSoup(req_detail_prod.text, "html.parser")

      # info_prod is content include image and name, price Product
      info_main_prod = detail_soup.find("div", class_="product-main")

      prod_gallery = info_main_prod.find("div", class_="product-gallery")

      images = prod_gallery.findAll("img", class_="attachment-woocommerce_thumbnail")

      imgArr = []
      for img in images:
        url_img = img.get("src")
        imgArr.append(url_img)

      Pharmacity.write_row_to_excel(sheet, imgArr, line, 3)

      prod_info = info_main_prod.find("div", class_="product-info")
      prod_name = prod_info.h1.get_text(strip=True)
      Pharmacity.write_row_to_excel(sheet, prod_name, line, 1)

      prod_price = prod_info.find("p", class_="product-page-price")
      span_prod_prices = prod_price.findAll("span")

      price = span_prod_prices[0].get_text(strip=True) + span_prod_prices[-1].get_text(strip=True) # Ex: 39,000VND/Chai
      Pharmacity.write_row_to_excel(sheet, price, line, 2)

      in_stock = prod_info.find("p", class_="stock").get_text(strip=True)
      Pharmacity.write_row_to_excel(sheet, in_stock, line, 8)
      # in-stock")
      # if in_stock is not None:
      #   in_stock = in_stock.getText(strip=True) # Còn hàng / hết hàng
      # else:
      #   in_stock = None

      # out_of_stock = prod_info.find("p", class_="stock out-of-stock")
      # if out_of_stock is not None:
      #   out_of_stock = out_of_stock.getText(strip=True) # Còn hàng / hết hàng
      # else:
      #   out_of_stock = None



      ### Detail prod is description product
      # desc_prod = detail_soup.find("div", id="tab-description")
      # label_chong_chi_dinh = desc_prod.p.find("strong", text=re.compile("Chống chỉ định"))
      # if label_chong_chi_dinh is not None:
      #   label_chong_chi_dinh = label_chong_chi_dinh.next_element
      #   chong_chi_dinh = label_chong_chi_dinh.next_element
      # else:
      #   chong_chi_dinh = None
      line = line + 1
    i = i + 1

dt_end = (datetime.now() - dt_now)
print("We spend: {}".format(dt_end.total_seconds()))
