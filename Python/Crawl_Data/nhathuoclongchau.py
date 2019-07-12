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

import simplejson as json

# class NhaThuocLongChau:
#   def __init__(url):
#     self.url = url

#   def requests_get_url(url):
#     req_get = requests.get(url, timeout=20, stream=True)
#     html_soup = BeautifulSoup(req_get.text, "html.parser")
#     return html_soup

# url = "https://nhathuoclongchau.com"
# req_url = requests.get(url, timeout=20, stream=True)
# soup = BeautifulSoup(req_url.text, "html.parser")
# find_main_category_drug_from_navs = soup.find(
#     "div", "collapse navbar-collapse navbar-ex1-collapse").ul.find_all("li")
# # categories_tpcn = find_main_category_drug_from_navs.find("li", "dropdown")
# main_drug_urls = []
# for item in find_main_category_drug_from_navs:
#   div_size_items = item.find_all("div", "size")
#   for div_size in div_size_items:
#     if div_size:
#       div_size_items = div_size.extract()
#   mega_menu_items = item.find_all("li", "mega-menu-item")
#   for mega_item in mega_menu_items:
#     if mega_item:
#       mega_menu_items = mega_item.extract()
#   # print("======= mega", mega_menu_items)
#   li_items = item.find_all("li", class_=None)
#   find_main_drug_dropdown = item.findAll("li", class_="menu-item")
#   if not find_main_drug_dropdown:
#     next
#   for drug_item in find_main_drug_dropdown:
#     main_drug_url = drug_item.a.get("href")
#     main_drug_urls.append(main_drug_url)
#   if not li_items:
#     next
#   else:
#     for li in li_items:
#       category_drug_url = li.a.get("href")
#       if "/benh" in category_drug_url or "bai-viet" in category_drug_url or "/he-thong-cua-hang" in category_drug_url:
#         del li
#       else:
#         main_drug_urls.append(category_drug_url)
# print("main_drug_urls", main_drug_urls)

# main_category_drug_urls = ['https://nhathuoclongchau.com/thuc-pham-chuc-nang/ho-tro-dac-biet?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/me-va-be?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/sinh-ly-noi-tiet-to?src=mega-menu',
# 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/vitamin-thuoc-bo?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/lam-dep-tang-giam-can?src=mega-menu', 'https://nhathuoclongchau.com/duoc-my-pham', 'https://nhathuoclongchau.com/cham-soc-ca-nhan']

# line = 1
# for main_category in main_category_drug_urls:
#   req_main_category = requests.get(main_category, timeout=20, stream=True)
#   soup_main_category_html = BeautifulSoup(req_main_category.text, "html.parser")

#   drug_groups = soup_main_category_html.findAll(
# "div", class_ = "col-xs-12 col-sm-15 ctg")
#   print("drug groups", drug_groups)
#   for drug_group in drug_groups:
#     druggroup = drug_group.a.get("href")
#     page = 1

#     # druggroup with page
#     while True:
#       number_page = "?page={}".format(page)
#       druggroup_per_page = druggroup + number_page

#       druggroup_soup = NhaThuocLongChau.requests_get_url(druggroup_per_page)

#       print("================= drug group perpage", druggroup_per_page)

#       products = druggroup_soup.find(
#           "div", "tab-content-bcn tab-content-item current").findAll("div", re.compile("^prd col-sm-3 col-xs-6"))

#       if not products:
#         break

#       for prod in products:
#         product_id = prod.get("data-product-id")
#         product_name = prod.get("data-name")
#         product_price = prod.get("data-price")

#         product_category = prod.get("data-category")

#         product_img_100x100 = prod.find("div", "thumbnail")

#         if product_img_100x100 is not None:
#           product_img_100x100 = product_img_100x100.img.get("src")
#         else:
#           product_img_100x100 = None

#         print("line: ", line)
#         print("------> id: {}, name: {}, price: {}".format(product_id,
#                                                           product_name, product_price))

