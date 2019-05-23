import re
import requests
from bs4 import BeautifulSoup

import xlwt

from xlrd import open_workbook
from xlutils.copy import copy
from openpyxl.styles import Font

def create_excel_file(self, sheet_name, excel_name):
  book = xlwt.Workbook(encoding='utf-8', style_compression = 0)
  sheet = book.add_sheet(sheet_name, cell_overwrite_ok = True)

  first_rows = ("url", "ten_thuoc", "img", "nhom_thuoc", "nha_san_xuat", "nha_dang_ky", "nha_phan_phoi", "chi_dinh", "lieuluong_cachdung", "chong_chi_dinh", "chu_y", "duoc_luc")

  i = 0
  # Title Default in first line
  while i < len(first_rows):
    # Bold text first rows
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font


    a = sheet.write(0, i, first_rows[i], style=style)
    i = i + 1
  book.save("{}.xls".format(excel_name))

def save_to_excel(self, sheet_name, data, row, column):
  rb = open_workbook(sheet_name, formatting_info=True)

  if rb is not None:
    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    sheet = wb.get_sheet(0)

    i = 0
    while i < len(data):
      writing = sheet.write(row, column, data[i])
      # print(len(sheet._Worksheet__rows)) # count row in sheet
      # print(r_sheet.nrows)
      wb.save(sheet_name)
      i = i + 1
      row = row + 1

def save_text_to_excel(self, sheet_name, text_data, row, column):
  rb = open_workbook(sheet_name, formatting_info=True)

  r_sheet = rb.sheet_by_index(0)
  wb = copy(rb)
  sheet = wb.get_sheet(0)

  writing = sheet.write(row, column, text_data)
  # print(len(sheet._Worksheet__rows)) # count row in sheet
  # print(r_sheet.nrows)
  wb.save(sheet_name)


default_url = "https://www.thuocbietduoc.com.vn"
url = "https://www.thuocbietduoc.com.vn/nhom-thuoc-1-0/thuoc-gay-te-me.aspx"

sheet_name = url.split("/")[-1][:-5] # thuoc-gay-te-me
excel_name = default_url.split("/")[2][4:-7] # thuocbietduoc
excel_name_file = "{}.xls".format(excel_name) # thuocbietduoc.xls

detail_url = "https://www.thuocbietduoc.com.vn/thuoc-60446/lasectil.aspx"

excel = create_excel_file(url, sheet_name, excel_name)

url_details = ["https://www.thuocbietduoc.com.vn/thuoc-60446/lasectil.aspx", "https://www.thuocbietduoc.com.vn/thuoc-60140/tyrosur.aspx"]

# i = 0
# line = 1
# while i < 2:
#   with requests.Session() as s:
#     print("url", url_details[i])
#     res = s.get(url_details[i], timeout=5, stream=True)
#     soup = BeautifulSoup(res.text,"lxml")

#     find_soup = soup.find("article")
#     print("==================== soup article", find_soup)
#     save_text_to_excel(url, excel_name_file, detail_url, line, 0)
#     # Tên thuốc
#     drug_name = find_soup.h1.get_text(strip=True)
#     print(">>>>>>>> drug name", drug_name)
#     save_text_to_excel(url, excel_name_file, drug_name, line, 1)

#     url = find_soup.find("img", class_="imgdrg_lst").get("src")
#     print(">>>>>>>>>>>>> image url", url)
#     save_text_to_excel(url, excel_name_file, url, line, 2)

#     drug_group_name = find_soup.find('a', class_="textdetaillink").get("title")
#     save_text_to_excel(url, excel_name_file, drug_group_name, line, 3)
#     print("======", drug_group_name)

#     nha_san_xuat = find_soup.find(string="Nhà sản xuất:").find_next('span').get_text(strip=True)
#     save_text_to_excel(url, excel_name_file, nha_san_xuat, line, 4)

#     nha_dang_ky = find_soup.find(string="Nhà đăng ký:").find_next('span').get_text(strip=True)
#     save_text_to_excel(url, excel_name_file, nha_dang_ky, line, 5)

#     nha_phan_phoi = find_soup.find(string="Nhà phân phối:").parent.parent.find_next('td').get_text(strip=True)
#     save_text_to_excel(url, excel_name_file, nha_phan_phoi, line, 6)
#     if not nha_phan_phoi:
#       nha_phan_phoi = None

#     chi_dinh = find_soup.find(string="Chỉ định:").find_next("div").get_text(strip=True)
#     save_text_to_excel(url, excel_name_file, chi_dinh, line, 7)

#     lieuluong_cachdung = find_soup.find("section", id="cach-dung", string="Liều lượng - Cách dùng:").find_next("div", class_="textdetaildrg1").get_text(strip=True)
#     print("lieu luong", lieuluong_cachdung)
#     # save_text_to_excel(url, excel_name_file, chi_dinh, line, 7)
#     line = line + 1
#   i = i + 1

############################################## Detail 1 record ###################################
row = 1
with requests.Session() as s:
  res = s.get(url_details[0], timeout=5, stream=True)
  soup = BeautifulSoup(res.text,"lxml")

  find_soup = soup.find("article")
  print("==================== soup article", find_soup)
  save_text_to_excel(url, excel_name_file, detail_url, row, 0)

  # Tên thuốc
  drug_name = find_soup.h1.get_text(strip=True)
  save_text_to_excel(url, excel_name_file, drug_name, row, 1)

  url = find_soup.find("img", class_="imgdrg_lst").get("src")
  save_text_to_excel(url, excel_name_file, url, row, 2)

  drug_group_name = find_soup.find('a', class_="textdetaillink").get("title")
  save_text_to_excel(url, excel_name_file, drug_group_name, row, 3)

  nha_san_xuat = find_soup.find(string="Nhà sản xuất:").find_next('span').get_text(strip=True)
  save_text_to_excel(url, excel_name_file, nha_san_xuat, row, 4)

  nha_dang_ky = find_soup.find(string="Nhà đăng ký:").find_next('span').get_text(strip=True)
  save_text_to_excel(url, excel_name_file, nha_dang_ky, row, 5)

  nha_phan_phoi = find_soup.find(string="Nhà phân phối:").parent.parent.find_next('td').get_text(strip=True)
  save_text_to_excel(url, excel_name_file, nha_phan_phoi, row, 6)
  if not nha_phan_phoi:
    nha_phan_phoi = None

  chi_dinh = find_soup.find(string="Chỉ định:").find_next("div").get_text(strip=True)
  save_text_to_excel(url, excel_name_file, chi_dinh, row, 7)

  lieuluong_cachdung = find_soup.find(string="")#.find_next("div").get_text(strip=True)
  print("=========== lieu luong", lieuluong_cachdung)
  # save_text_to_excel(url, excel_name_file, chi_dinh, line, 7)
