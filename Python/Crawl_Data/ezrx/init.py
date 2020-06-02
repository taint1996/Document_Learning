import requests
from bs4 import BeautifulSoup, Comment
import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

from timeit import default_timer as timer
from datetime import timedelta, date, datetime
import json

from to_excel import ToExcel as ex

url_login = "https://www.ezrx.com.vn/10_Member/member_p.asp?flag=log"
url_main = "https://www.ezrx.com.vn/mainCommon.asp"

s = requests.Session()

payload={"tbxUserId":"30338855", "tbxPassword": "P@ssw0rdz"}