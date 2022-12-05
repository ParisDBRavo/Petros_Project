import os 
import random
from PIL import Image
import numpy as np
import Petrosds
import DisplayBatch
from torchvision import transforms
from torch.utils.data import DataLoader, random_split
# tamaño del lote
BATCH_SIZE = 32
# filas y columnas de la rejilla de imágenes
ROWS, COLS = 4, 8

# tamaño del conjunto de entrenamiento (porcentaje)
TRN_SIZE = 0.8
NUM_WORKERS = 4 # hilos

# media y varianza de ImageNet
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

data_dir= "ReduccionSinAumento"
images_names= os.listdir(data_dir)
print(len(images_names))
random.shuffle(images_names)
trn_names= [images_names[i::int(len(images_names))] for i in range(int(len(images_names)*0.8))]
tst_names= [images_names[i::int(len(images_names))] for i in range(int(len(images_names)*0.8), int(len(images_names)))]
print(len(trn_names))
print(len(tst_names))
#print(trn_names)
trn_names = [item for items in trn_names for item in items]
tst_names = [item for items in tst_names for item in items]
tsfm = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD)
])
tst_tsfm = transforms.Compose([
    # convertimos a torch.Tensor
    transforms.ToTensor(),
    # Normalizamos
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD)
])
trn_ds = Petrosds.PetrosDS(data_dir, trn_names, tst_names, tsfm,True)
tst_ds = Petrosds.PetrosDS(data_dir, trn_names, tst_names, tst_tsfm,False)
tst_tsfm = transforms.Compose([
    # convertimos a torch.Tensor
    transforms.ToTensor(),
    # Normalizamos
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD)
])
trn_dl = DataLoader(
    # conjunto
    trn_ds,
    # tamaño del lote
    batch_size=BATCH_SIZE,
    # desordenar
    shuffle=True,
)
tst_dl = DataLoader(
    # conjunto
    tst_ds,
    # tamaño del lote
    batch_size=BATCH_SIZE,
    # desordenar
    shuffle=True,
)
x, y = next(iter(trn_dl))
print(f'x shape={x.shape} dtype={x.dtype}')
print(f'y shape={y.shape} dtype={y.dtype}')
titles = [f'{l.item()} '  for l in y]
DisplayBatch.display_batch(x, titles, ROWS, COLS)
