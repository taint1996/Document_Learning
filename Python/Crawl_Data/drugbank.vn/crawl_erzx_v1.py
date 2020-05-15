import requests
from bs4 import BeautifulSoup, Comment
from init import *
from urllib.parse import urljoin
from to_excel import ToExcel as ex
from drug_bank import DrugBank

class ERZX:
  def save_data_to_excel(excel_name_file):
    s = requests.Session()
    url_login = "https://www.ezrx.com.vn/10_Member/member_p.asp?flag=log"
    url_main = "https://www.ezrx.com.vn/mainCommon.asp"
    url_prod = "https://www.ezrx.com.vn/11_GoodMall/goodmall_l.asp"

    payload={"tbxUserId":"30338855", "tbxPassword": "1234qwer"}

    # Login
    req_login = s.post(url_login, data=payload, stream=True, timeout=20)
    req_main = s.get(url_main, timeout=20, stream=True)

    line_row = 1
    num_page = 1
    params= {"pageSize": 10, "leftpage": 1, "schGoodName": "", "schMakerName": "", "pPage": num_page}

    while True:
      # Go to List product page
      req_page = s.post(url_prod, params=params, stream=True, timeout=20, data=payload)
      soup = BeautifulSoup(req_page.content, 'lxml')

      # table width 820 contain product list
      table_prod = soup.find('table', {"width": "820"})

      # Remove comment html
      for element in table_prod(text=lambda text: isinstance(text, Comment)):
        element.extract()

      # TODO: If have issue, we need to print here to see issues
      trs = table_prod.find_all('tr')

      # Hãng sản xuất - Manufacturer
      td_production_names = table_prod.find_all('td', {"align":"center", "class":"justify", "colspan":"2"})
      # production_names = [prod.get_text(strip=True) for prod in production_name]

      if not td_production_names:
        break

      # Tên sản phẩm
      a_tag_names = table_prod.find_all('a')
      # name_prod = a_tags[0]

      # Giá - Price
      prod_prices = table_prod.find_all('input', {"name": "tbxPrice", "type": "hidden"})
      # prod_price.get('value')

      for name, manufacturer, price in zip(a_tag_names, td_production_names, prod_prices):
        print(f">>>>>>>>>>> {line_row} - Product {name.get_text(strip=True)}, Manufacturer in {manufacturer.get_text(strip=True)}, price {price.get('value')}")
        ex.save_data_row_to_excel(line_row, [name.get_text(strip=True), manufacturer.get_text(strip=True), price.get('value')], excel_name_file)
        line_row = line_row + 1

      num_page = num_page + 1
      params["pPage"] = num_page



if __name__ == "__main__":
  sheet_name = "Danh sách thuốc"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_ERZX_DS_Thuoc.xls"

  headers_drug_list = ("Sản phẩm", "Hãng sản xuất", "Thành tiền")
  ex.create_headers_to_excel(headers_drug_list, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  ERZX.save_data_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")




