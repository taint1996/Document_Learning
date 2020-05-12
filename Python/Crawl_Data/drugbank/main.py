from drug_list import ToExcel as ex, DrugList as dl
from init import *

if __name__ == "__main__":
  sheet_name = "DrugBank_DS_thuoc"
  drug_list_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_drugbank_DS_thuoc.xls"

  headers = ("Id", "Tên thuốc", "Hình ảnh", "Đợt phê duyệt", "Số quyết định", "Phê duyệt", "Hiệu lực", "Số đăng ký", "Hoạt chất", "Phân loại", "Nồng độ", "Tá dược", "Bào chế", "Đóng gói", "Tiêu chuẩn", "HSD", "Cty SX", "Nước SX", "Địa chỉ SX", "Cty DK", "Nước DK", "Địa chỉ DK", "Giá kê khai")
  ex.create_headers_to_excel(headers, sheet_name, drug_list_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  dl.save_drug_list_to_excel(drug_list_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {drug_list_file_path}")