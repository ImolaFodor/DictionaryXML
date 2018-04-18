import glob
import os
import xml.etree.ElementTree as ET
import xlrd

wb = xlrd.open_workbook('LabelDictionary.xlsx')
d2 = {}
sh2 = wb.sheet_by_index(0)
for i in range(37):
    cell_value_class2 = sh2.cell(i, 2).value
    cell_value_id2 = sh2.cell(i, 1).value
    d2[cell_value_class2] = cell_value_id2

print(d2)

parent_dir = 'labelMilansAgain'
for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    key: object

    for i in range(7):
        for key, value in d2.items():
            try:
                if root[i][0].text == value:
                    root[i][0].text = str(key)
            except IndexError:
                print('No childNodes for this element')
            tree.write(xml_file)

