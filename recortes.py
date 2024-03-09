import os
import subprocess
import shutil
import time


def listar_archivos(path):
    archivos = []
    archivos_fcpxml = set()
    archivos_procesados = set()
    for root, dirs, files in os.walk(path):
        for file in files:
            nombre_archivo, extension = os.path.splitext(file)
            if extension.lower() in (".fcpxml", ".xml"):
                archivos_fcpxml.add(nombre_archivo.replace("_ALTERED", ""))
                archivos_procesados.add(nombre_archivo)
            elif extension.lower() in (".mkv", ".mp4") and nombre_archivo not in archivos_fcpxml:
                archivos.append(os.path.join(root, file))
    return archivos, archivos_fcpxml, archivos_procesados


def mover_archivos_fcpxml(origen, destino):
    archivos_en_carpeta = os.listdir(origen)
    for archivo in archivos_en_carpeta:
        if archivo.endswith((".xml", ".fcpxml")):
            archivo_destino = os.path.join(destino, archivo)
            if not os.path.exists(archivo_destino):
                try:
                    shutil.move(os.path.join(origen, archivo), destino)
                    print(f"Archivo {archivo} movido a {destino}")
                except FileNotFoundError:
                    print(f"No se pudo encontrar el archivo {archivo}.")
            else:
                print(f"El archivo {archivo} ya existe en el destino, omitiendo.")



def ejecutar_auto_editor(archivos, archivos_fcpxml, archivos_procesados, destino_recortes):
    archivos_nuevos = []
    archivos_en_destino = os.listdir(destino_recortes)
    archivos_procesados_en_destino = set()
    for archivo in archivos_en_destino:
        nombre_archivo, extension = os.path.splitext(archivo)
        if extension.lower() in (".fcpxml", ".xml"):
            archivos_procesados_en_destino.add(nombre_archivo.replace("_ALTERED", ""))
    for archivo in archivos:
        nombre_archivo_base, extension = os.path.splitext(os.path.basename(archivo))
        if nombre_archivo_base not in archivos_fcpxml and nombre_archivo_base not in archivos_procesados and nombre_archivo_base not in archivos_procesados_en_destino:
            comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export resolve"
            try:
                subprocess.run(comando, shell=True, check=True)
                print(f"Archivo {archivo} procesado correctamente.")
                archivo_procesado = f"{nombre_archivo_base}_ALTERED{extension}"
                archivos_nuevos.append(archivo_procesado)
            except subprocess.CalledProcessError as e:
                print(f"Error al procesar el archivo '{archivo}': {e}")
        elif nombre_archivo_base in archivos_fcpxml:
            print(f"Archivo {archivo} ya tiene su archivo .fcpxml correspondiente, omitiendo.")
        elif nombre_archivo_base in archivos_procesados_en_destino:
            print(f"Archivo {archivo} ya tiene su archivo _ALTERED en el destino, omitiendo.")
    return archivos_nuevos


if __name__ == "__main__":
    path = r'D:\yt\raw2'
    destino_recortes = r'D:\yt\recortes'
    archivos, archivos_fcpxml, archivos_procesados = listar_archivos(path)
    if archivos:
        # Ejecutar el auto editor
        archivos_procesados = ejecutar_auto_editor(archivos, archivos_fcpxml, archivos_procesados, destino_recortes)
        
        # Mover los archivos procesados al destino
        mover_archivos_fcpxml(path, destino_recortes)  # Se pasa la ruta de origen y el destino
    else:
        print("No se encontraron archivos .mkv o .mp4 en la carpeta especificada.")
