import requests
from bs4 import BeautifulSoup
import re

class NhaThuocLongChau:
  def __init__(url):
    self.url = url

  def request_get(url):
    req_get = requests.get(url, timeout=20, stream=True)
    html_soup = BeautifulSoup(req_get.text, "html.parser")

    return html_soup

  def drugstore_categories_tpcn(drugstore):
    category_drug = drugstore.find("a", "thumbnail").get("href")

    # get category_drug
    category_drug_soup_html = NhaThuocLongChau.request_get(category_drug)
    # get url drug group to drug
    drug_groups = category_drug_soup_html.find(
        "div", "view-category-tpcn").find("div", "ctn").findAll("div", "ctg")
    return drug_groups

  def info_product(prod):
    product_id = prod.get("data-product-id")
    product_name = prod.get("data-name")
    product_price = prod.get("data-price")

    product_category = prod.get("data-category")

    product_img_100x100 = prod.find("div", "thumbnail")

    if product_img_100x100 is not None:
      product_img_100x100 = product_img_100x100.img.get("src")
    else:
      product_img_100x100 = None
    line = line + 1
    print("line: ", line)
    print("------> id: {}, name: {}, price: {}".format(product_id,
                                                        product_name, product_price))

    ############ Go to Detail of Drug ###############
    product_detail_url = prod.find("a").get("href")
    detail_req = requests.get(
        product_detail_url, stream=True, timeout=20)
    detail_soup = BeautifulSoup(detail_req.text, "html.parser")

    slide_img = detail_soup.find("div", "product-info-in product-slide").find(
        "div", "gallery-top swiper-container swiper-container-horizontal")
    img = slide_img.find("div", "swiper-slide").img

    if img is not None:
      product_img_600x600 = img.get("src")
    else:
      product_img_600x600 = None

  def crawl_data(url):
    soup_html = NhaThuocLongChau.request_get(url)
    categories_tpcn = soup_html.find(
        "div", "category-tpcn").findAll("div", "col-xs-6 col-sm-2")

    for drugstore in categories_tpcn:
      drug_groups = NhaThuocLongChau.drugstore_categories_tpcn(drugstore)

      for drug_group in drug_groups:
        druggroup = drug_group.a.get("href")
        page = 1

        # druggroup with page
        while True:
          number_page = "?page={}".format(page)
          druggroup_per_page = druggroup + number_page

          druggroup_soup = NhaThuocLongChau.request_get(druggroup_per_page)

          print("================= drug group perpage", druggroup_per_page)

          products = druggroup_soup.find(
              "div", "tab-content-bcn tab-content-item current").findAll("div", "prd col-sm-3 col-xs-6 grid-group-item")

          if not products:
            break

          for prod in products:
            info_prod = NhaThuocLongChau.info_product(prod)
          page = page + 1



# if __name__ == "__main__":
#   url = "https://nhathuoclongchau.com/thuc-pham-chuc-nang"
#   NhaThuocLongChau.crawl_data(url)

# url = "https://nhathuoclongchau.com/thuc-pham-chuc-nang"

# req_url = requests.get(url, timeout=20, stream=True)
# soup = BeautifulSoup(req_url.text, "html.parser")

# categories_tpcn = soup.find("div", "category-tpcn").findAll("div", "col-xs-6 col-sm-2")

# for drugstore in categories_tpcn:
#   category_drug = drugstore.find("a", "thumbnail").get("href")
#   # get category_drug
#   req_category_drug = requests.get(category_drug, timeout=20, stream=True)
#   category_drug_soup = BeautifulSoup(req_category_drug.text, "html.parser")
#   # get url drug group to drug
#   drug_groups = category_drug_soup.find("div", "view-category-tpcn").find("div", "ctn").findAll("div", "ctg")

#   for drug_group in drug_groups:
#     druggroup = drug_group.a.get("href")
#     page = 1

#     # druggroup with page
#     while True:
#       number_page = "?page={}".format(page)
#       druggroup_per_page = druggroup + number_page
#       req_druggroup = requests.get(druggroup_per_page, timeout=20, stream=True)
#       druggroup_soup = BeautifulSoup(req_druggroup.text, "html.parser")
#       print("================= drug group perpage", druggroup_per_page)
#       products = druggroup_soup.find("div", "tab-content-bcn tab-content-item current").findAll("div", "prd col-sm-3 col-xs-6 grid-group-item")

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

#         print("------> id: {}, name: {}, price: {}".format(product_id, product_name, product_price))

#         ############ Go to Detail of Drug ###############
#         product_detail_url = prod.find("a").get("href")
#         detail_req = requests.get(product_detail_url, stream=True, timeout=20)
#         detail_soup = BeautifulSoup(detail_req.text, "html.parser")

#         slide_img = detail_soup.find("div", "product-info-in product-slide").find("div", "gallery-top swiper-container swiper-container-horizontal")
#         img = slide_img.find("div", "swiper-slide").img

#         if img is not None:
#           product_img_600x600 = img.get("src")
#         else:
#           product_img_600x600 = None
#       page = page + 1





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

