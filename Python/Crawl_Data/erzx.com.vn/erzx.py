# Refactor thành công
from init import *
from to_excel import ToExcel as ex

class ERZX:
  def __init__(self, url):
    self.url = url

  def requests_goodmall_url(url, params):
    req_page = s.post(url, params=params, stream=True, timeout=20, data=payload)
    soup = BeautifulSoup(req_page.content, 'lxml')
    return soup

  def remove_comment_html(soup_):
    find_table_w_820 = soup_.find('table', {"width": "820"})

    # Remove comment html
    for element in find_table_w_820(text=lambda text: isinstance(text, Comment)):
      element.extract()
    return find_table_w_820

  def save_data_to_excel(excel_name_file):
    # Login
    req_login = s.post(url_login, data=payload, stream=True, timeout=20)
    req_main = s.get(url_main, timeout=20, stream=True)
    num_page = 1
    line_row = 1

    params= {"pageSize": 10, "leftpage": 1, "schGoodName": "", "schMakerName": "", "pPage": num_page}

    while True:
      # Go to List product page
      soup = ERZX.requests_goodmall_url(url_prod, params)

      # table width 820 contain product list
      table_prod = ERZX.remove_comment_html(soup)

      # TODO: If have issue, we need to print here to see issues # trs = table_prod.find_all('tr')
      # Tên sản phẩm -> name.get_text(strip=True)
      find_a_tag_names = table_prod.find_all('a')

      if not find_a_tag_names:
        break

      # Hãng sản xuất - Manufacturer -> prod.get_text(strip=True)
      find_td_manufacturer_names = table_prod.find_all('td', {"align":"center", "class":"justify", "colspan":"2"})

      # Giá - Price -> prod_price.get('value')
      find_input_tag_prices = table_prod.find_all('input', {"name": "tbxPrice", "type": "hidden"})

      for name, manufacturer, price in zip(find_a_tag_names, find_td_manufacturer_names, find_input_tag_prices):
        print(f">>>>>>>>>>> {line_row} - Product {name.get_text(strip=True)}, Manufacturer in {manufacturer.get_text(strip=True)}, price {price.get('value')}")
        ex.save_data_row_to_excel(line_row, [name.get_text(strip=True), manufacturer.get_text(strip=True), price.get('value')], excel_name_file)
        line_row = line_row + 1

      num_page = num_page + 1
      params["pPage"] = num_page



