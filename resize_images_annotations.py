from PIL import Image
import glob
import os
import xml.etree.ElementTree as ET

dividings_widths = []
dividings_heights = []

parent_dir = 'all_rotated_annotated_test'
for image_file in glob.glob(os.path.join(parent_dir, '*.jp*')):
    image = Image.open(image_file)
    width, height = image.size
    #print(width, height)
    resized_image = image.resize((300, 300))
    resized_image.save(image.filename)
    width300, height300 = resized_image.size
    #print(width300, height300)
    divide_width = width/width300
    divide_height = height/width300
    #print(divide_height)
    dividings_widths.append(divide_width)
    dividings_heights.append(divide_height)
    #print(dividings_heights)

i = 0
for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    key: object

    for elem in tree.iter(tag='width'):
        elem.text = str(300)
    for elem in tree.iter(tag='height'):
        elem.text = str(300)
    for elem in tree.iter(tag='xmin'):
        elem.text = str(int(int(elem.text)/dividings_widths[i]))
    for elem in tree.iter(tag='ymin'):
        elem.text = str(int(int(elem.text)/dividings_heights[i]))
    for elem in tree.iter(tag='xmax'):
        elem.text = str(int(int(elem.text) / dividings_widths[i]))
    for elem in tree.iter(tag='ymax'):
        elem.text = str(int(int(elem.text) / dividings_heights[i]))
    i = i + 1
    tree.write(xml_file)

