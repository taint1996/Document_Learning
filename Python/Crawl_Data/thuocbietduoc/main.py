from init import *
from thuocbietduoc import ThuocBietDuoc as tbd

if __name__ == "__main__":
  excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_thuoc_thuocbietduoc.xls"

  start = timer()
  print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

  #TODO: function save data to excel
  tbd.save_data_to_excel(excel_file_path)

  end = timer()
  print(f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")

  # sheet name wb.sheet_names()
  # all of sheets wb.sheets() -> loop to get sheet