#         ############ Go to Detail of Drug ###############
#         product_detail_url = prod.find("a").get("href")
#         detail_req = requests.get(
#             product_detail_url, stream=True, timeout=20)
#         detail_soup = BeautifulSoup(detail_req.text, "html.parser")

#         slide_img = detail_soup.find("div", "product-info-in product-slide").find(
#             "div", "gallery-top swiper-container")
#         print("slide image", slide_img)
#         image = slide_img.find("div", "swiper-slide")
#         print("IMG:", image.img.get("src"))
#         if image is not None:
#           product_img_600x600 = image.img.get("src")
#         else:
#           product_img_600x600 = None
#         line = line + 1
#       page = page + 1
import psycopg2
from psycopg2 import Error

from datetime import datetime

class ConnectionPostgresQL:
  def __init__(self):
    self.conn = psycopg2.connect(database="refer_pharmacy_dev", user="postgres",
                                 password="postgres", host="localhost", port=5432)
    self.cursor = self.conn.cursor()

  def close_connection(self):
    if self.conn:
      self.cursor.close()
      self.conn.close()
      print("PostgreSQL connection is closed")

  def insert_refer_pharmacies_data(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at):
    create_data_query = """ INSERT INTO refer_pharmacies (pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); """

    self.cursor.execute(create_data_query, (pharmacy_id, pharmacy_name,
                                            pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, json.dumps(crawl_data), created_at, updated_at))
    self.conn.commit()
    print("Successfully CREATE data Refer Pharmacies PostgresQL")

  def update_refer_pharmacies_data(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, updated_at):
    update_query = """ UPDATE refer_pharmacies SET pharmacy_name=%s, pharmacy_price=%s,       pharmacy_unit=%s, pharmacy_url=%s, crawl_data=%s, updated_at=%s WHERE pharmacy_id=%s and pharmacy_source=%s """

    self.cursor.execute(update_query, (pharmacy_name, pharmacy_price, pharmacy_unit,
                                       pharmacy_url, json.dumps(crawl_data), updated_at, pharmacy_id, pharmacy_source))
    self.conn.commit()
    print("Successfully UPDATE data with {} Refer Pharmacies PostgresQL".format(
        pharmacy_id))

  def insert_update_refer_pharmacies(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at):
    try:
      query = """SELECT * FROM refer_pharmacies WHERE pharmacy_id=%s AND pharmacy_source=%s"""
      self.cursor.execute(query, (pharmacy_id, pharmacy_source))

      record = self.cursor.fetchone()

      if record is None:
        self.insert_refer_pharmacies_data(pharmacy_id, pharmacy_name, pharmacy_price,
                                          pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at)

      else:
        self.update_refer_pharmacies_data(pharmacy_id, pharmacy_name, pharmacy_price,
                                          pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, updated_at)
    except (Exception, psycopg2.DatabaseError) as error:
      print(" --- Error while INSERT UPDATE refer_pharmacies table", error)

    finally:
      self.close_connection()


