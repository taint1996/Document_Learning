from init import *

class ATCCode:
    def __init__(self):
        Thread.__init__()
        self.daemon = True

    def request_url(url):
        global req
        try:
            req = s.get(url, timeout=20, stream=True)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error {e}. Try to connect again")
            req = s.get(url, timeout=20, stream=True)
        except requests.exceptions.Timeout as e:
            print(f"Connection Timeout {e}. Try to connect again")
            req = s.get(url, timeout=20, stream=True)
        except requests.exceptions.TooManyRedirects as e:
            raise(SystemError)
            pass
        return BeautifulSoup(req.content, 'lxml')

    def get_text_li_tag(li_tag) -> str:
        return li_tag.get_text(strip=True)

    def code_dash_name_format(code, name):
        return f"{code.upper().strip()}-{name.title().strip()}"

    def code_format(code_name) -> str:
        return re.sub(r"\s:\w+.*", "", code_name)

    def name_format(code_name) -> str:
        return re.sub(r"(.*?):", "", code_name)

    def code_name_categories(a_tags):
        code_name_categories = []
        for a_tag in a_tags:
            code_name_categories.append(
                f"{a_tag.get('href').replace('/', '')}-{a_tag.get('title').title().strip()}")
        return code_name_categories

    def data_category_w_medicines(code_lv_4, name_lv_4):
        url_lv_4 = f"{url}{code_lv_4}"
        soup_category_lv_4 = ATCCode.request_url(url_lv_4)
        a_tags = soup_category_lv_4.find('ul').find_all('a')[1:]
        code_name_categories = ATCCode.code_name_categories(a_tags)

        # all drugs: A01AA01-Name1, A01AA02-Name2
        all_li_from_last_ul_category_lv_4 = soup_category_lv_4.find_all(
            'ul')[-1].find_all('li')
        medicines = list(map(lambda drug: drug.get_text(strip=True).replace(
            r" : ", "-"), all_li_from_last_ul_category_lv_4))

        #      lv1: V-Various Atc Structures', lv2: V01-Allergens, lv3: V01A-Allergens,     lv4: A01AA, medicines
        return [code_name_categories[0], code_name_categories[1], code_name_categories[2], ATCCode.code_dash_name_format(
            code_lv_4, name_lv_4), medicines]

    def code_name_category_from_title(soup, code_category):
        name_category = re.sub(
            r"\s-.+", "", soup.find("title").get_text(strip=True))
        return f"{code_category} - {name_category}"

    def find_all_ul_index_page(url):
        soup = ATCCode.request_url(url)
        return soup.find_all('ul', attrs={'style': 'margin-bottom:40px'})

    def data_category_lv_3_without_a_tag(category_lv_3_a_tag, code_name_category_lv_3, line, excel_name_file):
        main_a_tags = soup_category_lv_3.find_all('ul')[1].find_all('a')

        code_name_categories = ATCCode.code_name_categories(
            main_a_tags)
        code_name_lv_3 = ATCCode.code_name_category_from_title(
            soup_category_lv_3, code_category_lv_3)

        return [code_name_categories[0], code_name_categories[1], code_name_category_lv_3, '', '']

    def save_final_level_w_medicines(code_category, name_category, line, excel_name_file):
        # -> V01AA01 or None
        ex.save_data_row_to_excel(line, ATCCode.data_category_w_medicines(
            code_category, name_category), excel_name_file)

    def data_atc_code(excel_name_file):
        find_all_ul_tags_index_page = ATCCode.find_all_ul_index_page(url)

        #       A,            A01,         A01A,            A01AA,     A01AA01 ( Ten thuoc/ chat hoa hoc)
        # uses for lv 1, uses for lv 2, uses for lv 3, uses for lv 4, medicines
        line = 1

        for ul in find_all_ul_tags_index_page:
            li_tags = ul.find_all('li')

            for li in li_tags:
                code_name_category = li.get_text(
                    strip=True)  # 'V: Various Atc Structures'

                code_category = ATCCode.code_format(
                    code_name_category)  # A01A/ A01/ A01AA
                name_category = ATCCode.name_format(code_name_category)

                category_lv2 = ATCCode.code_dash_name_format(
                    code_category, name_category)

                find_a_tag_drug_use = li.find('a')  # /A01A: công dụng thuốc

                if len(code_category) == 3:  # A01
                    # A01 -> A01A -> A01AA -> A01AA01 or None
                    # A01 -> A01AA -> A01AA01 or None
                    # A01 -> A01AA01 or None

                    if not find_a_tag_drug_use:
                        data = [code_name_category, category_lv2, '', '', '']
                        ex.save_data_row_to_excel(line, data, excel_name_file)
                        line = line + 1
                        continue

                    soup_category_lv_2 = ATCCode.request_url(
                        f"{url}{code_category}")
                    get_last_ul_lv_2 = soup_category_lv_2.find_all('ul')[-1]

                    for li in get_last_ul_lv_2.find_all('li'):
                        code_name_category_lv_3 = li.get_text(strip=True)

                        code_category_lv_3 = ATCCode.code_format(
                            code_name_category_lv_3)  # A01A/ A01AA/ A01AA01
                        name_category_lv_3 = ATCCode.name_format(
                            code_name_category_lv_3)
                        category_lv_3_a_tag = li.find('a')

                        # case A01A
                        if len(code_category_lv_3) == 4:
                            soup_category_lv_3 = ATCCode.request_url(
                                f"{url}{code_category_lv_3}")

                            if not category_lv_3_a_tag:
                                data = ATCCode.data_category_lv_3_without_a_tag(
                                    category_lv_3_a_tag, code_name_category_lv_3)
                                ex.save_data_row_to_excel(
                                    line, data, excel_name_file)
                                line = line + 1
                                continue

                            all_li_from_last_ul_lv_3 = soup_category_lv_3.find_all(
                                'ul')[-1].find_all('li')

                            # find all ul at last to get category drug lv 3
                            for li in all_li_from_last_ul_lv_3:
                                code_name_category_lv_4 = li.get_text(
                                    strip=True)

                                code_category_lv_4 = ATCCode.code_format(
                                    code_name_category_lv_4)  # A01AA
                                name_category_lv_4 = ATCCode.name_format(
                                    code_name_category_lv_4)

                                a_tag_category_lv_4 = li.find('a')

                                if len(code_category_lv_4) == 5:
                                    if not a_tag_category_lv_4:
                                        soup_category_lv_4 = ATCCode.request_url(
                                            f"{url}{code_category_lv_4}")

                                        main_a_tags = soup_category_lv_4.find_all('ul')[
                                            1].find_all('a')
                                        code_name_categories = ATCCode.code_name_categories(
                                            main_a_tags)

                                        data = [code_name_categories[0], code_name_categories[1], code_name_categories[2],
                                                code_name_category_lv_4, '']

                                        ex.save_data_row_to_excel(
                                            line, data, excel_name_file)
                                        line = line + 1
                                        continue
                                    else:
                                        ATCCode.save_final_level_w_medicines(code_category_lv_4, name_category_lv_4,
                                                                             line, excel_name_file)
                                        line = line + 1

                        # case A01AA
                        if len(code_category_lv_3) == 5:
                            ATCCode.save_final_level_w_medicines(
                                code_category_lv_3, name_category_lv_3, line, excel_name_file)
                            line = line + 1

                # V01AA
                if len(code_category) == 5:
                    ATCCode.save_final_level_w_medicines(
                        code_category, name_category, line, excel_name_file)
                    line = line + 1

                if len(code_category) == 4:
                    # A01A -> A01AA -> A01AA01
                    # Soup level 2: A01A => find all ul at last to lv 3
                    soup_category_lv_3 = ATCCode.request_url(
                        f"{url}{code_category}")
                    main_a_tags = soup_category_lv_3.find_all(
                        'ul')[1].find_all('a')
                    code_name_categories = ATCCode.code_name_categories(
                        main_a_tags)

                    all_li_from_last_ul_soup_category_lv_3 = soup_category_lv_3.find_all(
                        'ul')[-1].find_all('li')

                    for li in all_li_from_last_ul_soup_category_lv_3:
                        code_name_category_lv_4 = li.get_text(strip=True)

                        code_category_lv_4 = ATCCode.code_format(
                            code_name_category_lv_4)  # A01AA
                        name_category_lv_4 = ATCCode.name_format(
                            code_name_category_lv_4)

                        a_tag_category_lv_4 = li.find('a')

                        if not a_tag_category_lv_4:
                            # save data to excel
                            data = [code_name_categories[0], code_name_categories[1], ATCCode.code_name_category_from_title(soup_category_lv_3, code_category),
                                    ATCCode.code_dash_name_format(code_category_lv_4, name_category_lv_4), '']
                            ex.save_data_row_to_excel(
                                line, data, excel_name_file)
                            line = line + 1
                            continue
                        else:
                            ATCCode.save_final_level_w_medicines(
                                code_category_lv_4, name_category_lv_4, line, excel_name_file)
                            line = line + 1
