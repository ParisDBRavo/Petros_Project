from DuplicarImagenes import HacerDosImagenes
import os
directorio = 'PrimeraReduccion'
entradas = os.listdir(directorio)
#print(entradas)
for item in entradas:
    HacerDosImagenes(item, directorio)
