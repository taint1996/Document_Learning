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

  # Get all href menu on homepage
  # def start_request_get_home_page(self):
  #   response = requests.get(self, timeout=10, stream=True).text
  #   soup = BeautifulSoup(response, "html.parser")
  #   first_list = soup.find_all("div", attrs={"class": "clearfix_menu", "id": "menu")

  #   urls = []

  #   for item in first_list.find("div", attrs={"class": "ddcolortabs", "id": "ddtabs4"):
  #     get_urls_navbar = item.find('a').get("href")
  #     urls.append("{}{}".format(self, get_urls_navbar))
  #   return urls

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

  # def start_requests_post_list(self, post_url, url):
  #   n = 1
  #   urls = []
  #   names = []
  #   prices = []
  #   while n:
  #     form_data = {
  #       "Key": "",
  #       "PageSize": "10",
  #       "PageIndex": n,
  #       "Category": "0",
  #       "ListIsNotMedCate": "",
  #       "IsFunctionFood": "True"
  #     }

  #     r = requests.post(post_url, data = form_data)

  #     if r.status_code == 200 and r.status_code is not None:
  #       more_soup = BeautifulSoup(r.text, "html.parser")

  #       next_lists = more_soup.find("div", id="product")

  #       for item in next_lists.find_all('li', {'class': ''}):
  #         more_item_urls = item.find('a').get("href")

  #         check_url = url in more_item_urls
  #         if check_url is False:
  #           more_item_urls = "{}/{}".format(self, more_item_urls.split("/")[2])
  #         urls.append(more_item_urls)

  #         # get names
  #         get_names = item.find('h3').text
  #         names.append("".join(get_names.strip()))

  #         # get price
  #         get_price = item.find('div', class_="price").text
  #         prices.append("".join(get_price.strip()))
  #     else:
  #         break
  #     n = n + 1
  #   return urls, names, prices

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

##### Get urls href base on navbar index page

default_url = "https://www.thuocbietduoc.com.vn"
url = "https://www.thuocbietduoc.com.vn/thuoc/drgsearch.aspx"


# This  will get all menu home page
# homepage_url = "https://www.thuocbietduoc.com.vn/home/"
# home = ThuocBietDuoc.start_request_get_home_page(homepage_url)

# sheet_name = home[1].split("/")[-1]
# excel_name = home[1].split(".")[1]

# excel = ThuocBietDuoc.create_excel_file(url, sheet_name, excel_name)
# excel_name_file = "{}.xls".format(excel_name) # nhathuocankhang.xls

# to_excel = ThuocBietDuoc.create_excel_file(url, excel_name_file, home[1], 1, 0)

# ######################################## Nhóm thuốc ########################################
start = time.time()

medicine_group_urls = ThuocBietDuoc.start_request_get_list(url, default_url)
# excel = ThuocBietDuoc.create_excel_file(url, sheet_name, excel_name)

# go to page drug
# TODO: test get 1 url
# res = requests.get(medicine_group_urls[0][0], timeout=10, stream=True)
# soup = BeautifulSoup(res.text, "html.parser")
# find_soup = soup.find("table", attrs={"class": "text2", "id": "Tabl1"})

# find_a_href = find_soup.find_all("a", class_="textlink01_v")

# default_href_to_details = []

# for url in find_a_href:
#   url_href = url.get("href")

#   # check unique url href
#   if url_href not in default_href_to_details:
#     default_href_to_details.append(url_href)

# print("all detail url", default_href_to_details)

################################### TODO: DONT DELETE HERE ########################
# get_default_medicine_group_urls = []
# i = 0
# while i < len(medicine_group_urls[0]):
#   res = requests.get(medicine_group_urls[0][i], timeout=10, stream=True)
#   soup = BeautifulSoup(res.text, "html.parser")
#   find_soup = soup.find("table", attrs={"class": "text2", "id": "Tabl1"})

#   find_a_href = find_soup.find_all("a", class_="textlink01_v")

#   for url in find_a_href:
#     url_href = "{}{}".format(default_url, url.get("href")[2:])

