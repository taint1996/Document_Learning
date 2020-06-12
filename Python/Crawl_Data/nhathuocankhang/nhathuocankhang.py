from init import *
from to_excel import ToExcel as ex

class NhaThuocAnKhang:
    def __init__(self, url):
      self.url = url

    def requests_get_url(url):
        global req

        try:
          req = s.get(url, timeout=20, stream=True)
        except requests.exceptions.ConnectionError as e:
          print(f">>>> Requests Connection Error {e}. Try to connect again")
          req = s.get(drug_url, timeout=20, stream=True)
        except requests.exceptions.Timeout as e:
          print(f">>>> Requests Timeout {e}. Try to connect again")
          req = s.get(drug_url, timeout=20, stream=True)
        except requests.exceptions.RequestException as e:
          raise SystemExit(e)
        except requests.exceptions.HTTPError as err:
          raise SystemExit(err)

        soup = BeautifulSoup(req.content, "lxml")
        return soup

    def get_all_url_categories(drug_url):
        soup_drug = NhaThuocAnKhang.requests_get_url(drug_url)
        find_all_li_tags = soup_drug.find_all("li", class_="nonecate")
        return list(map(lambda tag: tag.a, find_all_li_tags))

    def get_categories_attr(a_tags, data_attr="") -> list:
        return list(map(lambda a_tag: a_tag.get(data_attr), a_tags))

    def get_categories_name(categories_url):
        return list(map(lambda a_tag: a_tag.get_text(strip=True), categories_url))

    def get_info_drug(attr_name):
        return attr_name.find_next('div').get_text(strip=True)

    def get_info_w_name(soup_info, info_name):
        detail_info = soup_info.find("strong", string=re.compile(r"{}".format(info_name)))

        if not detail_info:
            detail_info = ""
        else:
            detail_info = NhaThuocAnKhang.get_info_drug(detail_info)
        return detail_info

    def find_all_span_by_shortdesc(info_sell):
        find_all_span = info_sell.find("div", class_="shortdesc").find_all("span")
        del find_all_span[2] # remove category name

        return find_all_span

    def get_price_product(soup_detail):
        find_price_tag = soup_detail.find("div", class_="price")

        prices = []

        for price, unit in zip(find_price_tag.find_all('strong'), find_price_tag.find_all('span', class_='unit')):
            prices.append(f"{price.get_text(strip=True)}{unit.get_text(strip=True)}")

        return prices

    ######################## Detail Drug: Price 1, price 2, packing, ingredient name, producer, made in ########################
    def get_detail_drug(info_sell, soup_detail):
        shortdesc_infos = NhaThuocAnKhang.find_all_span_by_shortdesc(info_sell)

        product_prices = NhaThuocAnKhang.get_price_product(soup_detail)

        packing = re.sub(r"(.*?):\s", "", shortdesc_infos[0].get_text(strip=True))
        ingredient_name = re.sub(r"(.*?):\s", "", shortdesc_infos[1].get_text(strip=True))
        producer = re.sub(r"(.*?):\s", "", shortdesc_infos[-2].get_text(strip=True))
        made_in = re.sub(r"Sản xuất tại", "", shortdesc_infos[-1].get_text(strip=True))

        if len(product_prices) == 2:
            return [product_prices[0], product_prices[1], packing, ingredient_name, producer, made_in]
        else:
            return [''.join(product_prices), '', packing, ingredient_name, producer, made_in]

    ############################## INFO Drug (Ingredient, Uses, Dosage, Notice, Pharma) ##############################
    def info_ingredient_uses_dosage(soup_info):
        ingredient = NhaThuocAnKhang.get_info_w_name(soup_info, "Thành phần")
        uses = NhaThuocAnKhang.get_info_w_name(soup_info, "Công dụng")
        dosage = NhaThuocAnKhang.get_info_w_name(soup_info, "Liều dùng")

        return [ingredient, uses, dosage]

    def info_notice_caution_exp_to_use(soup_info):
        note_when_using = NhaThuocAnKhang.get_info_w_name(soup_info, "Lưu ý khi sử dụng")
        contraindicated = NhaThuocAnKhang.get_info_w_name(soup_info, "Chống chỉ định")
        side_effects = NhaThuocAnKhang.get_info_w_name(soup_info, "Tác dụng phụ")
        interaction_with_other_drugs = NhaThuocAnKhang.get_info_w_name(soup_info, "Tương tác với thuốc khác")
        preservation = NhaThuocAnKhang.get_info_w_name(soup_info, "Bảo quản")
        driver = NhaThuocAnKhang.get_info_w_name(soup_info, "Lái xe")
        package = NhaThuocAnKhang.get_info_w_name(soup_info, "Đóng gói")
        pregnancy = NhaThuocAnKhang.get_info_w_name(soup_info, "Thai kỳ")
        exp_date = NhaThuocAnKhang.get_info_w_name(soup_info, "Hạn dùng")

        return [note_when_using, contraindicated, side_effects, interaction_with_other_drugs,
                preservation, driver, package, pregnancy, exp_date]

    def info_pharma_drug(soup_info):
        pharmacodynamic = NhaThuocAnKhang.get_info_w_name(soup_info, "Dược lực học")
        pharmacokinetics = NhaThuocAnKhang.get_info_w_name(soup_info, "Dược động học")
        pharmacological = NhaThuocAnKhang.get_info_w_name(soup_info, "Dược lý")
        characteristics = NhaThuocAnKhang.get_info_w_name(soup_info, "Đặc điểm")

        return [pharmacodynamic, pharmacokinetics, pharmacological, characteristics]

    def info_ingredients_drug(soup_info):
        info_ingredient_uses_dosage = NhaThuocAnKhang.info_ingredient_uses_dosage(soup_info)
        info_notice_caution_exp_to_use = NhaThuocAnKhang.info_ingredient_uses_dosage(soup_info)
        info_pharma = NhaThuocAnKhang.info_pharma_drug(soup_info)

        return [*info_ingredient_uses_dosage, *info_notice_caution_exp_to_use, *info_pharma]
    ##########################################################################################

    def categories_info(drug_url):
        categories_a_tag = NhaThuocAnKhang.get_all_url_categories(drug_url)

        categories_id = NhaThuocAnKhang.get_categories_attr(categories_a_tag, "data-id")
        categories_name = NhaThuocAnKhang.get_categories_name(categories_a_tag)
        categories_url = list(map(lambda category_url: f"{url}{category_url.get('href')}", categories_a_tag))

        return [categories_id, categories_url, categories_name]

    def url_drugs_list_by_category(soup_category):
        category_li_tags_by_get = soup_category.find('ul', class_='cate')

        if category_li_tags_by_get:
            li_tags = category_li_tags_by_get.find_all("li")
            return list(map(lambda li: f"{url}{li.a.get('href')}", li_tags))
        else:
            return False

    def save_drug_info_to_excel(url_drugs_list_by_category, row, excel_name_file, categories):
        for url_drug_w_get_category in url_drugs_list_by_category:
            soup_detail_info = NhaThuocAnKhang.requests_get_url(url_drug_w_get_category)

            info_sell = soup_detail_info.find("aside", class_="infosell")
            drug_name = info_sell.h1.get_text(strip=True)

            ######################## Detail Drug: Price 1, price 2, packing, ingredient name, producer, made in ########################
            get_detail_drugs = NhaThuocAnKhang.get_detail_drug(info_sell, soup_detail_info)
            #############################

            # TODO: detail drug: create folder images -> folder drug name -> image picture
            # slidedetail = detail_soup.find("aside", class_="slidedetail")
            # Download image by using urlretrieve(url, file_name)
            # urllib.request.urlretrieve(img_url, "neustam-400mg-2-700x467.jpg")

            # information drug and how to use drug
            url_information_drug = f"{url}{soup_detail_info.find('a', class_='viewguide').get('href')}"

            # info ingredients drug: https://www.nhathuocankhang.com/thuoc/thuoc-gian-co-waruwari-2mg-100-vien/thong-tin-cach-dung-thuoc?id=194335
            soup_info = NhaThuocAnKhang.requests_get_url(url_information_drug)
            info_ingredients_drug = NhaThuocAnKhang.info_ingredients_drug(soup_info)

            # Drug info: (Category id, category url, category name, product name, retail price, whosale price, packing, ingredient name, producer, made in, ingredient, uses, dosage, note when using, contraindicated, side effects, interaction_with_other_drugs, preservation, driver, package, pregnancy, exp_date, pharmacodynamic, pharmacokinetics, pharmacological, characteristics)
            drug_infos = [*categories, drug_name, url_drug_w_get_category, *get_detail_drugs, *info_ingredients_drug]

            ex.save_data_row_to_excel(row, drug_infos, excel_name_file, 0)
            row = row + 1

    def save_data_to_excel(excel_name_file):
      row = 1

      categories_id, categories_url, categories_name = NhaThuocAnKhang.categories_info(drug_url)

      for category_id, category_url, category_name in zip(categories_id, categories_url, categories_name):
          categories = [category_id, category_name, category_url]

          soup_category_by_get = NhaThuocAnKhang.requests_get_url(category_url)
          url_drugs_list_by_get_category = NhaThuocAnKhang.url_drugs_list_by_category(soup_category_by_get)

          if url_drugs_list_by_get_category == False:
              continue

          save_data_to_excel_by_get_category = NhaThuocAnKhang.save_drug_info_to_excel(url_drugs_list_by_get_category, row, excel_name_file, categories)

          page_num = 1
          while True:
              params = {
                "Key": "",
                "PageSize": "10",
                "PageIndex": page_num,
                "Category": category_id,
              }

              req_category_drug = s.post(prod_url, data=params, timeout=20, stream=True)

              # If requests post category is 500 -> jump to another category
              if req_category_drug.status_code == 500:
                  break

              soup_category_drug = BeautifulSoup(req_category_drug.content, "lxml")
              url_drugs_list_by_post_category = NhaThuocAnKhang.url_drugs_list_by_category(soup_category_drug)

              if url_drugs_list_by_post_category == False:
                  break

              for detail_url in url_drugs_list_by_post_category:
                  soup_detail_info = NhaThuocAnKhang.requests_get_url(detail_url)

                  info_sell = soup_detail_info.find("aside", class_="infosell")
                  drug_name = info_sell.h1.get_text(strip=True)

                  ######################## Detail Drug: Price 1, price 2, packing, ingredient name, producer, made in ########################
                  get_detail_drugs = NhaThuocAnKhang.get_detail_drug(info_sell, soup_detail_info)
                  #############################

                  # TODO: detail drug: create folder images -> folder drug name -> image picture
                  # slidedetail = detail_soup.find("aside", class_="slidedetail")
                  # Download image by using urlretrieve(url, file_name)
                  # urllib.request.urlretrieve(img_url, "neustam-400mg-2-700x467.jpg")

                  # information drug and how to use drug
                  url_information_drug = f"{url}{soup_detail_info.find('a', class_='viewguide').get('href')}"

                  # info ingredients drug: https://www.nhathuocankhang.com/thuoc/thuoc-gian-co-waruwari-2mg-100-vien/thong-tin-cach-dung-thuoc?id=194335
                  soup_info = NhaThuocAnKhang.requests_get_url(url_information_drug)
                  info_ingredients_drug = NhaThuocAnKhang.info_ingredients_drug(soup_info)

                  # Drug info: (Category id, category url, category name, product name, retail price, whosale price, packing, ingredient name, producer, made in, ingredient, uses, dosage, note when using, contraindicated, side effects, interaction_with_other_drugs, preservation, driver, package, pregnancy, exp_date, pharmacodynamic, pharmacokinetics, pharmacological, characteristics)
                  drug_infos = [*categories, drug_name, detail_url, *get_detail_drugs, *info_ingredients_drug]

                  print(f">>>>>>>>>>>>>> Drug info: {drug_name} ----- {detail_url}")
                  ex.save_data_row_to_excel(row, drug_infos, excel_name_file, 0)
                  row = row + 1
              page_num = page_num + 1
              params["PageIndex"] = page_num