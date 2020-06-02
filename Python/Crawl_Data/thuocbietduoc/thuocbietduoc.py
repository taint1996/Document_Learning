from init import *
from to_excel import ToExcel as ex

# TODO: Build class and refactor code

class ThuocBietDuoc:
    def __init__(self, url):
        self.url = url

    def find_article_product_detail(product_url):
        global req_detail

        try:
            req_detail = s.get(product_url, timeout=20, stream=True,
                               headers=requests.utils.default_headers())
        except requests.exceptions.ConnectionError as e:
            pass
        except requests.exceptions.Timeout as e:
            print(f">>>> Requests Timeout {e}. Try to connect again")
            req_detail = s.get(product_url, timeout=20, stream=True,
                               headers=requests.utils.default_headers())
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
            pass

        soup_detail = BeautifulSoup(req_detail.content, "lxml")
        return soup_detail.find("article")

    def get_all_a_tag_categories(drug_url):
        global req_idx

        try:
            req_idx = s.get(drug_url, stream=True, timeout=20)
        except requests.exceptions.ConnectionError as e:
            pass
        except requests.exceptions.Timeout as e:
            print(f">>>> Requests Timeout {e}. Try to connect again")
            req_idx = s.get(drug_url, stream=True, timeout=20)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
            pass

        soup = BeautifulSoup(req_idx.content, 'lxml')

        find_left_category_drug = soup.find('div', id='neo-left-drug')
        return find_left_category_drug.find_all('a', class_="textpldl")

    def get_category_infos(category_a_tags):
        category_urls = []
        category_names = []

        for category in category_a_tags:
            category_urls.append(category.get(
                'href').strip().replace('..', url))
            category_names.append(category.get('title').strip())
        return (category_urls, category_names)

    def get_product_url(drug_name_title):
        return drug_name_title.a.get('href').strip().replace('..', url)

    def find_product_detail_by_string(soup_product_detail, string_name=""):
        find_string_name = soup_product_detail.find(class_=re.compile(
            r'textdetailhead'), string=re.compile(r"{}".format(string_name)))

        if not find_string_name:
            record = ""
        else:
            record = find_string_name.find_next_sibling().get_text(strip=True)
        return record

    def get_product_info(soup_product_detail, product_url):
        # Tên thuốc
        find_title = soup_product_detail.find('h1', class_="drugtitle")
        ten_thuoc = find_title.get_text(strip=True) if find_title else ""

        nhom_thuoc = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Nhóm thuốc")

        print(f">>>>>>>>>>> Product {ten_thuoc}")

        # img
        # go to detail src='https://img.thuocbietduoc.com.vn/images/drugs/anh-thuoc-3.jpg': Waiting image -> return ""
        find_img = soup_product_detail.find("img", class_="imgdrg_lst")
        img = find_img.get("src").strip(
        ) if not find_img or "anh-thuoc" in find_img.get('src') else ""

        # Thông tin thành phần thuốc
        dang_bao_che = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Dạng bào chế")
        dong_goi = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Đóng gói")
        thanh_phan = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Thành phần")
        so_dang_ky = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Số đăng ký")
        nha_san_xuat = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Nhà sản xuất")
        nha_dang_ky = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Nhà đăng ký")
        nha_phan_phoi = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Nhà phân phối")

        chi_dinh = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Chỉ định")
        doituong_sudung = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Đối tượng sử dụng")

        lieuluong_cachdung = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Liều lượng - cách dùng")
        cach_dung = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Cách dùng")

        chong_chi_dinh = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Chống chỉ định")
        chu_y_de_phong = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Chú ý đề phòng")

        duoc_luc = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Dược lực")
        duoc_dong_hoc = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Dược động học")
        tac_dung = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Tác dụng")
        tac_dung_phu = ThuocBietDuoc.find_product_detail_by_string(
            soup_product_detail, "Tác dụng phụ")

        return (ten_thuoc, product_url, img, nhom_thuoc, dang_bao_che, dong_goi, thanh_phan, so_dang_ky, nha_san_xuat, nha_dang_ky, nha_phan_phoi, chi_dinh, doituong_sudung, lieuluong_cachdung, cach_dung, chong_chi_dinh, chu_y_de_phong, duoc_luc, duoc_dong_hoc, tac_dung, tac_dung_phu)

    def save_data_to_excel(excel_name_file):
        # req get drug_url to get all a tag category drugs from div #neo-left-drug
        category_a_tags = ThuocBietDuoc.get_all_a_tag_categories(drug_url)

        category_urls = ThuocBietDuoc.get_category_infos(category_a_tags)[0]

        # TODO: Combine threading to upgrade performance
        for idx, category_url in enumerate(category_urls):
            sheet_name = category_url.split('/')[-2].strip()

            headers = ("Tên thuốc", "url", "Image", "Nhóm thuốc", "Dạng bào chế", "Đóng Gói", "Thành phần", "Số đăng ký", "Nhà sản xuất", "Nhà đăng ký", "Nhà phân phối",
                       "Chỉ định", "Đối tượng sử dụng", "Liều lượng - cách dùng", "Cách dùng", "Chống chỉ định", "Chú ý đề phòng", "Dược lực", "Dược động học", "Tác dụng", "Tác dụng phụ")

            if idx == 0:
                ex.create_excel_file_with_headers(
                    headers, sheet_name, excel_name_file)
            else:
                wb = ex.add_sheet_w_headers_exists_excel(
                    headers, sheet_name, excel_name_file)
                sheet = wb.get_sheet(idx)

            page = 1
            line = 1
            while True:
                print(
                    f"Go to page {page} ---- category {category_url} ----- idx {idx}")

                payload = {
                    "__VIEWSTATEGENERATOR": "336E2262",
                    "page": page,
                    "currentView": 1,
                    "__VIEWSTATEENCRYPTED": "",
                    "Drugnews1$Gr1": "Rdrgnm",
                    "Drugnews1$txtKeyword": ""
                }

                global req_category
                try:
                    req_category = s.post(category_url, data=payload, stream=True,
                                          timeout=20, headers=requests.utils.default_headers())
                except requests.exceptions.ConnectionError as e:
                    continue
                except requests.exceptions.Timeout as e:
                    print(f">>>> Requests Timeout {e}. Try to connect again")
                    req_category = s.post(category_url, data=payload, stream=True,
                                          timeout=20, headers=requests.utils.default_headers())
                except requests.exceptions.RequestException as e:
                    raise SystemExit(e)
                    continue

                soup_category = BeautifulSoup(req_category.content, 'lxml')

                table_list_drug = soup_category.find(
                    'table', id='Drugnews1_dlstThuoc')

                if not table_list_drug:
                    break

                drug_name_per_pages = table_list_drug.find_all('h2')

                if not drug_name_per_pages:
                    break

                for drug_name_title in drug_name_per_pages:
                    product_url = ThuocBietDuoc.get_product_url(
                        drug_name_title)

                    soup_product_detail = ThuocBietDuoc.find_article_product_detail(
                        product_url)

                    if not soup_product_detail:
                        continue

                    drug_infos = ThuocBietDuoc.get_product_info(
                        soup_product_detail, product_url)

                    ex.save_data_row_to_excel(
                        line, drug_infos, excel_name_file, idx)
                    line = line + 1

                page = page + 1
                payload["page"] = page
