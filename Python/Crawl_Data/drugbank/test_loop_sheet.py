import xlrd
import xlwt
from xlutils.copy import copy
import os

file_path = "09-05-2020_165815_drugbank_DS_thuoc.xls"

wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)
for row_num in range(sheet.nrows):
    row_value = sheet.row_values(row_num)

    if row_value[1] == 'Bisoplus Stada 5mg/12.5 mg':
      print("Go to continue")
      continue


# sheet_by_index = open_wb.sheet_by_index(0)
# for row_num in range(sheet_by_index.nrows):
#   row_value = sheet_by_index.row_values(row_num)

#   if row_value[1] != ten_thuoc: # nếu tên sp trong file excel có chứa tên thuốc -> next
#     DrugList.save_data_row_to_excel(wb_copy, sheet, drug_infos, line, excel_name_file)