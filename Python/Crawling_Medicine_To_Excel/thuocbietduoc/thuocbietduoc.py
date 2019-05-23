import requests
# import the beautiful soup library
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from openpyxl.styles import Font

import time

class ThuocBietDuoc:
  def __init__(self, url, post_url = "", name = ""):
    self.url = url
    self.post_url = post_url
    self.name = name

  def create_excel_file(self, sheet_name, excel_name):
    book = xlwt.Workbook(encoding='utf-8', style_compression = 0)
    sheet = book.add_sheet(sheet_name, cell_overwrite_ok = True)

    first_rows = ("url", "ten_thuoc", "img", "nhom_thuoc", "dang_bao_che", "dong_goi", "thanh_phan", "sdk", "nha_san_xuat", "nha_dang_ky", "nha_phan_phoi", "chi_dinh", "lieuluong_cachdung", "chong_chi_dinh", "chu_y_de_phong", "duoc_luc", "duoc_dong_hoc", "tac_dung", "tac_dung_phu")

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

  def start_request_get_list(self, url):
    response = requests.get(self, timeout=10, stream=True)

    soup = BeautifulSoup(response.text, "html.parser")
    default = soup.find("table", id="Leftsearch1_dlstMenu")
    # TODO: url nhóm thuốc
    urls = []

    # tên nhóm thuốc
    names = []

    for item in default.find_all("a", class_="textpldl"):
      get_hrefs = item.get("href")
      name = item.get("title")
      urls.append("{}{}".format(url, get_hrefs[2:]))
      names.append(name)
    return urls, names

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

  def save_home_to_excel(self, sheet_name, data, row, column):
    rb = open_workbook(sheet_name, formatting_info=True)

    if rb is not None:
      r_sheet = rb.sheet_by_index(0)
      wb = copy(rb)
      sheet = wb.get_sheet(0)

      writing = sheet.write(row, column, data)

      wb.save(sheet_name)

  def save_text_to_excel(self, sheet_name, text_data, row, column):
    rb = open_workbook(sheet_name, formatting_info=True)

    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    sheet = wb.get_sheet(0)

    writing = sheet.write(row, column, text_data)
    # print(len(sheet._Worksheet__rows)) # count row in sheet
    # print(r_sheet.nrows)
    wb.save(sheet_name)

  def check_presence_find_next_tag_by_find(tag, tag_name):
    if tag is None:
      tag = ""
    else:
      tag = tag.find_next("{}".format(tag_name)).get_text(strip=True)

  def check_presence_find_next_div_by_find_all(tag_contents, text_info):
    for content in tag_contents:
      if content is None:
        content = ""
      else:
        text_info = (text_info.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()

  def save_detail_drug_to_excel(url, data, detail_url):
    default_url = "https://www.thuocbietduoc.com.vn"
    url = "https://www.thuocbietduoc.com.vn/nhom-thuoc-1-0/thuoc-gay-te-me.aspx"

    sheet_name = url.split("/")[-1][:-5] # thuoc-gay-te-me
    excel_name = default_url.split("/")[2][4:-7] # thuocbietduoc
    excel_name_file = "{}.xls".format(excel_name) # thuocbietduoc.xls

    excel = ThuocBietDuoc.create_excel_file(detail_url, sheet_name, excel_name)
    i = 0
    line = 1

    while i < len(data):
      with requests.Session() as s:
        res = s.get(data[i], timeout=5, stream=True)
        soup = BeautifulSoup(res.text,"lxml")

        find_soup = soup.find("article")
        print("================= data", data[i])
        ThuocBietDuoc.save_text_to_excel(data[i], excel_name_file, data[i], line, 0)

        # Tên thuốc
        ten_thuoc = find_soup.h1
        if not ten_thuoc:
          ten_thuoc = ""
        else:
          ten_thuoc = ten_thuoc.get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, ten_thuoc, line, 1)

        # img
        img = find_soup.find("img", class_="imgdrg_lst")
        if not img:
          img = ""
        else:
          img = img.get("src")
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, img, line, 2)

        # nhom_thuoc
        nhom_thuoc = find_soup.find('a', class_="textdetaillink")
        if not nhom_thuoc:
          nhom_thuoc = ""
        else:
          nhom_thuoc = nhom_thuoc.get("title")
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, nhom_thuoc, line, 3)

        # Dạng bào chế
        dang_bao_che = find_soup.find("span", class_="textdetailhead1", string=re.compile("Dạng bào chế"))
        if not dang_bao_che:
          dang_bao_che = ""
        else:
          dang_bao_che = dang_bao_che.find_next('span').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, dang_bao_che, line, 4)

        #  Đóng gói
        dong_goi = find_soup.find("span", string=re.compile("Đóng gói"))
        if not dong_goi:
          dong_goi = ""
        else:
          dong_goi = dong_goi.find_next('span').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, dong_goi, line, 5)


        # Thành phần
        thanh_phan = find_soup.find(string=re.compile("Thành phần"))
        if not thanh_phan:
          thanh_phan = ""
        else:
          thanh_phan = thanh_phan.find_next('span').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, thanh_phan, line, 6)

        # SDK
        sdk = find_soup.find(string=re.compile("SĐK"))
        if not sdk:
          sdk = ""
        else:
          sdk = sdk.find_next('span').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, sdk, line, 7)

        # Nhà sản xuất
        nha_san_xuat = find_soup.find(string=re.compile("Nhà sản xuất"))
        if not nha_san_xuat:
          nha_san_xuat = ""
        else:
          nha_san_xuat = nha_san_xuat.find_next('span').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, nha_san_xuat, line, 8)

        # Nhà đăng ký
        nha_dang_ky = find_soup.find(string=re.compile("Nhà đăng ký"))
        if not nha_dang_ky:
          nha_dang_ky = ""
        else:
          nha_dang_ky = nha_dang_ky.find_next('span').get_text(strip=True)
        # print(">>>>>>>>>", nha_dang_ky)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, nha_dang_ky, line, 9)

        # Nhà phân phối
        nha_phan_phoi = find_soup.find(id="lblnhapp", string=re.compile("Nhà phân phối"))
        if not nha_phan_phoi:
          nha_phan_phoi = ""
        else:
          nha_phan_phoi = nha_phan_phoi.find_next('td').get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, nha_phan_phoi, line, 10)

        # chỉ định
        chi_dinhs = find_soup.find_all(string=re.compile("Chỉ định"))
        chi_dinh = ""
        # ThuocBietDuoc.check_presence_find_next_div_by_find_all(chi_dinhs, chi_dinh)
        for content in chi_dinhs:
          if content is None:
            content = ""
          else:
            chi_dinh = (chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, chi_dinh, line, 11)

        # Liều lượng - cách dùng
        lieuluong_cachdungs = find_soup.find_all(string=re.compile("Liều lượng - cách dùng"[1:].lower()))

        lieuluong_cachdung = ""
        for content in lieuluong_cachdungs:
          if content is None:
            content = ""
          else:
            lieuluong_cachdung = (lieuluong_cachdung.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
        # ThuocBietDuoc.check_presence_find_next_div_by_find_all(lieuluong_cachdungs, lieuluong_cachdung)
        # print(">>>>>>>>>", lieuluong_cachdung)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, lieuluong_cachdung, line, 12)

        # chống chỉ định
        chong_chi_dinhs = find_soup.find_all(string=re.compile("Chống chỉ định"[1:].lower()))

        chong_chi_dinh = ""
        for content in chong_chi_dinhs:
          if content is None:
            content = ""
          else:
            chong_chi_dinh = (chong_chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
        # ThuocBietDuoc.check_presence_find_next_div_by_find_all(chong_chi_dinhs, chong_chi_dinh)
        # print(">>>>>>>>>", chong_chi_dinh)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, chong_chi_dinh, line, 13)


        # Chú ý đề phòng
        chu_y_de_phong = find_soup.find("h2", class_="textdetailhead1", string=re.compile("Chú ý đề phòng"))
        if not chu_y_de_phong:
          chu_y_de_phong = ""
        else:
          chu_y_de_phong = chu_y_de_phong.find_next("div").get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, chu_y_de_phong, line, 14)

        ######### Thông tin thành phần
        # Dược lực
        duoc_luc = find_soup.find("h3", string=re.compile("Dược lực"))
        if not duoc_luc:
          duoc_luc = ""
        else:
          duoc_luc = duoc_luc.find_next("div").get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, duoc_luc, line, 15)

        # Dược động học
        duoc_dong_hoc = find_soup.find("h3", string=re.compile("Dược động học"))
        if not duoc_dong_hoc:
          duoc_dong_hoc = ""
        else:
          duoc_dong_hoc = duoc_dong_hoc.find_next("div").get_text(strip=True)
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, duoc_dong_hoc, line, 16)

        # Tác dụng
        tac_dung = find_soup.find("h3", string="Tác dụng :")
        if not tac_dung:
          tac_dung = ""
        else:
          tac_dung = tac_dung.find_next("div").get_text(strip=True)
        # ThuocBietDuoc.check_presence_find_next_tag_by_find(tac_dung, "div")
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, tac_dung, line, 17)

        # Tác dụng phụ
        tac_dung_phus = find_soup.find_all("section", id=re.compile("tac-dung-phu"), string=re.compile("Tác dụng phụ"[1:].lower()))
        tac_dung_phu = ""
        for content in tac_dung_phus:
          if content is None:
            content = ""
          else:
            tac_dung_phu = (tac_dung_phu.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()
        ThuocBietDuoc.save_text_to_excel(url, excel_name_file, tac_dung_phu, line, 18)
        line = line + 1
      i = i + 1

##### Get urls href base on navbar index page

default_url = "https://www.thuocbietduoc.com.vn"
url = "https://www.thuocbietduoc.com.vn/thuoc/drgsearch.aspx"

print(">>>>>>>>>>>>>>>>>> Here We Go ")
from datetime import datetime

dt_now = datetime.now()
print("Start at: {}", dt_now)

# ######################################## List URL Nhóm thuốc ########################################
medicine_group_urls = ThuocBietDuoc.start_request_get_list(url, default_url)

i = 0
total = []
urls_medicine_groups = []
while i < len(medicine_group_urls[0]):
  with requests.Session() as s:
    s.headers={
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
              }
    n = 1
    res = s.get(medicine_group_urls[0][i], headers=s.headers, timeout=20, stream=True)
    soup = BeautifulSoup(res.text,"lxml")
    while True:
      payload = {item['name']:item.get('value','') for item in soup.select("input[name]")}
      payload['__VIEWSTATEGENERATOR'] = '336E2262'
      payload['Drugnews1$Gr1'] = 'Rdrgnm'
      payload['page'] = n
      payload['currentView'] = '1'
      req = s.post(medicine_group_urls[0][i], data=payload,headers=s.headers)
      soup_obj = BeautifulSoup(req.text,"html.parser")

      find_soup = soup_obj.find("table", attrs={"class": "text2", "id": "Tabl1"})

      find_a_href = find_soup.find_all("a", class_="textlink01_v")
      if len(find_a_href) == 0:
        break
      if find_a_href is None:
        continue

      for url in find_a_href:
        url_href = "{}{}".format(default_url, url.get("href")[2:])
        name_drug = url_href[:-5].split("/")[-1] # Get name drug

        # check unique url href #TODO: check later
        ############### name drug use to uniq drug
        if url_href not in urls_medicine_groups: # and name_drug not in urls_medicine_groups:
          urls_medicine_groups.append(url_href)
          ################################################### Save record to Excel #########################################
          ThuocBietDuoc.save_detail_drug_to_excel(url_href, urls_medicine_groups, url_href)

      n = n + 1
  print("============================= Post urls ", urls_medicine_groups)
  print("============ amount url", len(urls_medicine_groups))
  total.append(len(urls_medicine_groups))
  print("Each url has amount", total)
  print("============== Total group drug", sum(total))
  i = i + 1


end = (datetime.now() - start)

print("We spent {} to done this", end)