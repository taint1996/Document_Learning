import requests
from bs4 import BeautifulSoup

import re

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy as xl_copy
from openpyxl.styles import Font

from timeit import default_timer as timer
from datetime import timedelta, date, datetime
import json

url = "https://www.nhathuocankhang.com"
drug_url = "https://www.nhathuocankhang.com/thuoc"
prod_url = "https://www.nhathuocankhang.com/aj/Category/Products"

s = requests.Session()