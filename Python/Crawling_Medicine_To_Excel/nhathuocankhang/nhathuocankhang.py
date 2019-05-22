import requests
# import the beautiful soup library
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from openpyxl.styles import Font

import time

class CrawlingNhaThuocAnKhang:
  def __init__(self, url, post_url = "", name = ""):
    self.url = url
    self.post_url = post_url
    self.name = name

  def create_title_excel(self, sheet_name, excel_name):
    book = xlwt.Workbook(encoding='utf-8', style_compression = 0)
    sheet = book.add_sheet(sheet_name, cell_overwrite_ok = True)

    first_rows = ("homepage", "drugs_href", "drug_name", "img", "price", "producer", "made_in_country", "ingredient_and_use")

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

  def start_request_get_home_page(self):
    response = requests.get(self).text
    soup = BeautifulSoup(response, "html.parser")
    first_list = soup.find("nav")

    urls = []

    for item in first_list.find_all('li'):
      get_urls_navbar = item.find('a').get("href")
      urls.append("{}{}".format(self, get_urls_navbar))
    return urls

  def start_request_get_list(self, url):
    response = requests.get(self).text
    soup = BeautifulSoup(response, "html.parser")
    first_list = soup.find("div", id="product")

    # save to excel product url drugs
    urls = []
    names = []
    prices = []
    for item in first_list.find_all('li', {'class': ''}):
      get_href_default = item.find('a').get("href") # Get all a href

      check_url = url in get_href_default
      if check_url:
        urls.append(get_href_default)
      else:
        get_href_default = urls.append("{}/{}".format(self, get_href_default.split("/")[2]))

      # get names
      get_names = item.find('h3').text
      names.append("".join(get_names.strip()))

      # get price
      get_price = item.find('div', class_="price").text
      prices.append("".join(get_price.strip()))

    return urls, names, prices

  def start_requests_post_list(self, post_url, url):
    n = 1
    urls = []
    names = []
    prices = []
    while n:
      form_data = {
        "Key": "",
        "PageSize": "10",
        "PageIndex": n,
        "Category": "0",
        "ListIsNotMedCate": "",
        "IsFunctionFood": "True"
      }

      r = requests.post(post_url, data = form_data)

      if r.status_code == 200 and r.status_code is not None:
        more_soup = BeautifulSoup(r.text, "html.parser")

        next_lists = more_soup.find("div", id="product")

        for item in next_lists.find_all('li', {'class': ''}):
          more_item_urls = item.find('a').get("href")

          check_url = url in more_item_urls
          if check_url is False:
            more_item_urls = "{}/{}".format(self, more_item_urls.split("/")[2])
          urls.append(more_item_urls)

          # get names
          get_names = item.find('h3').text
          names.append("".join(get_names.strip()))

          # get price
          get_price = item.find('div', class_="price").text
          prices.append("".join(get_price.strip()))
      else:
          break
      n = n + 1
    return urls, names, prices

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

start = time.time()
print("Start crawling at: {}".format(start))

##### Get urls href base on navbar index page
url = "https://www.nhathuocankhang.com"
home = CrawlingNhaThuocAnKhang.start_request_get_home_page(url)

sheet_name = home[1].split("/")[-1]
excel_name = home[1].split(".")[1] # nhathuocankhang

excel = CrawlingNhaThuocAnKhang.create_title_excel(url, sheet_name, excel_name)
excel_name_file = "{}.xls".format(excel_name) # nhathuocankhang.xls

to_excel = CrawlingNhaThuocAnKhang.save_home_to_excel(url, excel_name_file, home[1], 1, 0)
# ######################################## thuc-pham-chuc-nang ########################################
get_defaults_page = CrawlingNhaThuocAnKhang.start_request_get_list(home[1], url)
#### show more product list
urls_show_more_list_page = CrawlingNhaThuocAnKhang.start_requests_post_list(home[1], "https://www.nhathuocankhang.com/aj/Category/Products", url)

# #### all url of thucphamchucnang
all_urls_of_tpcn_products = get_defaults_page[0] + urls_show_more_list_page[0]
# save drug href to excel
drug_urls_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(url, excel_name_file, all_urls_of_tpcn_products, 1, 1)

### Drug Information
# name: Tên thuốc
all_drug_names = get_defaults_page[1] + urls_show_more_list_page[1]
drug_names_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(url, excel_name_file, all_drug_names, 1, 2)

# price: Giá
all_drug_prices = get_defaults_page[2] + urls_show_more_list_page[2]
prices_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(url, excel_name_file, all_drug_prices, 1, 4)

details_item_rowinfo = []
details_item_rowcontent = []

images = []
producers = []
mades_in = []

for url in all_urls_of_tpcn_products:
  response = requests.get(url.strip(), params=None)
  soup = BeautifulSoup(response.text, 'html.parser')

  for data in soup.find_all('div', class_="rowinfo"):
    # get mages
    get_images = data.find('aside', class_="slidedetail").find_all('img')
    for img in get_images:
      get_src = img.get('src')

      if get_src:
        images.append(get_src)
      else:
        get_src = None
    # get Item info - thông tin sp
    item_info = data.find_all('aside', class_="infosell")
    details_item_rowinfo.append(str(item_info))

    # get Producer - Nhà sản xuất
    get_producer = data.find('div', class_='shortdesc').find('span').text
    text_producer = "Nhà sản xuất:"
    check_producer = text_producer in get_producer

    # nếu có <span> Nhà sản xuất
    if check_producer is False:
      get_producer = None
    else:
      get_producer = ("".join(get_producer.split(text_producer)))
    producers.append(get_producer)

    # get Made in country - Sản xuất tại
    get_mades_in = data.find('div', class_='shortdesc').find_all('span')
    text_made_in = "Sản xuất tại"
    check_made_in = text_made_in in get_mades_in[-1].text

    if len(get_mades_in) > 1 and check_made_in:
      get_mades_in = ("".join(get_mades_in[-1].text.split(text_made_in)))
    else:
      get_mades_in = None
    mades_in.append(get_mades_in) ########

  # get Ingrediant and use - thành phần và công dụng
  for data in soup.find_all('div', class_='rowcontent'):
    get_row_contents = data.find('div', class_='content collapse')

    for tag in get_row_contents("style"):
      if tag is not None:
        tag.decompose()

    contents = get_row_contents.find_all([re.compile('^p'), re.compile('ul'), re.compile('li')])

    row_contents = []
    for content in contents:
      row_contents.append(u'{}'.format(content.text.strip()))
    details_item_rowcontent.append(row_contents)

# print("============= Row info", details_item_rowinfo)
# print("============= Image", images)
# print("======== producer", producers)
# print("======= made in", mades_in)
# print("Data content", details_item_rowcontent)

images_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(home[1], excel_name_file, images, 1, 3)
producers_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(home[1], excel_name_file, producers, 1, 5)
mades_in_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(home[1], excel_name_file, mades_in, 1, 6)
details_item_row_content_to_excel = CrawlingNhaThuocAnKhang.save_to_excel(home[1], excel_name_file, details_item_rowcontent, 1, 7)

end_at = (time.time() - start) / 60
print("Finished Crawling Data at: {} minute".format(end_at))
#############################################################3########################################