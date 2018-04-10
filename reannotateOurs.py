import glob
import os
import xml.etree.ElementTree as ET
import xlrd

wb = xlrd.open_workbook('LabelDictionary.xlsx')
d2 = {}
sh2 = wb.sheet_by_index(1)
for i in range(37):
    cell_value_class2 = sh2.cell(i, 0).value
    cell_value_id2 = int(sh2.cell(i, 1).value)
    d2[cell_value_class2] = cell_value_id2

print(d2)

parent_dir = 'labelsOurs'
for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print(root[6][0].text)
    key: object
    for key, value in d2.items():
            try:
                if root[6][0].text == key:
                    root[6][0].text = str(value)
            except IndexError:
                print('No childNodes for this element')
            try:
                if root[7][0].text == key:
                    root[7][0].text = str(value)
            except IndexError:
                print('No childNodes for this element')
            try:
                if root[8][0].text == key:
                    root[8][0].text = str(value)
            except IndexError:
                print('No childNodes for this element')
            try:
                if root[9][0].text == key:
                    root[9][0].text = str(value)
            except IndexError:
                print('No childNodes for this element')
            try:
                if root[10][0].text == key:
                    root[10][0].text = str(value)
            except IndexError:
                print('No childNodes for this element')
            tree.write(xml_file)

