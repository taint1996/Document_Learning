# Cơ sở phân phói
from drug_bank import DrugBank
from init import *
from to_excel import ToExcel as ex

class DistributionFacilities(DrugBank):
  def __init__(self, url):
    super().__init__(self, url)

  def save_facilities_to_excel(excel_name_file):
    headers_req = requests.utils.default_headers()
    page = 0
    line_row = 1
    total_record = 0

    while True:
      req = requests.get(f"https://drugbank.vn/services/drugbank/api/public/co-so-phan-phoi?page={page}&size=20&sort=id,desc", stream=True, timeout=20, headers=headers_req)
      production_facilities = req.json()

      print(f"Go to page {page}")
      if not production_facilities:
        print(f"Totaly {total_record} record saved to Excel...")
        break

      # Production Facilities
      for data in range(len(production_facilities)):
        data_info = production_facilities[data]

        data_infos = [data_info["id"], data_info["title"], data_info["businessForm"], data_info["phoneContact"], data_info["businessAddress"], data_info["address"], data_info["numberDkkd"], data_info["dkkdDate"], data_info["dkkdIssuedBy"], data_info["businessScope"], data_info["numberGdp"], data_info["gdpDate"], data_info["expirationGdpDate"], data_info["responseLevel"], data_info["numberCCHN"], data_info["cchnDate"], data_info["cchnIssuedBy"], data_info["year"], data_info["note"]]

        print(f"Save to excel... {data_info['id']}: {data_info['title']}")
        ex.save_data_row_to_excel(line_row, data_infos, excel_name_file)
        line_row = line_row + 1
      total_record = total_record + len(production_facilities)
      page = page + 1

if __name__ == "__main__":
  sheet_name = "DrugBank_CoSoPhanPhoi"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_drugbank_CoSoPhanPhoi.xls"

  headers = ("id", "Tên cơ sở", "Loại hình kinh doanh (Business Form)", "SĐT Liên hệ", "Địa chỉ trụ sở chính", "Địa chỉ chi nhánh", "Số ĐKKD", "Ngày ĐKKD", "ĐKKD cấp bởi", "Phạm vi kinh doanh (Business Scope)", "Số GDP", "Ngày GDP", "Ngày hết hạn GDP", "Mức độ đáp ứng (Response Level)", "Số chứng chỉ hành nghề", "Ngày CCHN", "CCHN cấp bởi", "Năm", "Ghi chú")

  ex.create_headers_to_excel(headers, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  DistributionFacilities.save_facilities_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")