from PIL import Image
import pydicom as dicom
import numpy as np
import pylab as py


#Wczytanie pliku
plik=dicom.read_file('0015.dcm')

#Uzyskanie informacji o max i min wartości elementów w tablicy z obrazu
pixel=plik.pixel_array
print('Ksztalt: ', pixel.shape)
print('Minimalna wartosc pixela: ', min(pixel.flatten()), 'Maksymalna wartosc pixela',max(pixel.flatten()))
py.imshow(pixel,cmap=py.cm.gray,interpolation='nearest')
py.show()

#Przypisanie wartości 0-1
pixel=pixel*1.0/max(pixel.flatten())

def dodajPasek(tablica, n):
 tablica[:n,:]=np.linspace(0,1,tablica.shape[1])

def jasnosc(tablica, a):
 def f(x,a):
  return min(a*x,1.0)
 wynik=tablica.copy()
 for x,y in np.ndindex(tablica.shape):
  wynik[x,y]=f(tablica[x,y],a)
 dodajPasek(wynik,15)
 return wynik

py.imshow(jasnosc(pixel,2),cmap=py.cm.gray,interpolation='nearest')
py.show()
py.imshow(jasnosc(pixel,0.5),cmap=py.cm.gray,interpolation='nearest')
py.show()

def gamma(tablica, a):
 def f(x,a):
  return min(x**a,1.0)
 wynik=tablica.copy()
 for x,y in np.ndindex(tablica.shape):
  wynik[x,y]=f(tablica[x,y],a)
 dodajPasek(wynik,15)
 return wynik

py.imshow(gamma(pixel,2),cmap=py.cm.gray,interpolation='nearest')
py.show()
py.imshow(gamma(pixel,0.5),cmap=py.cm.gray,interpolation='nearest')
py.show()

def prog(tablica, a):
 def f(x,a):
  return 0 if x<a else 1
 wynik=tablica.copy()
 for x,y in np.ndindex(tablica.shape):
  wynik[x,y]=f(tablica[x,y],a)
 dodajPasek(wynik,15)
 return wynik

py.imshow(prog(pixel,0.5),cmap=py.cm.gray,interpolation='nearest')
py.show()

from medpy.io import load
import matplotlib.pyplot as plt
import matplotlib.cm as cm
i, h = load("flair.nii")
plt.imshow(i, cmap = cm.Greys_r)
plt.show()
print('Rozdzielczosc obrazu: ', i.shape)

from medpy.io import header
print('Rozstaw wokseli: ', header.get_pixel_spacing(h))

plt.hist(i.ravel(), bins=32, log=True)
plt.show()

bgmean = i[:10,:10].mean()
brainmask = i > bgmean
plt.imshow(brainmask, cmap = cm.Greys_r)
plt.show()

i[np.random.randint(0, i.shape[0], int(0.05 * i.size)), np.random.randint(0,
i.shape[1], int(0.05 * i.size))] = i.min()
i[np.random.randint(0, i.shape[0], int(0.05 * i.size)), np.random.randint(0,
i.shape[1], int(0.05 * i.size))] = i.max()
plt.imshow(i, cmap = cm.Greys_r);
plt.show()

brainmask = i > 0
plt.imshow(brainmask, cmap = cm.Greys_r)
plt.show()

from medpy.filter import largest_connected_component
brainmask = largest_connected_component(brainmask)
plt.imshow(brainmask, cmap = cm.Greys_r)
plt.show()

from scipy.ndimage import binary_fill_holes
brainmask = binary_fill_holes(brainmask)
plt.imshow(brainmask, cmap = cm.Greys_r)
plt.show()




