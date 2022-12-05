from PIL import Image
import os
import pandas as pd
import math
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def ObtenerCLasificacion(nombreCarpeta):
    data = pd.read_csv("YVerdaderas.csv")
    #print(nombreCarpeta)
    linea = data.loc[data["Soporte"]==nombreCarpeta, "Tipo de motivo"].item()
    return linea
directorio = "Petrograbados"
entradas = os.listdir(directorio)
conjunto = set()
#for element in entradas:
#    subentradas = os.listdir(directorio +"/"+element)
#    subentradas.remove("recortadas")
#    for imagenes in subentradas:
#        imagen = Image.open(directorio +"/"+element+ "/"+imagenes)
#        im_new = crop_max_square(imagen)
#        im_new.save("/PetrograbadosCuadrados/"+imagenes, quality=95)   
#print(len(entradas))
for element in entradas:
    Yverdadera = ObtenerCLasificacion(element)
    if (math.isnan(Yverdadera)):
        entradas.remove(element)
    subentradas = os.listdir(directorio +"/"+element)
    try:
        subentradas.remove("recortadas")
    except:
        print("")
for element in entradas:
    subentradas = os.listdir(directorio +"/"+element)
    try:
        subentradas.remove("recortadas")
    except:
        print("")
    Yverdadera = ObtenerCLasificacion(element)
    for imagenes in subentradas:
        imagen = Image.open(directorio +"/"+element+ "/"+imagenes)
        im_new = crop_max_square(imagen)
        im_new.save("PetrograbadosCuadrados/"+str(Yverdadera)+"_"+imagenes, quality=95)   
#print(len(entradas))}