#     # check unique url href
#     if url_href not in get_default_medicine_group_urls:
#       get_default_medicine_group_urls.append(url_href)
#   i = i + 1

# print("total: ", len(get_default_medicine_group_urls))

################################### TODO: This is Special for me  ########################
# post_url_medicine_group_urls = []
# i = 0
# total = []
# while i < len(medicine_group_urls[0]):
#   with requests.Session() as s:
#     s.headers={
#                 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
#               }

#     res = s.get(medicine_group_urls[0][i], timeout=20, stream=True)
#     soup = BeautifulSoup(res.text,"lxml")
#     n = 1
#     while True:
#       payload = {item['name']:item.get('value','') for item in soup.select("input[name]")}
#       payload['__VIEWSTATEGENERATOR'] = '336E2262'
#       payload['Drugnews1$Gr1'] = 'Rdrgnm'
#       payload['page'] = n
#       payload['__VIEWSTATEENCRYPTED'] = None
#       payload['currentView'] = '1'
#       req = s.post(medicine_group_urls[0][i], data=payload, headers=s.headers)
#       soup_obj = BeautifulSoup(req.text,"html.parser")

#       find_soup = soup_obj.find("table", attrs={"class": "text2", "id": "Tabl1"})

#       find_a_href = find_soup.find_all("a", class_="textlink01_v")
#       if len(find_a_href) == 0:
#         print("Did we going here?")
#         break

#       for url in find_a_href:
#         url_href = "{}{}".format(default_url, url.get("href")[2:])

#         # check unique url href
#         if url_href not in post_url_medicine_group_urls:
#           print(url_href)
#           post_url_medicine_group_urls.append(url_href)
            # total.append(len(post_url_medicine_group_urls))
#       n = n + 1
#   i = i + 1
#   print("============================= Post urls ", post_url_medicine_group_urls)
#   print("Total URLs", sum(total))
######################################################################################


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
        # check unique url href
        ############### name drug use to uniq drug
        if url_href not in urls_medicine_groups: # and name_drug not in urls_medicine_groups:
          print(url_href)
          urls_medicine_groups.append(url_href)

      n = n + 1
  print("============================= Post urls ", urls_medicine_groups)
  print("============ amount url", len(urls_medicine_groups))
  total.append(len(urls_medicine_groups))
  print("Each url has amount", total)
  print("============== Total group drug", sum(total))
  i = i + 1






######################### TODO: Create Excel file
# sheet_name = medicine_group_urls[0][0].split("/")[-1][:-5] # thuoc-gay-te-me
# excel_name = default_url.split("/")[2][4:-7] # thuocbietduoc
# excel_name_file = "{}.xls".format(excel_name) # thuocbietduoc.xls
# print("Sheet name", sheet_name)
# print("excel name: ", excel_name)
# print("name file: ", excel_name_file)
# excel = ThuocBietDuoc.create_excel_file(medicine_group_urls[0][0], sheet_name, excel_name)

##### Save to excel
# to_excel = ThuocBietDuoc.save_to_excel(medicine_group_urls[0][0], excel_name_file, post_url_medicine_group_urls, 1, 0)


################################################### Save record to Excel #########################################
# def save_detail_drug_to_excel():
i = 0
line = 1
while i < len(urls_medicine_groups):
  with requests.Session() as s:
    res = s.get(urls_medicine_groups[i], timeout=5, stream=True)
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

end = (time.time() - start) / 60

print("We spent {} minute to done this", end)


###################################################### Detail drug 1 Record ###########################################

# row = 1
# with requests.Session() as s:
#   res = s.get(url_details[1], timeout=5, stream=True)
#   soup = BeautifulSoup(res.text,"lxml")

#   find_soup = soup.find("article")
#   save_text_to_excel(url, excel_name_file, detail_url, row, 0)

#   # Tên thuốc
#   drug_name = find_soup.h1.get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, drug_name, row, 1)

#   url = find_soup.find("img", class_="imgdrg_lst").get("src")
#   save_text_to_excel(url, excel_name_file, url, row, 2)

