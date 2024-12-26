import pandas as pd
import shutil
import subprocess
import dicom2nifti
import os

# Primero vamos a crear una carpeta con únicamente los datos de los pacientes sanos y con 
# los distitnos formatos de imagen.

directorio = "C:\\Users\\albert.pumarberga\\Desktop\\PROYECTO AUTOENCODER\\train"
resultado = subprocess.run(["dir", directorio], capture_output=True, text=True, shell=True)
lista_archivos = resultado.stdout.split('\n')
formato = "T2w" # Distintos formatos ["FLAIR", "T1w", "T1wCE", "T2w"]

# Eliminar cualquier cadena vacía al final de la lista
train_patients = [archivo[-5:] for archivo in lista_archivos if archivo]

# Ruta del directorio principal que contiene 'train' y 'train_labels.csv'
directorio_principal = 'C:\\Users\\albert.pumarberga\\Desktop\\PROYECTO AUTOENCODER'

# Leer el archivo CSV
archivo_labels = os.path.join(directorio_principal, 'train_labels.csv')
df = pd.read_csv(archivo_labels)

# Filtrar los subdirectorios con etiqueta 0
subdirectorios_healthy = df[df['MGMT_value'] != 1]['BraTS21ID'].astype(str).str.zfill(5).tolist()

subdirectorios_unhealthy = df[df['MGMT_value'] == 1]['BraTS21ID'].astype(str).str.zfill(5).tolist()


healthy_patients = [x for x in train_patients if x in subdirectorios_healthy]
unhealthy_patients = [x for x in train_patients if x in subdirectorios_unhealthy]

def get_dicom_files(root_dir, type_patients, formato_imagen):
    """ Esta función crea y devuelve un diccionario (dicom_files) que contiene como llave cada paciente y
      el valor consiste en la lista de archivos de tipo T1 para ese paciente."""
    dicom_files = {}
    for patient in os.listdir(root_dir):
        patient_files = []
        if patient in type_patients:
            for image_type in os.listdir(root_dir+"\\"+patient):
                if image_type == formato_imagen: # Usamos solo las imágenes de un tipo de formato a la vez
                    for file in os.listdir(root_dir+"\\"+patient+"\\"+image_type):
                        if file.endswith('.dcm'):
                            file_path = os.path.join(root_dir+"\\"+patient+"\\"+image_type, file)
                            patient_files.append(file_path)

            dicom_files[patient] = patient_files

    return dicom_files
    
archivos_dicom_healthy = get_dicom_files(directorio, healthy_patients, formato)
archivos_dicom_unhealthy = get_dicom_files(directorio, unhealthy_patients, formato) 

def convert_Dicom2Nifti(archivos_dicom, directorio_principal, formato, clase):
        """ Esta función sirve para crear un directorio train_healthy que contenga todos los archivos en
            formato DICOM de cada paciente y convertirlos a formato NIFTI en otro directorio llamado 
            train_nifti."""
        # Vamos primero a convertir el diccionario archivos_dicom en un directorio
        # para poder usar la función dicom2nifti.

        for clave, lista_archivos in archivos_dicom.items():
          # Crear la subcarpeta con el nombre de la clave ORIGEN
          subdirectorio_origen = os.path.join(directorio_principal+f"\\train_{clase}_{formato}", str(clave))
          os.makedirs(subdirectorio_origen, exist_ok=True)

          # Crear la subcarpeta con el nombre de la clave DESTINO
          subdirectorio_destino = os.path.join(directorio_principal+f"\\train_{clase}_nifti_{formato}", str(clave))
          os.makedirs(subdirectorio_destino, exist_ok=True)

          # Copiar cada archivo de la lista a la subcarpeta
          for archivo in lista_archivos:
              shutil.copy(archivo, subdirectorio_origen)

          # Convertimos el directorio a archvios nifti
          dicom2nifti.convert_directory(subdirectorio_origen,subdirectorio_destino)

convert_Dicom2Nifti(archivos_dicom_healthy, directorio_principal, formato, "healthy")

convert_Dicom2Nifti(archivos_dicom_unhealthy, directorio_principal, formato, "unhealthy")