class NhaThuocLongChau:
  def __init__(self, url):
    self.url = url

  def requests_get_url(self):
    req_get = requests.get(self, timeout=20, stream=True)
    html_soup = BeautifulSoup(req_get.text, "html.parser")

    return html_soup

  def find_category_drug_group(category_drug_group):
    category_url = category_drug_group.a.get("href")
    print(category_url)
    req_category_html = NhaThuocLongChau.requests_get_url(category_url)
    drug_groups = req_category_html.findAll(
        "div", class_="col-xs-12 col-sm-15 ctg")
    print("drug groups", drug_groups)
    return drug_groups

  def info_product(prod):
    global line

    product_url = prod.a.get("href")
    product_source = "Long Châu"
    product_id = prod.get("data-product-id")
    product_name = prod.get("data-name")
    product_price = prod.get("data-price")
    product_unit = prod.find("div", "caption").find("span", "box").get_text(strip=True)

    crawl_data_json = {}
    time_crawling = datetime.now().strftime("%Y%m%d_%H%M%S")
    crawl_data_json[time_crawling] = {
      "pharmacy_id": product_id,
      "pharmacy_url": product_url,
      "pharmacy_name": product_name,
      "pharmacy_price": product_price,
      "pharmacy_unit": product_unit,
      "pharmacy_source": product_source
    }

    product_category = prod.get("data-category")

    product_img_100x100 = prod.find("div", "thumbnail")

    if product_img_100x100 is not None:
      product_img_100x100 = product_img_100x100.img.get("src")
    else:
      product_img_100x100 = None

    print("line: ", line)
    print("------> id: {}, name: {}, price: {}".format(product_id,
                                                       product_name, product_price))

    created_at = datetime.now().ctime()
    updated_at = datetime.now().ctime()

    ConnectionPostgresQL.insert_update_refer_pharmacies(ConnectionPostgresQL(), product_id, product_name, product_price, product_unit, product_source, product_url, crawl_data_json, created_at, updated_at)
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
    else:
      product_img_600x600 = None
    line = line + 1

  def find_category_duocmypham(soup_main_category_html):
    find_categories = soup_main_category_html.find(
        "div", "view-category").find_all("div", "col-xs-12 col-sm-15 ctg")

    for categories in find_categories:
      drug_groups = NhaThuocLongChau.find_category_drug_group(categories)

      for drug_group in drug_groups:
        druggroup = drug_group.a.get("href")
        page = 1

        # druggroup with page
        while True:
          number_page = "?page={}".format(page)
          druggroup_per_page = druggroup + number_page

          druggroup_soup = NhaThuocLongChau.requests_get_url(
              druggroup_per_page)

          print("================= drug group perpage", druggroup_per_page)

          current = druggroup_soup.find("div", "tab-content-bcn tab-content-item current")
          products = current.findAll("div", class_="prd col-sm-3 col-xs-6 grid-group-item")

          if not products:
            break

          for prod in products:
            NhaThuocLongChau.info_product(prod)
          page = page + 1

  def crawl_data_nhathuoclongchau(main_category_drug_urls):
    for main_category in main_category_drug_urls:
      soup_main_category_html = NhaThuocLongChau.requests_get_url(
          main_category)

      if 'https://nhathuoclongchau.com/duoc-my-pham' in main_category:
        NhaThuocLongChau.find_category_duocmypham(soup_main_category_html)
      else:
        drug_groups = soup_main_category_html.findAll(
            "div", class_="col-xs-12 col-sm-15 ctg")
        print("drug groups", drug_groups)
        for drug_group in drug_groups:
          druggroup = drug_group.a.get("href")
          page = 1

          # druggroup with page
          while True:
            number_page = "?page={}".format(page)
            druggroup_per_page = druggroup + number_page

            druggroup_soup = NhaThuocLongChau.requests_get_url(
                druggroup_per_page)

            print("================= drug group perpage", druggroup_per_page)

            current = druggroup_soup.find("div", "tab-content-bcn tab-content-item current")
            products = current.findAll("div", class_="prd col-sm-3 col-xs-6 grid-group-item")

            if not products or druggroup_per_page in "https://nhathuoclongchau.com/thuc-pham-chuc-nang/sua-296":
              break

            for prod in products:
              NhaThuocLongChau.info_product(prod)
            page = page + 1

if __name__ == "__main__":
  print(">>>>>>>>>>>>>>>>>> Here We Go <<<<<<<<<<<<<<<<<")
  dt_now = datetime.now()
  print("Start at: {}".format(dt_now))

  main_category_drug_urls = ['https://nhathuoclongchau.com/thuc-pham-chuc-nang/ho-tro-dac-biet?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/me-va-be?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/sinh-ly-noi-tiet-to?src=mega-menu',
                             'https://nhathuoclongchau.com/thuc-pham-chuc-nang/vitamin-thuoc-bo?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/lam-dep-tang-giam-can?src=mega-menu', 'https://nhathuoclongchau.com/duoc-my-pham', 'https://nhathuoclongchau.com/cham-soc-ca-nhan']
  line = 1

  NhaThuocLongChau.crawl_data_nhathuoclongchau(main_category_drug_urls)

  dt_end = (datetime.now() - dt_now)
  print("We spend: {}".format(dt_end.total_seconds()))
