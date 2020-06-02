from init import *
from atc_code import ATCCode

# A -> A01 -> A01A -> A01AB -> [A01AB02, A01AB03]
# Nhom thuoc A ( thuoc duong tieu hoa va chuyen hoa, Tri lieu mat va gan) -> Loai thuoc dung A01A ( che pham nha khoa ) ->  Dieu tri A01AB (Chống nhiễm trùng và sát trùng cho điều trị bằng miệng tại địa phương) -> [A01AB02, A01AB03] (Ten cac loai thuoc lien quan)

# A -> A05 (tri lieu mat va gan) -> A05A (Lieu phap mat) -> A05AX ( Thuoc khac de dieu tri mat) -> [A05AX01, A05AX03] Ten thuoc

# A -> A03 (Thuoc roi loan tieu hoa chuc nang) -> A03C -> None
# A -> [A03, A05] -> A03C -> None

# (nhom thuoc, cach su dung, cong dung thuoc, ten thuoc)

# Danh muc nhom thuoc A: /A: Thuoc duong tieu hoa
# Muc dich su dung thuoc: /A05
# Cong dung thuoc: /A05A
# Cac loai thuoc lien quan: /A05AX
# thuoc: [(ma thuoc: A01AA01, ten thuoc: Sodium floride), A05AX02, A05AX03]

# Nhom thuoc A, Sử dụng cho/ Loại thuốc của, Dùng cho trường hợp (chống nhiễm trùng), Tên các loại thuốc
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
