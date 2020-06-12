from nhathuocankhang import NhaThuocAnKhang as ntak
from init import *
from to_excel import ToExcel as ex

if __name__ == "__main__":
  sheet_name = "DrugList"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_nhathuocankhang_DS_thuoc.xls"

  headers = ("ID Nhóm Thuốc", "Category URL", "Tên nhóm thuốc", "Tên thuốc", "URL thuốc", "Giá lẻ", "Giá sỉ", "Quy cách đóng gói", "Tên thành phần thuốc", "Nhà sản xuất", "Sản xuất tại", "Thành phần thuốc", "Công dụng", "Liều dùng", "Lưu ý khi sử dụng", "Chống chỉ định", "Tác dụng phụ", "Tương tác với thuốc khác", "Bảo quản", "Lái xe", "Đóng gói", "Thai kỳ", "HSD", "Dược lực học", "Dược động học", "Dược lý", "Đặc điểm")

  print(f">>>> Len Headers Excel {len(headers)}")

  ex.create_excel_file_with_headers(headers, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  ntak.save_data_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")