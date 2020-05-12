from init import *
from to_excel import ToExcel as to_excel

class DrugBank:
  def __init__(self, url):
    self.url = url

  def save_data_row_to_excel(row, drug_infos, excel_name_file):
    open_wb = open_workbook(excel_name_file, formatting_info=True)
    wb_copy = xl_copy(open_wb)
    sheet = wb_copy.get_sheet(0)

    for i in range(len(drug_infos)):
      to_excel.write_row_to_excel(sheet, drug_infos[i], row, i)
      wb_copy.save(excel_name_file)