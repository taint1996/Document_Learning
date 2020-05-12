# Cơ sở sản xuất
from drug_bank import DrugBank
from init import *
from to_excel import ToExcel as ex

class ProductionFacilities(DrugBank):
  def __init__(self, url):
    super().__init__(self, url)

  def iteration_and_save_data_to_excel(data_tuple):
    row = 1

    for item in range(len(data_tuple)):
      for idx, val in enumerate(data_tuple[item].values())
        [DrugBank.save_data_row_to_excel(line_row, list(data_tuple[item].values()), excel_name_file)
      row = row + 1

  def save_facilities_to_excel(excel_name_file):
    headers_req = requests.utils.default_headers()
    page = 0
    line_row = 1
    total_record = 0

    while True:
      req = requests.get(f"https://drugbank.vn/services/drugbank/api/public/co-so-san-xuat?page={page}&size=20&sort=id,desc", stream=True, timeout=20, headers=headers_req)
      production_facilities = req.json()

      print(f"Go to page {page}")
      if len(production_facilities) == 0:
        total_record = total_record + len(production_facilities)
        print(f"Totaly {total_record} record. Ready to Save Excel...")
        break

      # Production Facilities
      ProductionFacilities.iteration_and_save_data_to_excel(production_facilities)
      page = page + 1

if __name__ == "__main__":
  sheet_name = "DrugBank_CoSoSanXuat"
  facilities_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_drugbank_CoSoSanXuat.xls"

  headers = ("Id", "Tên Cty", "Tên người", "Bằng cấp/ chứng chỉ", "SĐT", "Địa chỉ Trụ sở chính", "Địa chỉ kinh doanh", "Số điện thoại LH", "Hình thức kinh doanh", "Số ĐKKD", "Ngày ĐKKD", "Hình thức cấp", "DKKD Ban hành bởi", "Phạm vi kinh doanh", "Số GDP", "Ngày GDP", "Ngày hết hạn GDP", "Phạm vị GDP", "Số CCHN", "Ngày CCHN", "CCHN ban hành bởi", "Năm")
  ex.create_headers_to_excel(headers, sheet_name, facilities_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  ProductionFacilities.save_facilities_to_excel(facilities_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {facilities_file_path}")