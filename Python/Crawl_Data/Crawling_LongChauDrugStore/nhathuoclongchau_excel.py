# import requests
# # import the beautiful soup library
# from bs4 import BeautifulSoup

# import re

# import time
# import sys
# from datetime import datetime

# import simplejson as json

# from datetime import datetime

import requests
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

from datetime import datetime

class NhaThuocLongChau:
  def __init__(self, url):
    self.url = url

  def requests_get_url(self):
    req_get = requests.get(self, timeout=20, stream=True)
    html_soup = BeautifulSoup(req_get.text, "html.parser")

    return html_soup

  def find_category_drug_group(category_drug_group):
    category_url = category_drug_group.a.get("href")
    
    req_category_html = NhaThuocLongChau.requests_get_url(category_url)
    drug_groups = req_category_html.findAll(
        "div", class_="col-xs-12 col-sm-15 ctg")
    
    return drug_groups

  def info_product(sheet_name, prod):
    global line

    product_source = "Long Châu"
    product_id = prod.get("data-product-id")
    ToExcel.write_row_to_excel(sheet_name, product_id, line, 0)

    product_url = prod.a.get("href")
    ToExcel.write_row_to_excel(sheet_name, product_url, line, 1) 

    product_name = prod.get("data-name")
    ToExcel.write_row_to_excel(sheet_name, product_name, line, 2)
    product_price = prod.get("data-price")
    ToExcel.write_row_to_excel(sheet_name, product_price, line, 3)
    product_unit = prod.find("div", "caption").find("span", "box").get_text(strip=True)
    ToExcel.write_row_to_excel(sheet_name, product_unit, line, 4)

    product_category = prod.get("data-category")

    product_img_100x100 = prod.find("div", "thumbnail")

    if product_img_100x100 is not None:
      product_img_100x100 = product_img_100x100.img.get("src")
      ToExcel.write_row_to_excel(sheet_name, product_img_100x100, line, 5)
    else:
      product_img_100x100 = None
      ToExcel.write_row_to_excel(sheet_name, product_img_100x100, line, 5)

    print("line: ", line)
    print("------> id: {}, name: {}, price: {}".format(product_id,
                                                       product_name, product_price))

    ############ Go to Detail of Drug ###############
    product_detail_url = prod.find("a").get("href")
    detail_req = requests.get(
        product_detail_url, stream=True, timeout=20)
    detail_soup = BeautifulSoup(detail_req.text, "html.parser")

    slide_img = detail_soup.find("div", "product-info-in product-slide").find(
        "div", "gallery-top swiper-container")
    image = slide_img.find("div", "swiper-slide")

    print("IMG:", image.img.get("src"))
    if image is not None:
      product_img_600x600 = image.img.get("src")
      ToExcel.write_row_to_excel(sheet_name, product_img_600x600, line, 6)
    else:
      product_img_600x600 = None
      ToExcel.write_row_to_excel(sheet_name, product_img_600x600, line, 6)

    line = line + 1

  def find_category_duocmypham(soup_main_category_html):
    find_categories = soup_main_category_html.find(
        "div", "view-category").find_all("div", "col-xs-12 col-sm-15 ctg")

    open_wb = open_workbook(excel_name_file, formatting_info=True)
    wb_copy = xl_copy(open_wb)
    sheet_name = wb_copy.add_sheet("duoc-my-pham")
    
    for categories in find_categories:
      drug_groups = NhaThuocLongChau.find_category_drug_group(categories)

      for drug_group in drug_groups:
        druggroup_url = drug_group.a.get("href")
        druggroup_name = drug_group.a.get_text(strip=True)
        ToExcel.write_row_to_excel(sheet_name, druggroup_name, line, 7)

        page = 1

        # druggroup with page
        while True:
          number_page = "?page={}".format(page)
          druggroup_per_page = druggroup_url + number_page

          druggroup_soup = NhaThuocLongChau.requests_get_url(
              druggroup_per_page)

          print("================= drug group perpage", druggroup_per_page)

          current = druggroup_soup.find("div", "tab-content-bcn tab-content-item current")
          products = current.findAll("div", class_="prd col-sm-3 col-xs-6 grid-group-item")

          if not products:
            wb_copy.save(excel_name_file)
            break

          for prod in products:
            NhaThuocLongChau.info_product(sheet_name, prod)
          page = page + 1

  def crawling_data_nhathuoclongchau_to_excel(sheet_name, main_category_drug_urls):
    excel_name_file = "nhathuoclongchau.xls"

    ToExcel.create_headers_to_excel(sheet_name, excel_name_file)

    for main_category in main_category_drug_urls:
      soup_main_category_html = NhaThuocLongChau.requests_get_url(
          main_category)

      if 'https://nhathuoclongchau.com/duoc-my-pham' in main_category:        
        NhaThuocLongChau.find_category_duocmypham(soup_main_category_html)
      elif 'https://nhathuoclongchau.com/cham-soc-ca-nhan' in main_category:
        open_wb = open_workbook(excel_name_file, formatting_info=True)
        wb_copy = xl_copy(open_wb)
        sheet_name = wb_copy.add_sheet("cham-soc-ca-nhan")        

        drug_groups = soup_main_category_html.findAll("div", class_="col-xs-12 col-sm-15 ctg")
        print("drug groups", drug_groups)
        for drug_group in drug_groups:
          druggroup_url = drug_group.a.get("href")
          druggroup_name = drug_group.a.get_text(strip=True)
          ToExcel.write_row_to_excel(sheet_name, druggroup_name, line, 7)

          page = 1

          # druggroup with page
          while True:
            number_page = "?page={}".format(page)
            druggroup_per_page = druggroup_url + number_page

            druggroup_soup = NhaThuocLongChau.requests_get_url(druggroup_per_page)

            print("================= drug group perpage", druggroup_per_page)
            products = druggroup_soup.findAll("div", class_="prd col-sm-3 col-xs-6")

            if not products:
              wb_copy.save(excel_name_file)
              break

            for prod in products:
              NhaThuocLongChau.info_product(sheet_name, prod)
            page = page + 1
      else:
        drug_groups = soup_main_category_html.findAll("div", class_="col-xs-12 col-sm-15 ctg")
        print("drug groups", drug_groups)

        open_wb = open_workbook(excel_name_file, formatting_info=True)
        wb_copy = xl_copy(open_wb)
        sheet_name = wb_copy.add_sheet("druggroup_else")        

        for drug_group in drug_groups:
          druggroup_url = drug_group.a.get("href")
          druggroup_name = drug_group.a.get_text(strip=True)
          ToExcel.write_row_to_excel(sheet_name, druggroup_name, line, 7)

          page = 1

          # druggroup with page
          while True:
            number_page = "?page={}".format(page)
            druggroup_per_page = druggroup_url + number_page

            druggroup_soup = NhaThuocLongChau.requests_get_url(druggroup_per_page)

            print("================= drug group perpage", druggroup_per_page)
            products = druggroup_soup.findAll("div", class_="prd col-sm-3 col-xs-6 grid-group-item")
            current = druggroup_soup.find("div", "tab-content-bcn tab-content-item current")

            if not products or druggroup_per_page in "https://nhathuoclongchau.com/thuc-pham-chuc-nang/sua-296":
              wb_copy.save(excel_name_file)
              break

            for prod in products:
              NhaThuocLongChau.info_product(sheet_name, prod)
            page = page + 1