#   nhom_thuoc = find_soup.find('a', class_="textdetaillink").get("title")
#   save_text_to_excel(url, excel_name_file, nhom_thuoc, row, 3)

#   dang_bao_che = find_soup.find(string=re.compile("Dạng bào chế")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, dang_bao_che, row, 4)

#   dong_goi = find_soup.find(string=re.compile("Đóng gói")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, dang_bao_che, row, 5)

#   thanh_phan = find_soup.find(string=re.compile("Thành phần")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, dang_bao_che, row, 6)

#   sdk = find_soup.find(string=re.compile("SĐK")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, dang_bao_che, row, 7)

#   nha_san_xuat = find_soup.find(string=re.compile("Nhà sản xuất")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, nha_san_xuat, row, 8)

#   nha_dang_ky = find_soup.find(string=re.compile("Nhà đăng ký")).find_next('span').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, nha_dang_ky, row, 9)

#   nha_phan_phoi = find_soup.find(string=re.compile("Nhà phân phối")).parent.parent.find_next('td').get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, nha_phan_phoi, row, 10)

#   chi_dinh = find_soup.find(string=re.compile("Chỉ định")).find_next("div").get_text(strip=True).replace("-", "\n")
#   save_text_to_excel(url, excel_name_file, chi_dinh, row, 11)

#   lieuluong_cachdung = find_soup.find(string=re.compile("Liều lượng - Cách dùng")).find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, lieuluong_cachdung, row, 12)

#   # chong_chi_dinh = find_soup.find(string=re.compile("Chống chỉ định").find_next("div").get_text(strip=True)
#   # save_text_to_excel(url, excel_name_file, chong_chi_dinh, row, 13)

#   tac_dung_phu = find_soup.find(string=re.compile("Tác dụng phụ")).find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, tac_dung_phu, row, 14)

#   chu_y_de_phong = find_soup.find(string=re.compile("Chú ý đề phòng")).find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, chu_y_de_phong, row, 15)

#   bao_quan = find_soup.find(string=re.compile("Chú ý đề phòng")).find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, bao_quan, row, 17)

#   ######### Thông tin thành phần
#   duoc_luc = find_soup.find("h3", string=re.compile("Dược lực")).find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, duoc_luc, row, 18)

#   duoc_dong_hoc = find_soup.find("h3", string=re.compile("Dược động học"))
#   if not duoc_dong_hoc:
#     duoc_dong_hoc = ""
#   else:
#     duoc_dong_hoc.find_next("div").get_text(strip=True)
#   save_text_to_excel(url, excel_name_file, duoc_dong_hoc, row, 19)

#   tac_dung = find_soup.find("h3", string=re.compile("Tác dụng ")).find_next("div").get_text(strip=True)

#   chi_dinhs = find_soup.find_all(string=re.compile("Chỉ định"))
#   chi_dinh = ""
#   for content in chi_dinhs:
#     if not content:
#       content = ""
#     else:
#       chi_dinh = chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()

#   # chống chỉ định
#   chong_chi_dinhs = find_soup.find_all(string=re.compile("Chống chỉ định"[1:].lower()))

#   chong_chi_dinh = ""
#   for content in chong_chi_dinhs:
#     if not content:
#       content = ""
#     else:
#       chong_chi_dinh = chong_chi_dinh.strip() + "\n" + content.find_next("div").get_text(strip=True).strip()

#   # Liều lượng - cách dùng
#   lieuluong_cachdungs = find_soup.find_all(string=re.compile("Liều lượng - cách dùng"[1:].lower()))

#   lieuluong_cachdung = ""
#   for content in lieuluong_cachdungs:
#     if not content:
#       content = ""
#     else:
#       lieuluong_cachdung = (lieuluong_cachdung.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()

#   # Tác dụng phụ
#   tac_dung_phus = find_soup.find_all(string=re.compile("Tác dụng phụ"[1:].lower()))

#   tac_dung_phu = ""
#   for content in tac_dung_phus:
#     if not content:
#       content = ""
#     else:
#       tac_dung_phu = (tac_dung_phu.strip() + "\n" + content.find_next("div").get_text(strip=True)).strip()








