from init import *
from to_excel import ToExcel

class GiaThuocHapu:
  def requests_get(url):
    req = requests.get(url, stream=True, timeout=20)
    soup = BeautifulSoup(req.text, 'html.parser')
    return req

  def request_detail_soup(detail_url, thumb_soup):
    detail_url = thumb_soup.find('a', re.compile(r'button more-product'))
    try:
      req_detail_url = requests.get(detail_url.get('href'), timeout=20, stream=True)
    except requests.exceptions.ConnectionError as e:
      pass
    except requests.exceptions.Timeout as e:
      print(f">>>> Requests Timeout {e}. Try to connect again")
      req_detail_url = requests.get(detail_url.get('href'), timeout=20, stream=True)
    except requests.exceptions.RequestException as e:
      raise SystemExit(e)
      pass
    detail_soup = BeautifulSoup(req_detail_url.content, 'lxml')
    return detail_soup

  def get_thumbs_data(script_replace):
    thumbs = re.findall(r'"thumb":"(.*?)",', script_replace)
    thumbs_data = []

    for item in range(len(thumbs)):
      thumb_soup = BeautifulSoup(thumbs[item], 'html.parser')
      find_img = thumb_soup.find('img', class_='lazy')

      img_url = ''
      packing = ''
      product_url = ''
      detail_product = {'product_url': product_url, 'img_url': img_url, 'packing': packing}

      if find_img is not None:
        img_url = find_img.get('data-original')
        detail_product['img_url'] = img_url

      # go to detail url vd: https://giathuochapu.com/san-pham/actiso-ong-hau-giang/
      detail_soup = GiaThuocHapu.request_detail_soup(detail_url, thumb_soup)

      if detail_url is None and find_img is None:
        thumbs_data.append(detail_product)
      else:
        product_url = detail_url.get('href')
        detail_product['product_url'] = product_url

        find_table = detail_soup.find('table')

        if find_table is None:
          thumbs_data.append(detail_product)

        if find_table is not None:
          find_tr = find_table.find('tr')

          if find_tr is None:
            thumbs_data.append(detail_product)
          else:
            find_td = find_tr.find('td', text=re.compile(r'Quy cách:'))

            if find_td is not None:
              find_next_td = find_tr.td.find_next_sibling('td')

              if find_next_td is not None:
                packing = find_next_td.get_text(strip=True) # quy cach dong goi
                detail_product['packing'] = packing
                thumbs_data.append(detail_product)
              else:
                thumbs_data.append(detail_product)
            else:
              thumbs_data.append(detail_product)
      print("stt....... {} ------- detail {}".format(item, detail_product))
    return thumbs_data

  def remove_regex_data(tree_html):
    script = tree_html.xpath('//script[contains(., "var DVShop =")]/text()')[0]
    scripts = re.sub(r'(\\+n|\\+t|\\)', '', script)

    remove_regex_scripts_1 = scripts.replace('\n/* <![CDATA[ */\nvar DVShop = {"Products":', '')
    remove_regex_scripts_2 = remove_regex_scripts_1.replace(',"ajaxUrl":"https://giathuochapu.com/wp-admin/admin-ajax.php"};\n/* ]]> */\n', '')

    thumbs_data = GiaThuocHapu.get_thumbs_data(remove_regex_scripts_2)
    remove_thumb = re.sub(r'"thumb":"(.*?)",', "", remove_regex_scripts_2)
    remove_expire_date = re.sub(r'"expiration_date":"(.*?)",', "", remove_thumb)
    return re.sub(r'<i (.*?)></i>', "", remove_expire_date)

  def get_results_giathuochapu(req):
    tree = html.fromstring(req.content)

    data = json.loads(GiaThuocHapu.remove_regex_data(tree))

    results = []
    for i in range(len(data)):
      data[i].update(thumbs_data[i])
      results.append(data[i])

    return results

  def save_data_infos_to_excel(results, excel_name_file):
    line = 1
    count_item = 0

    for item in range(len(results)):
      data = results[item]

      product_id = data['product_id']
      product_name = data['name']
      product_price = float(data['item_vip_price']) * 1000
      product_type = data['loai_sp']
      product_url = data['product_url']
      product_image = data['img_url']
      product_packing = data['packing']

      data_infos = (product_id, product_name, product_price, product_url, product_image, product_packing)

      ToExcel.save_data_row_to_excel(line, data_infos, excel_name_file, 0)

      count_item = count_item + 1
      line = line + 1
    print('Total products is: {}'.format(count_item))

if __name__ == "__main__":
  sheet_name = 'giathuochapu'
  excel_name_file = '{}.xls'.format(sheet_name)

  form_data = {
    "log": 'loctai1995',
    "pwd": 'loctai95',
    "redirect_to": 'https://giathuochapu.com/dat-hang/'
  }

  ToExcel.create_headers_to_excel(sheet_name, excel_name_file)

  url_order = form_data["redirect_to"]
  req = GiaThuocHapu.requests_get(url_order)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  results = GiaThuocHapu.get_results_giathuochapu(req)
  GiaThuocHapu.save_data_infos_to_excel(results, excel_name_file)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)}")





