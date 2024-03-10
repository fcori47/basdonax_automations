# AI Content Creation

Este repositorio contiene herramientas automatizadas para la edición y transcripción de contenido de video, utilizando las tecnologías de Python `auto-editor` y `whisper`. Estas herramientas están diseñadas para acelerar el proceso de edición de video y generar transcripciones automáticas.

## Requisitos previos

- Python: https://www.python.org/downloads/release/python-3115/
- Dependencias de Python especificadas en `requirements.txt` o `requirements_transcripts_cuda.txt`/`requirements_transcripts_no_cuda.txt`

## Instalación

### Creación de un entorno virtual

Antes de instalar las dependencias, es recomendable crear un entorno virtual para evitar conflictos con otras bibliotecas o versiones de Python. 

#### Windows

```
py -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```
python3 -m venv .venv
source .venv/bin/activate
```

## Instalación de dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias:

### Para recortes.py:

```
pip install -r requirements.txt
```

### Para transcriptions.py:
* Con CUDA:
```
    pip install -r requirements_transcripts.txt
```

Instalamos CUDA 12.1 (Windows):

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
Instalamos CUDA 12.1 (Linux/No disponible para Mac):
```
pip3 install torch torchvision torchaudio
```

* Sin CUDA:

```
pip install -r requirements_transcripts.txt
```

## Uso

### recortes.py

Este script recorta los momentos de silencio en videos .mkv o .mp4 y los guarda en una carpeta especificada. Modifica las rutas en el script según tus necesidades:

```
if __name__ == "__main__":
    path = r'D:\yt\raw2'
    destino_recortes = r'D:\yt\recortes'
```

### transcriptions.py
Este script genera transcripciones en formato .srt para videos .mp4 o .mkv. Modifica las rutas y el modelo de Whisper según tus necesidades:

```
if __name__ == "__main__":
    path_videos = r'D:\yt\rawshorts'
    destino_transcripciones = r'D:\yt\transcripciones'
```

## Creación de archivos ejecutables

Para facilitar el uso de los scripts, puedes crear archivos ejecutables que permitan ejecutarlos con un doble clic. A continuación, se muestran ejemplos para Windows, pero puedes adaptarlos para Linux y Mac.

### Windows

#### recortes.bat:

```
@echo off
python "C:\Ruta\A\Tu\Script\recortes.py"
pause
```

#### transcripts.ps1:

```
# Activa el entorno virtual
& "C:\Ruta\A\Tu\Entorno\.venv\Scripts\Activate.ps1"

# Ejecuta el script de transcripciones
python "C:\Ruta\A\Tu\Script\transcriptions.py"

# Desactiva el entorno virtual
deactivate
```

Coloca estos archivos en tu escritorio o en una ubicación conveniente y haz doble clic para ejecutar los scripts.

### Linux/Mac

#### recortes.sh:

```
#!/bin/bash
source /Ruta/A/Tu/Entorno/.venv/bin/activate
python /Ruta/A/Tu/Script/recortes.py
deactivate
```

#### transcripts.sh:

```
#!/bin/bash
source /Ruta/A/Tu/Entorno/.venv/bin/activate
python /Ruta/A/Tu/Script/transcriptions.py
deactivate
```

Haz los archivos ejecutables:

```
chmod +x recortes.sh transcripts.sh
```

Ahora puedes ejecutar los scripts con un doble clic.

