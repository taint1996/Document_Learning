from init import *
from to_excel import ToExcel as ex

class NhaThuocAnKhang:
  def __init__(self, url):
    self.url = url

  def get_all_url_categories(drug_url):
    global req

    try:
      req = s.get(drug_url, timeout=10, stream=True)
    except requests.exceptions.ConnectionError as e:
      print(f">>>> Requests Connection Error {e}. Try to connect again")
      req = s.get(drug_url, timeout=10, stream=True)
    except requests.exceptions.Timeout as e:
      print(f">>>> Requests Timeout {e}. Try to connect again")
      req = s.get(drug_url, timeout=10, stream=True)
    except requests.exceptions.RequestException as e:
      raise SystemExit(e)

    soup = BeautifulSoup(req.content, "lxml")
    find_all_li_tags = soup.find_all("li", class_="nonecate")
    return find_all_li_tags

  def categories_url(url, category_li_tags):
    return list(map(lambda li_tag: url + li_tag.a.get('href'), category_li_tags))

  def categories_id(url, category_li_tags):
    return list(map(lambda li_tag: li_tag.a.get('data-id'), category_li_tags))

  def categories_name(url, category_li_tags):
    return list(map(lambda li_tag: li_tag.a.get_text(strip=True), category_li_tags))

  def save_data_to_excel(default_url, url):
    #TODO: create headers excel
    line = 1
    url_req_category_per_page = "https://www.nhathuocankhang.com/aj/Category/Products"

    li_tags = NhaThuocAnKhang.get_all_url_categories(url)
    categories_id = NhaThuocAnKhang.categories_id(url, li_tags)
    categories_url = NhaThuocAnKhang.categories_url(url, li_tags)
    categories_names = NhaThuocAnKhang.categories_url(url, li_tags)

    for id, item, category_name in zip(categories_id, categories_url, categories_name):
      page_num = 0
      category_id = id

      #TODO: save drugs category per sheet num
      while True:
        form_data = {
          "Key": "",
          "PageSize": "10",
          "PageIndex": page_num,
          "Category": category_id,
        }

        request_drug_group = requests.post(url_req_category_per_page, data=form_data, timeout=10, stream=True, headers=requests.utils.default_headers())

        soup_drug_group = BeautifulSoup(request_drug_group.text, "html.parser")

        if request_drug_group.status_code == 500:
          wb_copy.save(excel_name_file)
          break

        find_drug_ul_tag = soup_drug_group.find("ul", class_="cate")
        find_all_li_tags_from_drug_ul_tag = find_drug_ul_tag.find_all("li", class_="")

        for tag in find_all_li_tags_from_drug_ul_tag:
          get_url_detail_drug = default_url + tag.a.get("href")
          id_drug = get_url_detail_drug.split("?")[1][3:]

          #TODO: product detail
          # https://www.nhathuocankhang.com/thuoc/thuoc-gian-co-waruwari-2mg-100-vien?id=194335

          get_req_detail = requests.get(get_url_detail_drug, timeout=10, stream=True)
          detail_soup = BeautifulSoup(get_req_detail.text, "html.parser")

          info_sell = detail_soup.find("aside", class_="infosell")
          short_desc = info_sell.find("div", class_="shortdesc")

          quy_cach_dong_goi = short_desc.span.get_text().replace("Qui cách đóng gói: ", "")
          ten_thuoc = info_sell.h1.get_text(strip=True)
          print("ten thuoc: ", ten_thuoc)
          print("line", line)
          all_span_short_descs = short_desc.findAll("span")

          slidedetail = detail_soup.find("aside", class_="slidedetail")

          nha_san_xuat = all_span_short_descs[-2].get_text(strip=True).replace("Nhà sản xuất:", "")
          san_xuat_tai = all_span_short_descs[-1].get_text(strip=True).replace("Sản xuất tại", "")

          find_price = info_sell.find("div", class_="price").strong.get_text(strip=True).split("₫")
          gia_ca = int(find_price[0].replace('.', ''))
          print(gia_ca)

          don_vi = info_sell.find("span", class_="unit").get_text(strip=True) # /Viên

          # status item
          tinh_trang_sp = info_sell.find("span", class_="status")
          if tinh_trang_sp is not None:
            tinh_trang_sp = tinh_trang_sp.get_text(strip=True)
          else:
            tinh_trang_sp = None

          # Go to view guide (url information and use drug)
          information_drug_url = default_url + detail_soup.find("a", class_="viewguide").get("href")

          get_info_drug = requests.get(information_drug_url, stream=True, timeout=10)
          soup_info = BeautifulSoup(get_info_drug.text, "html.parser")

          #TODO get product info: https://www.nhathuocankhang.com/thuoc/thuoc-gian-co-waruwari-2mg-100-vien/thong-tin-cach-dung-thuoc?id=194335
          thanh_phan = soup_info.find("strong", string=re.compile(r"Thành phần"))
          thanh_phan = NhaThuocAnKhang.check_presence_find_next_tag_by_find(thanh_phan, "div", "content")

          cong_dung = soup_info.find("strong", string=re.compile(r"Công dụng"))
          cong_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(cong_dung, "div", "content")

          lieu_dung = soup_info.find("strong", string=re.compile(r"Liều dùng"))
          lieu_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(lieu_dung, "div", "content")

          chong_chi_dinh = soup_info.find("span", string=re.compile(r"(Chống chỉ định)"))
          chong_chi_dinh = NhaThuocAnKhang.check_presence_find_next_tag_by_find(chong_chi_dinh, "div", "content")

          luu_y_khi_su_dung = soup_info.find("strong", string=re.compile(r"Lưu ý khi sử dụng"))
          luu_y_khi_su_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(luu_y_khi_su_dung, "div", "content")

          # Tác dụng không mong muốn
          tac_dung_phu = soup_info.find("span", string=re.compile(r"(Tác dụng phụ)"))
          tac_dung_phu = NhaThuocAnKhang.check_presence_find_next_tag_by_find(tac_dung_phu, "div", "content")

          tuong_tac_voi_thuoc_khac = soup_info.find("strong", string=re.compile(r"Tương tác với thuốc khác"))
          tuong_tac_voi_thuoc_khac = NhaThuocAnKhang.check_presence_find_next_tag_by_find(tuong_tac_voi_thuoc_khac, "div", "content")

          bao_quan = soup_info.find("strong", string=re.compile(r"Bảo quản"))
          bao_quan = NhaThuocAnKhang.check_presence_find_next_tag_by_find(bao_quan, "div", "content")

          # đối với người lái xe
          lai_xe = soup_info.find("strong", string=re.compile(r"Lái xe"))
          lai_xe = NhaThuocAnKhang.check_presence_find_next_tag_by_find(lai_xe, "div", "content")

          # # Đóng gói
          dong_goi = soup_info.find("strong", string=re.compile(r"Đóng gói"))
          dong_goi = NhaThuocAnKhang.check_presence_find_next_tag_by_find(dong_goi, "div", "content")

          # Lưu ý đối với người có thai
          thai_ky = soup_info.find("strong", string=re.compile(r"Thai kỳ"))
          thai_ky = NhaThuocAnKhang.check_presence_find_next_tag_by_find(thai_ky, "div", "content")

          # Hạn sử dụng
          han_su_dung = soup_info.find("strong", string=re.compile(r"Hạn dùng"))
          han_su_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(han_su_dung, "div", "content")

          # dược lực học
          duoc_luc_hoc = soup_info.find("strong", string=re.compile(r"Dược lưc học"))
          duoc_luc_hoc = NhaThuocAnKhang.check_presence_find_next_tag_by_find(duoc_luc_hoc, "div", "content")

          # dược động học
          duoc_dong_hoc = soup_info.find("strong", string=re.compile(r"Dược động học"))
          duoc_dong_hoc = NhaThuocAnKhang.check_presence_find_next_tag_by_find(duoc_dong_hoc, "div", "content")

          # đặc điểm
          dac_diem = soup_info.find("strong", string=re.compile(r"Đặc điểm"))
          dac_diem = NhaThuocAnKhang.check_presence_find_next_tag_by_find(dac_diem, "div", "content")

          product_info = (id_drug, get_url_detail_drug, quy_cach_dong_goi, ten_thuoc, category_name, nha_san_xuat, san_xuat_tai, gia_ca, don_vi, tinh_trang_sp, thanh_phan, cong_dung, lieu_dung, chong_chi_dinh, luu_y_khi_su_dung, tac_dung_phu, tuong_tac_voi_thuoc_khac, bao_quan, lai_xe, dong_goi, thai_ky, han_su_dung, duoc_luc_hoc, duoc_dong_hoc, dac_diem)

          ex.save_data_row_to_excel(line_row, product_info, excel_name_file)
          line = line + 1
        page_num = page_num + 1
    dt_end = datetime.now() - dt_now
    print("Its took: {} to done this".format(dt_end))
