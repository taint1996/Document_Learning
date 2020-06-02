# Cơ sở sản xuất
from drug_bank import DrugBank
from init import *
from to_excel import ToExcel as ex
from drug_list import DrugList

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