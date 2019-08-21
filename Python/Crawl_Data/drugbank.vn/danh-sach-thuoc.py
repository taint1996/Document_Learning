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

class DrugBank:
  def crawling_drug_list():
    while req:
      for drug in req.json():
        drug_id = drug["id"]
        images = drug['images']
        ten_thuoc = drug["tenThuoc"]

        dot_phe_duyet = drug['dotPheDuyet']
        so_quyet_dinh = drug['soQuyetDinh']
        phe_duyet = drug['pheDuyet']
        hieu_luc = drug['hieuLuc']
        so_dang_ky = drug['soDangKy']

        hoat_chat = drug['hoatChat']
        phan_loai = drug['phanLoai']
        nong_do = drug['nongDo']
        ta_duoc = drug['taDuoc']
        bao_che = drug['baoChe']
        dong_goi = drug['dongGoi']
        tieu_chuan = drug['tieuChuan']
        tuoi_tho = drug['tuoiTho']

        cong_ty_SX = drug['congTySx']
        nuoc_SX = drug['nuocSx']
        dia_chi_SX = drug['diaChiSx']

        cong_ty_DK = drug['congTyDk']
        nuoc_DK = drug['nuocDk']
        dia_chi_DK = drug['diaChiDk']

        gia_ke_khai = drug['giaKeKhai']

        huong_dan_su_dung = drug['huongDanSuDung']
        huong_dan_su_dung_Bn = drug['huongDanSuDungBn']
        ten = drug['ten']

        print('==============={s} {s} {s}', drug_id, ten_thuoc)

      pageload['page'] = pageload['page'] + 1
      print(pageload)
      req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc", timeout=20, stream=True, params=pageload, json=pageload, headers=headers_req)

      print("Go here?")

      if len(req.json()) == 0:
        break

  def crawling_danh_sach_thuoc():
    sheet_name = "danh-sach-thuoc"
    excel_name_file = "drugbank_danh_sach_thuoc.xls"

    ExcelCrawlData.create_headers_to_excel(sheet_name, excel_name_file)

    pageload = { "page": 0, "size": 20, "sort": "tenThuoc,asc", "sort": "id" }
    headers_req = requests.utils.default_headers()

    req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc", timeout=20, stream=True, params=pageload, json=pageload, headers=headers_req)

    line = 1

    while req:
      for drug in req.json():
        drug_id = drug["id"]
        DrugBank.write_row_to_excel(sheet, drug_id, line, 0)
        images = drug['images']
        DrugBank.write_row_to_excel(sheet, images, line, 1)
        ten_thuoc = drug["tenThuoc"]
        DrugBank.write_row_to_excel(sheet, ten_thuoc, line, 2)

        dot_phe_duyet = drug['dotPheDuyet']
        DrugBank.write_row_to_excel(sheet, dot_phe_duyet, line, 3)
        so_quyet_dinh = drug['soQuyetDinh']
        DrugBank.write_row_to_excel(sheet, so_quyet_dinh, line, 4)
        phe_duyet = drug['pheDuyet']
        DrugBank.write_row_to_excel(sheet, phe_duyet, line, 5)
        hieu_luc = drug['hieuLuc']
        DrugBank.write_row_to_excel(sheet, hieu_luc, line, 6)
        so_dang_ky = drug['soDangKy']
        DrugBank.write_row_to_excel(sheet, so_dang_ky, line, 7)

        hoat_chat = drug['hoatChat']
        DrugBank.write_row_to_excel(sheet, hoat_chat, line, 8)
        phan_loai = drug['phanLoai']
        DrugBank.write_row_to_excel(sheet, phan_loai, line, 9)
        nong_do = drug['nongDo']
        DrugBank.write_row_to_excel(sheet, nong_do, line, 10)
        ta_duoc = drug['taDuoc']
        DrugBank.write_row_to_excel(sheet, ta_duoc, line, 11)
        bao_che = drug['baoChe']
        DrugBank.write_row_to_excel(sheet, bao_che, line, 12)
        dong_goi = drug['dongGoi']
        DrugBank.write_row_to_excel(sheet, dong_goi, line, 13)
        tieu_chuan = drug['tieuChuan']
        DrugBank.write_row_to_excel(sheet, tieu_chuan, line, 14)
        tuoi_tho = drug['tuoiTho']
        DrugBank.write_row_to_excel(sheet, tuoi_tho, line, 15)

        cong_ty_SX = drug['congTySx']
        DrugBank.write_row_to_excel(sheet, cong_ty_SX, line, 16)
        nuoc_SX = drug['nuocSx']
        DrugBank.write_row_to_excel(sheet, nuoc_SX, line, 17)
        dia_chi_SX = drug['diaChiSx']
        DrugBank.write_row_to_excel(sheet, dia_chi_SX, line, 18)

        cong_ty_DK = drug['congTyDk']
        DrugBank.write_row_to_excel(sheet, cong_ty_DK, line, 19)
        nuoc_DK = drug['nuocDk']
        DrugBank.write_row_to_excel(sheet, nuoc_DK, line, 20)
        dia_chi_DK = drug['diaChiDk']
        DrugBank.write_row_to_excel(sheet, dia_chi_DK, line, 21)

        gia_ke_khai = drug['giaKeKhai']
        DrugBank.write_row_to_excel(sheet, gia_ke_khai, line, 22)

        huong_dan_su_dung = drug['huongDanSuDung']
        DrugBank.write_row_to_excel(sheet, huong_dan_su_dung, line, 23)
        huong_dan_su_dung_Bn = drug['huongDanSuDungBn']
        DrugBank.write_row_to_excel(sheet, huong_dan_su_dung_Bn, line, 24)
        ten = drug['ten']
        DrugBank.write_row_to_excel(sheet, ten, line, 25)

        book.save("drugbank_danh_sach_thuoc.xls")
        line = line + 1
        print('==============={s} {s} ---- row {s}', drug_id, ten_thuoc, line)

      pageload['page'] = pageload['page'] + 1
      print(pageload)
      req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc", timeout=20, stream=True, params=pageload, json=pageload, headers=headers_req)

      if len(req.json()) == 0:
        break

