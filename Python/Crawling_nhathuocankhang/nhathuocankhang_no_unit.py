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

class NhaThuocAnKhang:
  def __init__(self, url, post_url = "", name = ""):
    self.url = url
    self.post_url = post_url
    self.name = name

  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def check_presence_find_next_tag_by_find(tag, tag_name = "", classname = ""):
    if tag is None:
      tag = ""
    else:
      tag = tag.find_next(tag_name, class_=classname).get_text(strip=True)
    return tag

  def request_get_ntak(url):
    req = requests.get(url, timeout=10, stream=True)
    soup = BeautifulSoup(req.text, "html.parser")
    li_tags = soup.find_all("li", class_="nonecate")
    return li_tags

  def crawling_nhathuocankhang(default_url, url):
    sheet_name = "nha-thuoc-ankhang"
    excel_name_file = "nhathuocankhang-no-unit.xls"
    ExcelCrawlData.create_headers_to_excel(sheet_name, excel_name_file)

    line = 1
    url_req_post = "https://www.nhathuocankhang.com/aj/Category/Products"

    li_tags = NhaThuocAnKhang.request_get_ntak(url)
    for item in li_tags:
      page_idx = 0
      a_tag = item.a
      print(a_tag)
      data_id = a_tag["data-id"]

      open_wb = open_workbook(excel_name_file, formatting_info=True)
      wb_copy = xl_copy(open_wb)
      sheet = wb_copy.get_sheet(0)
      while True:
        headers_req = requests.utils.default_headers()

        form_data = {
          "Key": "",
          "PageSize": "10",
          "PageIndex": page_idx,
          "Category": data_id,
        }

        request_drug_group = requests.post(url_req_post, data=form_data, timeout=10, stream=True, headers=headers_req)

        soup_drug_group = BeautifulSoup(request_drug_group.text, "html.parser")

        if request_drug_group.status_code == 500:
          wb_copy.save(excel_name_file)
          break

        find_drug_ul_tag = soup_drug_group.find("ul", class_="cate")
        find_all_li_tags_from_drug_ul_tag = find_drug_ul_tag.find_all("li", class_="")

        for tag in find_all_li_tags_from_drug_ul_tag:
          get_url_detail_drug = default_url + tag.a.get("href")
          id_drug = get_url_detail_drug.split("?")[1][3:]

          NhaThuocAnKhang.write_row_to_excel(sheet, id_drug, line, 0)
          NhaThuocAnKhang.write_row_to_excel(sheet, get_url_detail_drug, line, 1)

          get_req_detail = requests.get(get_url_detail_drug, timeout=10, stream=True)
          detail_soup = BeautifulSoup(get_req_detail.text, "html.parser")

          info_sell = detail_soup.find("aside", class_="infosell")
          short_desc = info_sell.find("div", class_="shortdesc")

          qui_cach_dong_goi = short_desc.span.get_text().replace("Qui cách đóng gói: ", "")
          NhaThuocAnKhang.write_row_to_excel(sheet, qui_cach_dong_goi, line, 7)
          ten_thuoc = info_sell.h1.get_text(strip=True)
          NhaThuocAnKhang.write_row_to_excel(sheet, ten_thuoc, line, 2)
          print("ten thuoc: ", ten_thuoc)
          print("line", line)
          all_span_short_descs = short_desc.findAll("span")
          nhom_thuoc = a_tag.get_text(strip=True)
          NhaThuocAnKhang.write_row_to_excel(sheet, nhom_thuoc, line, 6)

          slidedetail = detail_soup.find("aside", class_="slidedetail")

          nha_san_xuat = all_span_short_descs[-2].get_text(strip=True).replace("Nhà sản xuất:", "")
          NhaThuocAnKhang.write_row_to_excel(sheet, nha_san_xuat, line, 8)
          san_xuat_tai = all_span_short_descs[-1].get_text(strip=True).replace("Sản xuất tại", "")
          NhaThuocAnKhang.write_row_to_excel(sheet, san_xuat_tai, line, 9)

          gia_ca = info_sell.find("div", class_="price").strong.get_text(strip=True) + info_sell.find("span", class_="unit").get_text(strip=True)

          NhaThuocAnKhang.write_row_to_excel(sheet, gia_ca, line, 3)
          print(gia_ca)

          # status item
          tinh_trang_sp = info_sell.find("span", class_="status")
          if tinh_trang_sp is not None:
            tinh_trang_sp = tinh_trang_sp.get_text(strip=True)
          else:
            tinh_trang_sp = None
          NhaThuocAnKhang.write_row_to_excel(sheet, tinh_trang_sp, line, 10)

          # Go to view guide (url information and use drug)
          information_drug_url = default_url + detail_soup.find("a", class_="viewguide").get("href")

          get_info_drug = requests.get(information_drug_url, stream=True, timeout=10)
          soup_info = BeautifulSoup(get_info_drug.text, "html.parser")

          thanh_phan = soup_info.find("strong", string="Thành phần")
          thanh_phan = NhaThuocAnKhang.check_presence_find_next_tag_by_find(thanh_phan, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, thanh_phan, line, 11)

          cong_dung = soup_info.find("strong", string="Công dụng")
          cong_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(cong_dung, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, cong_dung, line, 12)

          lieu_dung = soup_info.find("strong", string="Liều dùng")
          lieu_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(lieu_dung, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, lieu_dung, line, 13)

          chong_chi_dinh = soup_info.find("span", string="(Chống chỉ định)")
          chong_chi_dinh = NhaThuocAnKhang.check_presence_find_next_tag_by_find(chong_chi_dinh, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, chong_chi_dinh, line, 14)

          luu_y_khi_su_dung = soup_info.find("strong", string="Lưu ý khi sử dụng")
          luu_y_khi_su_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(luu_y_khi_su_dung, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, luu_y_khi_su_dung, line, 15)

          # Tác dụng không mong muốn
          tac_dung_phu = soup_info.find("span", string="(Tác dụng phụ)")
          tac_dung_phu = NhaThuocAnKhang.check_presence_find_next_tag_by_find(tac_dung_phu, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, tac_dung_phu, line, 16)

          tuong_tac_voi_thuoc_khac = soup_info.find("strong", string="Tương tác với thuốc khác")
          tuong_tac_voi_thuoc_khac = NhaThuocAnKhang.check_presence_find_next_tag_by_find(tuong_tac_voi_thuoc_khac, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, tuong_tac_voi_thuoc_khac, line, 17)

          bao_quan = soup_info.find("strong", string="Bảo quản")
          bao_quan = NhaThuocAnKhang.check_presence_find_next_tag_by_find(bao_quan, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, bao_quan, line, 18)

          # đối với người lái xe
          lai_xe = soup_info.find("strong", string="Lái xe")
          lai_xe = NhaThuocAnKhang.check_presence_find_next_tag_by_find(lai_xe, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, lai_xe, line, 19)

          # # Đóng gói
          dong_goi = soup_info.find("strong", string="Đóng gói")
          dong_goi = NhaThuocAnKhang.check_presence_find_next_tag_by_find(dong_goi, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, dong_goi, line, 20)

          # Lưu ý đối với người có thai
          thai_ky = soup_info.find("strong", string="Thai kỳ")
          thai_ky = NhaThuocAnKhang.check_presence_find_next_tag_by_find(thai_ky, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, thai_ky, line, 21)

          # Hạn sử dụng
          han_su_dung = soup_info.find("strong", string="Hạn dùng")
          han_su_dung = NhaThuocAnKhang.check_presence_find_next_tag_by_find(han_su_dung, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, han_su_dung, line, 22)

          # dược lực học
          duoc_luc_hoc = soup_info.find("strong", string="Dược lưc học")
          duoc_luc_hoc = NhaThuocAnKhang.check_presence_find_next_tag_by_find(duoc_luc_hoc, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, duoc_luc_hoc, line, 23)

          # dược động học
          duoc_dong_hoc = soup_info.find("strong", string="Dược động học")
          duoc_dong_hoc = NhaThuocAnKhang.check_presence_find_next_tag_by_find(duoc_dong_hoc, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, duoc_dong_hoc, line, 24)

          # đặc điểm
          dac_diem = soup_info.find("strong", string="Đặc điểm")
          dac_diem = NhaThuocAnKhang.check_presence_find_next_tag_by_find(dac_diem, "div", "content")
          NhaThuocAnKhang.write_row_to_excel(sheet, dac_diem, line, 25)
          line = line + 1
        page_idx = page_idx + 1
    dt_end = datetime.now() - dt_now
    print("Its took: {} to done this".format(dt_end))


