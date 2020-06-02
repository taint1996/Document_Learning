from init import *
from to_excel import ToExcel as ex
from drug_bank import DrugBank

class DrugList(DrugBank):
  def __init__(self, url):
    DrugBank.__init__(self, url)

  def request_drug_list(page):
    req = requests.get(f"https://drugbank.vn/services/drugbank/api/public/thuoc?page={page}&size=20&isHide=ne(Yes)&sort=tenThuoc,asc&sort=id", stream=True, timeout=20)
    return req.json()

  def save_drug_list_to_excel(excel_name_file):
    headers_req = requests.utils.default_headers()
    page = 0
    line_row = 1
    drugs_data = []
    url_drug_list = "https://drugbank.vn/danh-sach-thuoc"

    total_record = 0
    while True:
      drugs = DrugList.request_drug_list(page)

      if len(drugs) == 0:
        print(f"----- Total {total_record} record")
        break

      for drug in drugs:
        drugs_data.append(drug)

      print(f"===== Go to page {page}")
      print(f"----- Total {total_record} record")
      total_record = len(drugs_data)
      page = page + 1

    # Drug List
    for idx, data in enumerate(drugs_data):
      drug = drugs_data[idx]

      so_dang_ky = data['soDangKy']
      images = ", ".join(["".join(f"https://drugbank.vn/api/public/gridfs/{img}") for img in data['images'] if img is not None])

      # return list gia ke khai từ các doanh nghiệp vd Cong ty A bán giá xxx đồng/ dvt
        # dongGoi, dvt, giaBan, doanhNghiepSx, doanhNghiepDk, ngayBaoCao
      try:
        req_product_detail = requests.get(f"https://drugbank.vn/services/drugbank/api/public/gia-ke-khai?sdk={so_dang_ky}&size=10000", stream=True, timeout=20, headers=headers_req)
      except requests.exceptions.ConnectionError as e:
        continue
      except requests.exceptions.Timeout as e:
        print(f">>>> Requests Timeout {e}. Try to connect again")
        req_product_detail = requests.get(f"https://drugbank.vn/services/drugbank/api/public/gia-ke-khai?sdk={so_dang_ky}&size=10000", stream=True, timeout=20, headers=headers_req)
      except requests.exceptions.RequestException as e:
        raise SystemExit(e)
        continue

      product_detail = req_product_detail.json()
      business_package = ""
      price = ""

      if len(product_detail) != 0:
        price = ", ".join(["".join(f"{p['ngayBaoCao']}: {p['doanhNghiepDk']} bán giá {p['giaBan']}đ/{p['dvt']}") for p in product_detail])
        business_package = ", ".join(["".join(f"{p['doanhNghiepDk']} đóng gói: {p['dongGoi']}") for p in product_detail])

      drug_infos = [data["id"], data["tenThuoc"], images, data['dotPheDuyet'], data['soQuyetDinh'], data['pheDuyet'], data['hieuLuc'], so_dang_ky, data['hoatChat'], data['phanLoai'], data['nongDo'], data['taDuoc'], data['baoChe'], data['dongGoi'], data['tieuChuan'], data['tuoiTho'], data['congTySx'], data['nuocSx'], data['diaChiSx'], data['congTyDk'], data['nuocDk'], data['diaChiDk'], price, business_package]

      print(f"Save to excel... {drug['id']}: {drug['tenThuoc']}")
      ex.save_data_row_to_excel(line_row, drug_infos, excel_name_file)
      line_row = line_row + 1

if __name__ == "__main__":
  sheet_name = "DrugBank_DS_thuoc"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_drugbank_DS_thuoc.xls"

  headers_drug_list = ("Id", "Tên thuốc", "Hình ảnh", "Đợt phê duyệt", "Số quyết định", "Phê duyệt", "Hiệu lực", "Số đăng ký", "Hoạt chất", "Phân loại", "Nồng độ", "Tá dược", "Bào chế", "Đóng gói", "Tiêu chuẩn", "HSD", "Cty SX", "Nước SX", "Địa chỉ SX", "Cty DK", "Nước DK", "Địa chỉ DK", "Giá", "Doanh nghiệp đóng gói")
  ex.create_headers_to_excel(headers_drug_list, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  DrugList.save_drug_list_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")