# req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc?page=0&size=20&sort=tenThuoc,asc&sort=id", timeout=20, stream=True, json=pageload, headers=headers_req)

class ExcelCrawlData:
  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def create_headers_to_excel(sheet_name, excel_name_file):
    ####################################### Create file Excel ##################################
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    ws = book.add_sheet(sheet_name, cell_overwrite_ok=True)

    headers = ("id", "images", "ten_thuoc", "dot_phe_duyet", "so_quyet_dinh", "phe_duyet", "hieu_luc", "so_dang_ky", "hoat_chat", "phan_loai", "nong_do", "ta_duoc", "bao_che", "dong_goi", "tieu_chuan", "tuoi_tho", 'cong_ty_SX', 'nuoc_SX', 'dia_chi_SX', 'cong_ty_DK', 'nuoc_DK', 'dia_chi_DK', 'gia_ke_khai', 'huong_dan_su_dung', 'huong_dan_su_dung_Bn', 'ten')

    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      ws.row(0).write(col, header_name, style)

    book.save(excel_name_file)

pageload = { "page": 0, "size": 20, "sort": "tenThuoc,asc", "sort": "id" }
headers_req = requests.utils.default_headers()

req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc", timeout=20, stream=True, params=pageload, json=pageload, headers=headers_req)

sheet_name = "danh-sach-thuoc"
excel_name_file = "drugbank_danh_sach_thuoc.xls"

ExcelCrawlData.create_headers_to_excel(sheet_name, excel_name_file)

# open_wb = open_workbook(excel_name_file, formatting_info=True)
# wb_copy = xl_copy(open_wb)
# sheet = wb_copy.get_sheet(0)

