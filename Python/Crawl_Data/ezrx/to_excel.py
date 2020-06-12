from init import *

class ToExcel:
  def __init__(self, sheet_name, excel_name_file):
    self.sheet_name = sheet_name
    self.excel_name_file = excel_name_file

  def write_row_to_excel(sheet, text_data, row, column):
    sheet.write(row, column, text_data)

  def create_headers_to_excel(headers, sheet_name, excel_name_file):
    wb = xlwt.Workbook(encoding="utf-8", style_compression=0)

    bsheet = wb.add_sheet(sheet_name, cell_overwrite_ok=True)
    style = xlwt.easyxf('align: vert centre, horiz centre; font: bold on')

    for col, header_name in enumerate(headers):
      bsheet.row(0).write(col, header_name, style)
    wb.save(excel_name_file)

  def save_data_row_to_excel(row, data_infos, excel_name_file):
    open_wb = open_workbook(excel_name_file, formatting_info=True)
    wb_copy = xl_copy(open_wb)
    sheet = wb_copy.get_sheet(0)

    for idx, data_info in enumerate(data_infos):
      ToExcel.write_row_to_excel(sheet, data_infos[idx], row, idx)
    wb_copy.save(excel_name_file)