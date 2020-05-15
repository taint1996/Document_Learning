# Cơ sở kinh doanh: nhà thuốc
from drug_bank import DrugBank
from init import *
from to_excel import ToExcel as ex

class BusinessFacilities(DrugBank):
  def __init__(self, url):
    super().__init__(self, url)

  def save_data_to_excel(excel_name_file):
    headers_req = requests.utils.default_headers()
    page = 0
    line_row = 1
    total_record = 0

    while True:
      req = requests.get(f"https://drugbank.vn/services/drugbank/api/public/co-so-kinh-doanh?page={page}&size=20&sort=id,desc", stream=True, timeout=20, headers=headers_req)
      soup = BeautifulSoup(req.text, 'html.parser')

      data_infos = req.json()

      print(f"Business Facilities page {page}")
      if not data_infos:
        print(f"Totaly {total_record} Business Facilities. Ready to Save Excel...")
        break

      drugstore_name = ""
      for data in range(len(data_infos)):
        data_info = data_infos[data]

        datas = [ data_info["id"], data_info["title"], drugstore_name.join(f"{data_info['hoDem']} {data_info['ten']}"), data_info["address"], data_info["numberDkkd"], data_info["businessForm"], data_info["businessScope"], data_info["issueDate"], data_info["cchn"], data_info["ngayCapCchn"], data_info["noiCapCchn"], data_info["note"] ]

        print(f"Save to excel... {data_info['id']}: {data_info['title']}")
        ex.save_data_row_to_excel(line_row, datas, excel_name_file)
        line_row = line_row + 1
      page = page + 1
      total_record = total_record + len(data_infos)

if __name__ == "__main__":
  sheet_name = "DrugBank_CoSoKinhDoanh"
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_drugbank_CoSoKinhDoanh.xls"

  headers = ("Id", "Tên nhà thuốc", "Tên chủ nhà thuốc", "Địa chỉ", "Số ĐKKD", "Loại hình kinh doanh", "Hình thức kinh doanh", "Ngày thành lập (Issue Date)",  "CCHN", "Ngày cấp CCHN", "Nơi cấp CCHN")
  ex.create_headers_to_excel(headers, sheet_name, excel_file_path)

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  BusinessFacilities.save_data_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")