#       druggroup_soup = NhaThuocLongChau.request_get(druggroup_per_page)

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
#             "div", "gallery-top swiper-container swiper-container-horizontal")
#         img = slide_img.find("div", "swiper-slide").img
#         if img is not None:
#           product_img_600x600 = img.get("src")
#         else:
#           product_img_600x600 = None
#         line = line + 1
#       page = page + 1







# main_category_drug_urls = ['https://nhathuoclongchau.com/duoc-my-pham',
#                            'https://nhathuoclongchau.com/cham-soc-ca-nhan']
main_category_drug_urls = ['https://nhathuoclongchau.com/thuc-pham-chuc-nang/ho-tro-dac-biet?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/me-va-be?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/sinh-ly-noi-tiet-to?src=mega-menu',
'https://nhathuoclongchau.com/thuc-pham-chuc-nang/vitamin-thuoc-bo?src=mega-menu', 'https://nhathuoclongchau.com/thuc-pham-chuc-nang/lam-dep-tang-giam-can?src=mega-menu', 'https://nhathuoclongchau.com/duoc-my-pham', 'https://nhathuoclongchau.com/cham-soc-ca-nhan']
line = 1
for main_category in main_category_drug_urls:
  req_main_category = requests.get(main_category, timeout=20, stream=True)
  soup_main_category_html = BeautifulSoup(
      req_main_category.text, "html.parser")

  if 'https://nhathuoclongchau.com/duoc-my-pham' in main_category:
    find_categories = soup_main_category_html.find(
        "div", "view-category").find_all("div", "col-xs-12 col-sm-15 ctg")

    for categories in find_categories:
      category_url = categories.a.get("href")
      print(category_url)
      req_category_html = NhaThuocLongChau.request_get(category_url)
      drug_groups = req_category_html.findAll(
          "div", class_="col-xs-12 col-sm-15 ctg")
      print("drug groups", drug_groups)
      for drug_group in drug_groups:
        druggroup = drug_group.a.get("href")
        page = 1

        # druggroup with page
        while True:
          number_page = "?page={}".format(page)
          druggroup_per_page = druggroup + number_page

          druggroup_soup = NhaThuocLongChau.request_get(druggroup_per_page)

          print("================= drug group perpage", druggroup_per_page)

          products = druggroup_soup.find(
              "div", "tab-content-bcn tab-content-item current").findAll("div", re.compile("^prd col-sm-3 col-xs-6"))

          if not products:
            break

          for prod in products:
            product_id = prod.get("data-product-id")
            product_name = prod.get("data-name")
            product_price = prod.get("data-price")

            product_category = prod.get("data-category")

            product_img_100x100 = prod.find("div", "thumbnail")

            if product_img_100x100 is not None:
              product_img_100x100 = product_img_100x100.img.get("src")
            else:
              product_img_100x100 = None

            print("line: ", line)
            print("------> id: {}, name: {}, price: {}".format(product_id,
                                                              product_name, product_price))

            ############ Go to Detail of Drug ###############
            product_detail_url = prod.find("a").get("href")
            detail_req = requests.get(
                product_detail_url, stream=True, timeout=20)
            detail_soup = BeautifulSoup(detail_req.text, "html.parser")

            slide_img = detail_soup.find("div", "product-info-in product-slide").find(
                "div", "gallery-top swiper-container swiper-container-horizontal")
            img = slide_img.find("div", "swiper-slide").img

            if img is not None:
              product_img_600x600 = img.get("src")
            else:
              product_img_600x600 = None
            line = line + 1
          page = page + 1
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

        druggroup_soup = NhaThuocLongChau.request_get(druggroup_per_page)

        print("================= drug group perpage", druggroup_per_page)

        products = druggroup_soup.find(
            "div", "tab-content-bcn tab-content-item current").findAll("div", re.compile("^prd col-sm-3 col-xs-6"))

        if not products:
          break

        for prod in products:
          product_id = prod.get("data-product-id")
          product_name = prod.get("data-name")
          product_price = prod.get("data-price")

          product_category = prod.get("data-category")

          product_img_100x100 = prod.find("div", "thumbnail")

          if product_img_100x100 is not None:
            product_img_100x100 = product_img_100x100.img.get("src")
          else:
            product_img_100x100 = None

          print("line: ", line)
          print("------> id: {}, name: {}, price: {}".format(product_id,
                                                            product_name, product_price))

          ############ Go to Detail of Drug ###############
          product_detail_url = prod.find("a").get("href")
          detail_req = requests.get(
              product_detail_url, stream=True, timeout=20)
          detail_soup = BeautifulSoup(detail_req.text, "html.parser")

          slide_img = detail_soup.find("div", "product-info-in product-slide").find(
              "div", "gallery-top swiper-container swiper-container-horizontal")
          img = slide_img.find("div", "swiper-slide").img
          if img is not None:
            product_img_600x600 = img.get("src")
          else:
            product_img_600x600 = None
          line = line + 1
        page = page + 1
