from ast import Name
from PIL import Image
import numpy as np
class PetrosDS:

    def __init__(self, root, trn_names, test_names, tsfm, flag):
          
        # guardamos la tranformación para las imágenes
        self.tsfm = tsfm
        
        # leemos el dataframe y filtramos columna healthy
        #df = pd.read_csv(os.path.join(root, 'trn.csv'), index_col='item')
        #df = df['healthy']
        
        # direcorios superiores
        #base_dir = os.path.join(root, 'trn')
        #classes = sorted(os.listdir(base_dir))
        
        # lista con las rutas a las imágenes
        self.paths = []
        # lista con las etiquetas de las imágenes
        self.labels = []
        # por cada clase
        images = trn_names if flag == True else test_names
        for name in images:
            # directorio de la clase
            #class_dir = os.path.join(base_dir, clazz)
            # nombres de los archivos en el directorio de la clase
            #names = sorted(os.listdir(class_dir))
            # guardamos los rutas y las etiquetas
            #for name in names:
            #print(str(name))
            self.labels.append(name.split('_')[0])
            self.paths.append(f'{root}/{name}')

    def __getitem__(self, i):
        # obtenemos la ruta de la imagen
        path = self.paths[i]
        # cargamos la imagen
        x = Image.open(path)
        # aplicamos transformación
        x = self.tsfm(x)
        # leeamos la etiqueta
        y = np.array(self.labels[i], np.float32).reshape(1)
        # regresamos el ejemplo
        return x, y

    def __len__(self):
        # número de ejemplos en el conjunto
        return len(self.paths)