class ToExcel:
  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def create_headers_to_excel(sheet_name, excel_name_file):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    headers = ("id", "url", "ten_thuoc", "gia_ca", "don_vi", "img_100x100", "img_600x600", "nhom_thuoc", "qui_cach_dong_goi", "nha_san_xuat", "san_xuat_tai", "tinh_trang_sp", "thanh_phan", "cong_dung", "lieu_dung", "chong_chi_dinh", "luu_y_khi_su_dung", "tac_dung_phu", "tuong_tac_voi_thuoc_khac", "bao_quan", "lai_xe", "dong_goi", "thai_ky", "han_su_dung", "duoc_luc_hoc", "duoc_dong_hoc", "dac_diem")
    bsheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      bsheet.row(0).write(col, header_name, style)
    book.save(excel_name_file)



if __name__ == "__main__":
  print(">>>>>>>>>>>>>>>>>> Here We Go <<<<<<<<<<<<<<<<<")
  dt_now = datetime.now()
  print("Start at: {}".format(dt_now))

  main_category_drug_urls = ['https://nhathuoclongchau.com/thuc-pham-chuc-nang/ho-tro-dac-biet?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/me-va-be?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/sinh-ly-noi-tiet-to?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/vitamin-thuoc-bo?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/lam-dep-tang-giam-can?src=mega-menu', 'https://nhathuoclongchau.com/duoc-my-pham', 'https://nhathuoclongchau.com/cham-soc-ca-nhan']

  line = 1
  sheet_name = "nha-thuoc-long-chau"
  NhaThuocLongChau.crawling_data_nhathuoclongchau_to_excel(sheet_name, main_category_drug_urls)
  
  dt_end = (datetime.now() - dt_now)
  print("We spend: {} minute".format(dt_end))