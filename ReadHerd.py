from xml.etree import ElementTree as ET
import Yak
from Yak import yak
file_name = 'herd.xml'
tree = ET.parse(file_name)
root = tree.getroot()
Herd = []
for child in root:
    NewYak = yak()
    NewYak.name = child.attrib['name']
    NewYak.age = float(child.attrib['age'])
    NewYak.sex = child.attrib['sex']
    Herd.append(NewYak)
[milk,wol,age,age_shave] = Yak.Stockstatus(Herd,13)
N = len(Herd)
print('In Stock:\n ' f'{"%.2f" % milk} liter of milk\n {wol} skins of wool')
print('Herd:')
for i in range(N):
    if age[i] >= 10:
        print(f'{Herd[i].name} is dead')
    else:
        print(f'{Herd[i].name} is {"%.2f" %age[i]} years old')