import os
from numpy import asarray
from matplotlib import image
directorio = "PetrograbadosCuadrados"
entradas = os.listdir(directorio)
conjunto = set()
for element in entradas:
    #subentradas = os.listdir(directorio +"/"+element)
    #for imagenes in subentradas:
    imagen = image.imread(directorio +"/"+element)
    data = asarray(imagen)
    conjunto.add(data.shape)
print(conjunto)