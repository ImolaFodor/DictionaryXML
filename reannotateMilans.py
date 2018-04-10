import pandas as pd
import glob
import os
import xml.etree.ElementTree as ET
import xlrd
from datetime import datetime as dt
import time

vflag = 'true'

d = {}
wb = xlrd.open_workbook('LabelDictionary.xlsx')
sh = wb.sheet_by_index(0)
for i in range(37):
    cell_value_class = sh.cell(i, 0).value
    cell_value_id = int(sh.cell(i, 1).value)
    d[cell_value_class] = cell_value_id

print(d)

parent_dir = 'labelsMilans'
for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print(root[0][0].text)

    key: object
    for key, value in d.items():
        try:
            if root[0][0].text == key:
                root[0][0].text = str(value)
        except IndexError:
            print('No childNodes for this element')
        try:
            if root[1][0].text == key:
                root[1][0].text = str(value)
        except IndexError:
            print('No childNodes for this element')
        try:
            if root[2][0].text == key:
                root[2][0].text = str(value)
        except IndexError:
            print('No childNodes for this element')
        try:
            if root[3][0].text == key:
                root[3][0].text = str(value)
        except IndexError:
            print('No childNodes for this element')
        try:
            if root[4][0].text == key:
                root[4][0].text = str(value)
        except IndexError:
            print('No childNodes for this element')
        tree.write(xml_file)

