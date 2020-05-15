from init import *
from erzx import ERZX

if __name__ == "__main__":
  sheet_name = "Danh sách thuốc"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_ERZX_DS_Thuoc.xls"

  headers_drug_list = ("Sản phẩm", "Hãng sản xuất", "Thành tiền")
  ex.create_headers_to_excel(headers_drug_list, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  ERZX.save_data_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")
