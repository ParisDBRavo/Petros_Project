import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image
from numpy import asarray
import numpy as np
def HacerDosImagenes(nombre, directorio):
    name = obtenerNombre(nombre)
    imagen = image.imread(directorio+ "/"+ nombre)
    data = asarray(imagen)
    #print(data.shape)
    imageEven= acortarPixelesPar(data)
    imageEven = rotar270(imageEven)
    imageNon= acortarPixelesImpar(data)
    imageNon = rotar270(imageNon)
    im = Image.fromarray(imageEven)
    im.save("SegundaReduccion/"+nombre.split('_')[0]+"_P"+nombre)
    im = Image.fromarray(imageNon)
    im.save("SegundaReduccion/"+nombre.split('_')[0]+"_N"+nombre)

def obtenerNombre(nombre):
    nombre.split(".")
    return nombre[0]
def acortarPixelesImpar(data):
    image = data[1::2]  
    image = np.rot90(image)
    image= image[1::2]
    return image
def acortarPixelesPar(data):
    image = data[::2]
    image = np.rot90(image)
    image= image[::2]
    return image
def rotar270(imagen):
    imagen = np.rot90(imagen)
    imagen = np.rot90(imagen)
    imagen = np.rot90(imagen)
    return imagen
