# Refactor thành công
from init import *
from to_excel import ToExcel as ex

class ERZX:
  def __init__(self, url):
    self.url = url

  def find_table_and_remove_comment_html(soup_):
    for element in soup_(text=lambda text: isinstance(text, Comment)):
      element.extract()
    return soup_.find('table', {"width": "820"})

  def get_text_html(field_name):
    return field_name.get_text(strip=True)

  def save_data_to_excel(excel_name_file):
    # Login
    num_page = 1
    line_row = 1

    req_login = s.post(url_login, data=payload, stream=True, timeout=20)
    req_main = s.get(url_main, timeout=20, stream=True)
    count = 0

    while True:
      # Go to List product page
      print(f"======== Go to page {num_page}")
      req_page = s.post(f"https://www.ezrx.com.vn/11_GoodMall/goodmall_l.asp?pageSize=50&leftpage=1&schGoodName=&schMakerName=&pPage={num_page}", stream=True, timeout=20, data=payload)
      soup = BeautifulSoup(req_page.content, 'lxml')

      # table width 820 contain product list
      table_list_product = ERZX.find_table_and_remove_comment_html(soup)

      # TODO: If have issue, we need to print here to see issues # trs = table_list_product.find_all('tr')
      # Tên sản phẩm -> name.get_text(strip=True)
      find_a_tag_names = table_list_product.find_all('a')

      td = table_list_product.findAll('td', text=re.compile(r'Sản phẩm không tồn tại'))

      if td:
        count = count + 1

      if td and count > 5:
        break
      elif not td:
        count = 0

      # Hãng sản xuất - Manufacturer -> prod.get_text(strip=True)
      find_td_manufacturer_names = table_list_product.find_all('td', {"align":"center", "class":"justify", "colspan":"2"})

      # Giá - Price -> prod_price.get('value')
      find_input_tag_prices = table_list_product.find_all('input', {"name": "tbxPrice", "type": "hidden"})

      for name, manufacturer, price in zip(find_a_tag_names, find_td_manufacturer_names, find_input_tag_prices):
        print(f">>>>>>>>>>> {line_row} - Product {ERZX.get_text_html(name)}, Manufacturer in {ERZX.get_text_html(manufacturer)}, price {price.get('value')}")
        ex.save_data_row_to_excel(line_row, [ERZX.get_text_html(name), ERZX.get_text_html(manufacturer), price.get('value')], excel_name_file)
        line_row = line_row + 1

      num_page = num_page + 1



