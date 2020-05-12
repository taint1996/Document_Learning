from init import *
from to_excel import ToExcel as to_excel

class DrugList(DrugBank):
  def __init__(self, url):
    super().__init__(self, url)

  def save_drug_list_to_excel(excel_name_file):
    headers_req = requests.utils.default_headers()
    page = 0
    line_row = 1

    total_record = 0
    while True:
      req = requests.get(f"https://drugbank.vn/services/drugbank/api/public/thuoc?page={page}&size=20&isHide=ne(Yes)&sort=tenThuoc,asc&sort=id", stream=True, timeout=20, headers=headers_req)
      drugs = req.json()

      print(f"Go to page {page}")
      if len(drugs) == 0:
        total_record = total_record + len(drugs)
        print(f"Totaly {total_record} record. Ready to Save Excel...")
        break

      # Drug List
      for item in range(len(drugs)):
        drug = drugs[item]
        drug_id = drug["id"]
        ten_thuoc = drug["tenThuoc"]

        so_dang_ky = drug['soDangKy']
        # Image product will add with link 'https://drugbank.vn/api/public/gridfs/{}'.format(drug['images'])
        images = ", ".join(["".join(f"https://drugbank.vn/api/public/gridfs/{img}") for img in drug['images'] if img is not None])

        gia_ke_khai = drug['giaKeKhai'] # request từ https://drugbank.vn/services/drugbank/api/public/gia-ke-khai?sdk={so_dang_ky}&size=10000
          # return list gia ke khai từ các doanh nghiệp vd Cong ty A bán giá xxx đồng/ dvt
          # dongGoi, dvt, giaBan, doanhNghiepSx, doanhNghiepDk, ngayBaoCao

        drug_infos = [drug["id"], drug["tenThuoc"], images, drug['dotPheDuyet'], drug['soQuyetDinh'], drug['pheDuyet'], drug['hieuLuc'], drug['soDangKy'], drug['hoatChat'], drug['phanLoai'], drug['nongDo'], drug['taDuoc'], drug['baoChe'], drug['dongGoi'], drug['tieuChuan'], drug['tuoiTho'], drug['congTySx'], drug['nuocSx'], drug['diaChiSx'], drug['congTyDk'], drug['nuocDk'], drug['diaChiDk'], gia_ke_khai]

        print(f"Save to excel... {drug_id}: {ten_thuoc}")
        super().save_data_row_to_excel(line_row, drug_infos, excel_name_file)

        line_row = line_row + 1
      page = page + 1