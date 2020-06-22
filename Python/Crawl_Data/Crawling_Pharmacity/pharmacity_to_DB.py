import requests
# import the beautiful soup library
from bs4 import BeautifulSoup

import re

import time
import sys
from datetime import datetime

class Pharmacity:
  def __init__(self, url, post_url="", name=""):
    self.url = url
    self.post_url = post_url
    self.name = name

  def requests_get_url(url):
    req_url = requests.get(url, timeout=20, stream=True)
    soup = BeautifulSoup(req_url.text, "html.parser")
    return soup
##### Get urls href base on navbar index page
print(">>>>>>>>>>>>>>>>>> Here We Go ")
dt_now = datetime.now()
print("Start at: {}".format(dt_now))
#########################################################

url1 = "https://www.pharmacity.vn/danh-muc-san-pham/thuoc-khong-ke-don/"
url2 = "https://www.pharmacity.vn/danh-muc-san-pham/cham-soc-suc-khoe/"

# pharmacity_urls = [url1, url2]
pharmacity_urls = [url2]

for url in pharmacity_urls:
  soup = Pharmacity.requests_get_url(url)
  prod_category = soup.find("ul", "product-categories")
  line = 1
  if url2 == url:
    ul_children = prod_category.find(
        "li", "cat-item cat-item-1594 current-cat cat-parent")
    find_ul_children = ul_children.find("ul", class_="children")
    cate_items = find_ul_children.findAll("li", "cat-item")

    for cate in cate_items:
      i = 1
      if "cat-parent" not in cate.get("class"):
        url_cate_item = cate.a.get("href")
        print(">>>>>>", url_cate_item)
        name_drug_group = cate.a.get_text(strip=True)
        print("url_cate_item", url_cate_item)
        while True:
          page = 'page/{}'.format(i)
          req_url_cate = requests.get(
              url_cate_item + page, stream=True, timeout=20)

          if req_url_cate.status_code == 404:
            break

          cate_soup = BeautifulSoup(req_url_cate.text, "html.parser")
          products = cate_soup.find(
              "div", class_="products row row-small large-columns-4 medium-columns-3 small-columns-2 equalize-box")
          product_drugs = products.find_all(
              "div", class_="product-small col has-hover")

          for prod in product_drugs:
            product_small = prod.find(
                "div", class_="box-text box-text-products")
            prod_title = product_small.find("p", class_="name product-title")
            prod_name = prod_title.a.get_text(strip=True)

            prod_url = prod_title.a.get("href")

            pharmacity_id = product_small.find(
                "div", class_=re.compile("^add-to-cart-button")).a.get("data-product_id")

            print("url: {}\nid: {}".format(prod_url, pharmacity_id))

            print("line:", line)

            ### get detail prod
            req_detail_prod = requests.get(prod_url, timeout=20, stream=True)
            detail_soup = BeautifulSoup(req_detail_prod.text, "html.parser")

            # info_prod is content include image and name, price Product
            info_main_prod = detail_soup.find("div", class_="product-main")

            prod_gallery = info_main_prod.find("div", class_="product-gallery")

            prod_image = prod_gallery.find(
                "img", "wp-post-image skip-lazy lazy-loaded")

            if prod_image is not None:
              prod_image_460x460 = prod_image.get("src")
            else:
              prod_image = None


            prod_info = info_main_prod.find("div", class_="product-info")

            prod_price = prod_info.find("p", class_="product-page-price")
            span_prod_prices = prod_price.findAll("span")

            price = span_prod_prices[0].get_text(
                strip=True) + span_prod_prices[-1].get_text(strip=True)  # Ex: 39,000VND/Chai

            line = line + 1
          i = i + 1
  else:
    prod_child = prod_category.find("ul", "children")

    cate_items = prod_child.find_all("li", "cat-item")

    # line = 1
    for item in cate_items:
      i = 1

      url_cate_item = item.a.get("href")
      print("url cate item", item.a.get_text(strip=True))
      name_drug_group = item.a.get_text(strip=True)

      while True:
        page = 'page/{}'.format(i)
        req_url_cate = requests.get(
            url_cate_item + page, stream=True, timeout=20)

        if req_url_cate.status_code == 404:
          break

        cate_soup = BeautifulSoup(req_url_cate.text, "html.parser")
        products = cate_soup.find(
            "div", class_="products row row-small large-columns-4 medium-columns-3 small-columns-2 equalize-box")
        product_drugs = products.find_all(
            "div", class_="product-small col has-hover")
        print("page: ", page)

        for prod in product_drugs:

          product_small = prod.find("div", class_="box-text box-text-products")
          prod_title = product_small.find("p", class_="name product-title")
          prod_name = prod_title.a.get_text(strip=True)

          prod_url = prod_title.a.get("href")

          pharmacity_id = product_small.find(
              "div", class_=re.compile("^add-to-cart-button")).a.get("data-product_id")

          print("url: {}\nid: {}".format(prod_url, pharmacity_id))

          print("line:", line)

          ### get detail prod
          req_detail_prod = requests.get(prod_url, timeout=20, stream=True)
          detail_soup = BeautifulSoup(req_detail_prod.text, "html.parser")

          # info_prod is content include image and name, price Product
          info_main_prod = detail_soup.find("div", class_="product-main")

          prod_gallery = info_main_prod.find("div", class_="product-gallery")

          prod_image = prod_gallery.find(
              "img", "wp-post-image skip-lazy lazy-loaded")

          if prod_image is not None:
            prod_image_460x460 = prod_image.get("src")
          else:
            prod_image = None


          prod_info = info_main_prod.find("div", class_="product-info")

          prod_price = prod_info.find("p", class_="product-page-price")
          span_prod_prices = prod_price.findAll("span")

          price = span_prod_prices[0].get_text(
              strip=True) + span_prod_prices[-1].get_text(strip=True)  # Ex: 39,000VND/Chai

          line = line + 1
        i = i + 1

dt_end = (datetime.now() - dt_now)
print("We spend: {}".format(dt_end))