class ExcelCrawlData:
  def create_headers_to_excel(sheet_name, excel_name_file):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    headers = ("id", "url", "ten_thuoc", "gia_ca", "don_vi", "img", "nhom_thuoc", "qui_cach_dong_goi", "nha_san_xuat", "san_xuat_tai", "tinh_trang_sp", "thanh_phan", "cong_dung", "lieu_dung", "chong_chi_dinh", "luu_y_khi_su_dung", "tac_dung_phu", "tuong_tac_voi_thuoc_khac", "bao_quan", "lai_xe", "dong_goi", "thai_ky", "han_su_dung", "duoc_luc_hoc", "duoc_dong_hoc", "dac_diem")
    bsheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      bsheet.row(0).write(col, header_name, style)
    book.save(excel_name_file)

##### Get urls href base on navbar index page
# url = "https://www.nhathuocankhang.com/thuoc"

print(">>>>>>>>>>>>>>>>>> Here We Go ")
from datetime import datetime

dt_now = datetime.now()
print("Start at: {}".format(dt_now))

################################### All Drug Group ###################################
###################### Auto run script
# from datetime import datetime
# from threading import Timer

# x=datetime.today()
# y=x.replace(day=x.day, hour=11, minute=8, second=0, microsecond=0)
# delta_t=y-x

# secs=delta_t.seconds+1

default_url = "https://www.nhathuocankhang.com"
url = "https://www.nhathuocankhang.com/thuoc"

NhaThuocAnKhang.crawling_nhathuocankhang(default_url, url)
# t = Timer(secs, NhaThuocAnKhang.crawling_nhathuocankhang)
# t.start()
####################################