line = 1
while req:
  open_wb = open_workbook(excel_name_file, formatting_info=True)
  wb_copy = xl_copy(open_wb)
  sheet = wb_copy.get_sheet(0)

  for drug in req.json():
    print("line for loop", line)
    drug_id = drug["id"]
    ExcelCrawlData.write_row_to_excel(sheet, drug_id, line, 0)
    images = drug['images']
    if not (images is None):
      images = ""

    ExcelCrawlData.write_row_to_excel(sheet, images, line, 1)
    ten_thuoc = drug["tenThuoc"]
    ExcelCrawlData.write_row_to_excel(sheet, ten_thuoc, line, 2)

    dot_phe_duyet = drug['dotPheDuyet']
    ExcelCrawlData.write_row_to_excel(sheet, dot_phe_duyet, line, 3)
    so_quyet_dinh = drug['soQuyetDinh']
    ExcelCrawlData.write_row_to_excel(sheet, so_quyet_dinh, line, 4)
    phe_duyet = drug['pheDuyet']
    ExcelCrawlData.write_row_to_excel(sheet, phe_duyet, line, 5)
    hieu_luc = drug['hieuLuc']
    ExcelCrawlData.write_row_to_excel(sheet, hieu_luc, line, 6)
    so_dang_ky = drug['soDangKy']
    ExcelCrawlData.write_row_to_excel(sheet, so_dang_ky, line, 7)

    hoat_chat = drug['hoatChat']
    ExcelCrawlData.write_row_to_excel(sheet, hoat_chat, line, 8)
    phan_loai = drug['phanLoai']
    ExcelCrawlData.write_row_to_excel(sheet, phan_loai, line, 9)
    nong_do = drug['nongDo']
    ExcelCrawlData.write_row_to_excel(sheet, nong_do, line, 10)
    ta_duoc = drug['taDuoc']
    ExcelCrawlData.write_row_to_excel(sheet, ta_duoc, line, 11)
    bao_che = drug['baoChe']
    ExcelCrawlData.write_row_to_excel(sheet, bao_che, line, 12)
    dong_goi = drug['dongGoi']
    ExcelCrawlData.write_row_to_excel(sheet, dong_goi, line, 13)
    tieu_chuan = drug['tieuChuan']
    ExcelCrawlData.write_row_to_excel(sheet, tieu_chuan, line, 14)
    tuoi_tho = drug['tuoiTho']
    ExcelCrawlData.write_row_to_excel(sheet, tuoi_tho, line, 15)

    cong_ty_SX = drug['congTySx']
    ExcelCrawlData.write_row_to_excel(sheet, cong_ty_SX, line, 16)
    nuoc_SX = drug['nuocSx']
    ExcelCrawlData.write_row_to_excel(sheet, nuoc_SX, line, 17)
    dia_chi_SX = drug['diaChiSx']
    ExcelCrawlData.write_row_to_excel(sheet, dia_chi_SX, line, 18)

    cong_ty_DK = drug['congTyDk']
    ExcelCrawlData.write_row_to_excel(sheet, cong_ty_DK, line, 19)
    nuoc_DK = drug['nuocDk']
    ExcelCrawlData.write_row_to_excel(sheet, nuoc_DK, line, 20)
    dia_chi_DK = drug['diaChiDk']
    ExcelCrawlData.write_row_to_excel(sheet, dia_chi_DK, line, 21)

    gia_ke_khai = drug['giaKeKhai']
    ExcelCrawlData.write_row_to_excel(sheet, gia_ke_khai, line, 22)

    huong_dan_su_dung = drug['huongDanSuDung']
    ExcelCrawlData.write_row_to_excel(sheet, huong_dan_su_dung, line, 23)
    huong_dan_su_dung_Bn = drug['huongDanSuDungBn']
    ExcelCrawlData.write_row_to_excel(sheet, huong_dan_su_dung_Bn, line, 24)
    ten = drug['ten']
    ExcelCrawlData.write_row_to_excel(sheet, ten, line, 25)

    line = line + 1
    print('==============={s} {s} ---- row {s}', drug_id, ten_thuoc, line)
    wb_copy.save(excel_name_file)

  pageload['page'] = pageload['page'] + 1
  print(pageload)
  req = requests.get("https://www.drugbank.vn/services/drugbank/api/public/thuoc", timeout=20, stream=True, params=pageload, json=pageload, headers=headers_req)

  if len(req.json()) == 0:
    break
