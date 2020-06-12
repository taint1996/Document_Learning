from init import *
from atc_code import ATCCode

# Danh muc nhom thuoc A: /A: Thuoc duong tieu hoa
# Cate 1: /A05
# Cate 2: /A05A
# Cate 3: /A05AX
# thuoc: [(ma thuoc: A01AA01, ten thuoc: Sodium floride), A05AX02, A05AX03]

# save to excel: A-Alimentary tract and metabolisma, A01A-Stomatological preparations, A01AA - Caries prophylactic agents, (A01AA01-Sodium fluoride, A01AA02-Sodium monofluorophosphate)

if __name__ == "__main__":
    sheet_name = "ATC Code"
    excel_file_path = f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}_ATC_Code.xls"

    headers = ("Nhóm thuốc bậc 1", "Nhóm thuốc bậc 2", "Nhóm thuốc bậc 3",
               "Nhóm thuốc bậc 4", "Tên các loại thuốc")

    ex.create_excel_file_with_headers(headers, sheet_name, excel_file_path)

    start = timer()
    print(f"Start crawling at {datetime.now().strftime('%A %H:%M:%S')}")

    ATCCode.data_atc_code(excel_file_path)

    end = timer()
    print(
        f"Finished Crawling Data at: {timedelta(seconds=end-start)} and save to file {excel_file_path}")
