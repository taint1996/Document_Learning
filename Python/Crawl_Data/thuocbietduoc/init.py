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

from threading import Thread

s = requests.Session()

url = "https://www.thuocbietduoc.com.vn"
drug_url = "https://www.thuocbietduoc.com.vn/thuoc/drgsearch.aspx"