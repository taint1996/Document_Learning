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

  first_rows = ("url", "ten_thuoc", "img", "nhom_thuoc", "dang_bao_che", "dong_goi", "thanh_phan", "sdk", "nha_san_xuat", "nha_dang_ky", "nha_phan_phoi", "chi_dinh", "lieuluong_cachdung", "chong_chi_dinh", "tac_dung_phu", "chu_y_de_phong", "duoc_luc", "duoc_dong_hoc", "tac_dung", "tac_dung_phu")

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

####################################### TODO: test 2 record
i = 0
line = 1
while i < len(url_details):
  with requests.Session() as s:
    res = s.get(url_details[i], timeout=5, stream=True)
    soup = BeautifulSoup(res.text,"lxml")

    find_soup = soup.find("article")
    save_text_to_excel(url, excel_name_file, detail_url, line, 0)

    # Tên thuốc
    ten_thuoc = find_soup.h1.get_text(strip=True)
    # print(">>>>>>>>>", ten_thuoc)
    save_text_to_excel(url, excel_name_file, ten_thuoc, line, 1)

    # img
    img = find_soup.find("img", class_="imgdrg_lst").get("src")
    # print(">>>>>>>>>", img)
    save_text_to_excel(url, excel_name_file, img, line, 2)

    nhom_thuoc = find_soup.find('a', class_="textdetaillink").get("title")
    # print(">>>>>>>>>", nhom_thuoc)
    save_text_to_excel(url, excel_name_file, nhom_thuoc, line, 3)

    dang_bao_che = find_soup.find(string=re.compile("Dạng bào chế")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", dang_bao_che)
    save_text_to_excel(url, excel_name_file, dang_bao_che, line, 4)

    dong_goi = find_soup.find(string=re.compile("Đóng gói")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", dong_goi)
    save_text_to_excel(url, excel_name_file, dong_goi, line, 5)

    thanh_phan = find_soup.find(string=re.compile("Thành phần")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", thanh_phan)
    save_text_to_excel(url, excel_name_file, thanh_phan, line, 6)

    sdk = find_soup.find(string=re.compile("SĐK")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", sdk)
    save_text_to_excel(url, excel_name_file, sdk, line, 7)

    nha_san_xuat = find_soup.find(string=re.compile("Nhà sản xuất")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", nha_san_xuat)
    save_text_to_excel(url, excel_name_file, nha_san_xuat, line, 8)

    nha_dang_ky = find_soup.find(string=re.compile("Nhà đăng ký")).find_next('span').get_text(strip=True)
    # print(">>>>>>>>>", nha_dang_ky)
    save_text_to_excel(url, excel_name_file, nha_dang_ky, line, 9)

    nha_phan_phoi = find_soup.find(string=re.compile("Nhà phân phối")).parent.parent.find_next('td').get_text(strip=True)
    # print(">>>>>>>>>", nha_phan_phoi)
    save_text_to_excel(url, excel_name_file, nha_phan_phoi, line, 10)

    # chỉ định
    chi_dinhs = find_soup.find_all(string=re.compile("Chỉ định"))
    chi_dinh = ""
    for content in chi_dinhs:
      if not content:
        content = ""
      else:
        chi_dinh = chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()
    # print(">>>>>>>>> chi dinh", chi_dinh)
    save_text_to_excel(url, excel_name_file, chi_dinh, line, 11)

    # Liều lượng - cách dùng
    lieuluong_cachdungs = find_soup.find_all(string=re.compile("Liều lượng - cách dùng"[1:].lower()))

    lieuluong_cachdung = ""
    for content in lieuluong_cachdungs:
      if not content:
        content = ""
      else:
        lieuluong_cachdung = (lieuluong_cachdung.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
    # print(">>>>>>>>>", lieuluong_cachdung)
    save_text_to_excel(url, excel_name_file, lieuluong_cachdung, line, 12)

    # chống chỉ định
    chong_chi_dinhs = find_soup.find_all(string=re.compile("Chống chỉ định"[1:].lower()))

    chong_chi_dinh = ""
    for content in chong_chi_dinhs:
      if not content:
        content = ""
      else:
        chong_chi_dinh = chong_chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()
    # print(">>>>>>>>>", chong_chi_dinh)
    save_text_to_excel(url, excel_name_file, chong_chi_dinh, line, 13)

    tac_dung_phu = find_soup.find(string=re.compile("Tác dụng phụ")).find_next("div").get_text(strip=True)
    # print(">>>>>>>>>", tac_dung_phu)
    save_text_to_excel(url, excel_name_file, tac_dung_phu, line, 14)

    chu_y_de_phong = find_soup.find(string=re.compile("Chú ý đề phòng")).find_next("div").get_text(strip=True)
    # print(">>>>>>>>>", chu_y_de_phong)
    save_text_to_excel(url, excel_name_file, chu_y_de_phong, line, 15)

    ######### Thông tin thành phần
    duoc_luc = find_soup.find("h3", string=re.compile("Dược lực")).find_next("div").get_text(strip=True)
    # print(">>>>>>>>>", duoc_luc)
    save_text_to_excel(url, excel_name_file, duoc_luc, line, 16)

    duoc_dong_hoc = find_soup.find("h3", string=re.compile("Dược động học"))
    if not duoc_dong_hoc:
      duoc_dong_hoc = ""
    else:
      duoc_dong_hoc = duoc_dong_hoc.find_next("div").get_text(strip=True)
    # print(">>>>>>>>>", duoc_dong_hoc)
    save_text_to_excel(url, excel_name_file, duoc_dong_hoc, line, 17)

    # Tác dụng
    tac_dung = find_soup.find("h3", string=re.compile("Tác dụng")).find_next("div").get_text(strip=True)
    # print(">>>>>>>>>", tac_dung)
    save_text_to_excel(url, excel_name_file, tac_dung, line, 18)

    # Tác dụng phụ
    tac_dung_phus = find_soup.find_all(string=re.compile("Tác dụng phụ"[1:].lower()))

    tac_dung_phu = ""
    for content in tac_dung_phus:
      if not content:
        content = ""
      else:
        tac_dung_phu = (tac_dung_phu.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
    # print(">>>>>>>>>", tac_dung_phu)
    save_text_to_excel(url, excel_name_file, tac_dung_phu, line, 19)
    line = line + 1
  i = i + 1













############################################## Detail 1 record ###################################

# line = 1
# with requests.Session() as s:
#   res = s.get(url_details[0], timeout=5, stream=True)
#   soup = BeautifulSoup(res.text,"lxml")

#   find_soup = soup.find("article")
#   save_text_to_excel(url, excel_name_file, detail_url, line, 0)

#   # Tên thuốc
#   ten_thuoc = find_soup.h1.get_text(strip=True)
#   # print(">>>>>>>>>", ten_thuoc)
#   save_text_to_excel(url, excel_name_file, ten_thuoc, line, 1)

#   # img
#   img = find_soup.find("img", class_="imgdrg_lst").get("src")
#   # print(">>>>>>>>>", img)
#   save_text_to_excel(url, excel_name_file, img, line, 2)

#   nhom_thuoc = find_soup.find('a', class_="textdetaillink").get("title")
#   # print(">>>>>>>>>", nhom_thuoc)
#   save_text_to_excel(url, excel_name_file, nhom_thuoc, line, 3)

#   dang_bao_che = find_soup.find(string=re.compile("Dạng bào chế")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", dang_bao_che)
#   save_text_to_excel(url, excel_name_file, dang_bao_che, line, 4)

#   dong_goi = find_soup.find(string=re.compile("Đóng gói")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", dong_goi)
#   save_text_to_excel(url, excel_name_file, dong_goi, line, 5)

#   thanh_phan = find_soup.find(string=re.compile("Thành phần")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", thanh_phan)
#   save_text_to_excel(url, excel_name_file, thanh_phan, line, 6)

#   sdk = find_soup.find(string=re.compile("SĐK")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", sdk)
#   save_text_to_excel(url, excel_name_file, sdk, line, 7)

#   nha_san_xuat = find_soup.find(string=re.compile("Nhà sản xuất")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", nha_san_xuat)
#   save_text_to_excel(url, excel_name_file, nha_san_xuat, line, 8)

#   nha_dang_ky = find_soup.find(string=re.compile("Nhà đăng ký")).find_next('span').get_text(strip=True)
#   # print(">>>>>>>>>", nha_dang_ky)
#   save_text_to_excel(url, excel_name_file, nha_dang_ky, line, 9)

#   nha_phan_phoi = find_soup.find(string=re.compile("Nhà phân phối")).parent.parent.find_next('td').get_text(strip=True)
#   # print(">>>>>>>>>", nha_phan_phoi)
#   save_text_to_excel(url, excel_name_file, nha_phan_phoi, line, 10)

#   # chỉ định
#   chi_dinhs = find_soup.find_all(string=re.compile("Chỉ định"))
#   chi_dinh = ""
#   for content in chi_dinhs:
#     if not content:
#       content = ""
#     else:
#       chi_dinh = chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()
#   # print(">>>>>>>>> chi dinh", chi_dinh)
#   save_text_to_excel(url, excel_name_file, chi_dinh, line, 11)

#   # Liều lượng - cách dùng
#   lieuluong_cachdungs = find_soup.find_all(string=re.compile("Liều lượng - cách dùng"[1:].lower()))

#   lieuluong_cachdung = ""
#   for content in lieuluong_cachdungs:
#     if not content:
#       content = ""
#     else:
#       lieuluong_cachdung = (lieuluong_cachdung.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
#   # print(">>>>>>>>>", lieuluong_cachdung)
#   save_text_to_excel(url, excel_name_file, lieuluong_cachdung, line, 12)

#   # chống chỉ định
#   chong_chi_dinhs = find_soup.find_all(string=re.compile("Chống chỉ định"[1:].lower()))

#   chong_chi_dinh = ""
#   for content in chong_chi_dinhs:
#     if not content:
#       content = ""
#     else:
#       chong_chi_dinh = chong_chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()
#   # print(">>>>>>>>>", chong_chi_dinh)
#   save_text_to_excel(url, excel_name_file, chong_chi_dinh, line, 13)

#   tac_dung_phu = find_soup.find(string=re.compile("Tác dụng phụ")).find_next("div").get_text(strip=True)
#   # print(">>>>>>>>>", tac_dung_phu)
#   save_text_to_excel(url, excel_name_file, tac_dung_phu, line, 14)

#   chu_y_de_phong = find_soup.find(string=re.compile("Chú ý đề phòng")).find_next("div").get_text(strip=True)
#   # print(">>>>>>>>>", chu_y_de_phong)
#   save_text_to_excel(url, excel_name_file, chu_y_de_phong, line, 15)

#   ######### Thông tin thành phần
#   duoc_luc = find_soup.find("h3", string=re.compile("Dược lực")).find_next("div").get_text(strip=True)
#   # print(">>>>>>>>>", duoc_luc)
#   save_text_to_excel(url, excel_name_file, duoc_luc, line, 16)

#   duoc_dong_hoc = find_soup.find("h3", string=re.compile("Dược động học"))
#   if not duoc_dong_hoc:
#     duoc_dong_hoc = ""
#   else:
#     duoc_dong_hoc = duoc_dong_hoc.find_next("div").get_text(strip=True)
#   # print(">>>>>>>>>", duoc_dong_hoc)
#   save_text_to_excel(url, excel_name_file, duoc_dong_hoc, line, 17)

#   # Tác dụng
#   tac_dung = find_soup.find("h3", string=re.compile("Tác dụng")).find_next("div").get_text(strip=True)
#   # print(">>>>>>>>>", tac_dung)
#   save_text_to_excel(url, excel_name_file, tac_dung, line, 18)

#   # Tác dụng phụ
#   tac_dung_phus = find_soup.find_all(string=re.compile("Tác dụng phụ"[1:].lower()))

#   tac_dung_phu = ""
#   for content in tac_dung_phus:
#     if not content:
#       content = ""
#     else:
#       tac_dung_phu = (tac_dung_phu.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
#   # print(">>>>>>>>>", tac_dung_phu)
#   save_text_to_excel(url, excel_name_file, tac_dung_phu, line, 19)