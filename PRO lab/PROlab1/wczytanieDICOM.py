import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pylab as py
from PIL import Image
import pydicom as dicom
import pydicom as dcm

#____________wprowadzenie____________
a=np.zeros((100,100),dtype=bool)
a[30:50,30:50]=True
a[50:70,50:70]=True

py.imshow(a,cmap = py.cm.gray, interpolation = 'nearest')
py.show()

#______________praca z obrazami___________
plik=dicom.read_file('IM-0001-0107.dcm')
print("15596973", plik)
pixel=plik.pixel_array
py.imshow(pixel,cmap=py.cm.gray,interpolation='nearest')
py.show()

#robaczek
robaczek_szary = mpimg.imread('stinkbug.png')
imshow = plt.imshow(robaczek_szary)
plt.show()

robaczek = robaczek_szary[:, :, 0]
implot = plt.imshow(robaczek)
implot.set_cmap('nipy_spectral')
plt.colorbar()
plt.show()

#_____________________praca z metadanymi__________________
print(plik.dir())
print(plik.PatientName)
print(plik.ImageType)
print(plik.PatientAge)

filename='0015.dcm'
dataset = dcm.read_file(filename)
print(dataset)

print(dataset.StudyDate)
print(dataset[(0x8, 0x20)])
element=dataset.data_element('StudyDate')
print("Wartość elementu:", element.value)

lista1= dataset.dir('pat')
print(lista1)
for de in lista1:
 print("dateset: ", dataset.data_element(de))

dataset.StudyDate= '20180111' #dzisiejsza data
lista2 = ['PatientAge',
 'PatientBirthDate',
 'PatientID',
 'PatientSex',]
for de in lista2:
    print(de)
    if type(dataset.data_element(de).value)==str:
        dataset.data_element(de).value='nic'
        print(dataset.data_element(de).value)
    if 'float' in str(type(dataset.data_element(de).value)):
        dataset.data_element(de).value=0