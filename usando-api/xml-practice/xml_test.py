import os
import xml.etree.ElementTree as ET

current_dir = os.path.dirname(__file__)
print(current_dir)
xml_path = os.path.join(current_dir, "cars.xml")
print(xml_path)

cars_for_sale = ET.parse(xml_path).getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
        print('\t', car.tag)
        for prop in car:
            print('\t\t', prop.tag, end='')
            if prop.tag == 'price':
                print(prop.attrib, end='')
            print(' =', prop.text)

# ###########################################################################
# ----------------------Removendo e adicionando tag -------------------------
# ###########################################################################

for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = ET.Element('car')
ET.SubElement(new_car, 'id').text = '4'
ET.SubElement(new_car, 'brand').text = 'Maserati'
ET.SubElement(new_car, 'model').text = 'Mexico'
ET.SubElement(new_car, 'production_year').text = '1970'
ET.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
ET.parse(xml_path).write('newcars.xml', method='')