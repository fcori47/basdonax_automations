# AI Content Creation

Este repositorio contiene herramientas automatizadas para la edición y transcripción de contenido de video, utilizando las tecnologías de Python `auto-editor` y `whisper`. Estas herramientas están diseñadas para acelerar el proceso de edición de video y generar transcripciones automáticas.

## Requisitos previos

- Python 3.11.5: https://www.python.org/downloads/release/python-3115/
- Dependencias de Python especificadas en `requirements.txt` o `requirements_transcripts.txt`

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
* Instalamos todo lo necesario (con/sin CUDA)
```
    pip install -r requirements_transcripts.txt
```

Instalamos CUDA 12.1 (Windows):

Primero instalamos CUDA 12.1 desde su página web oficial: https://developer.nvidia.com/cuda-12-1-0-download-archive

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
Instalamos CUDA 12.1 (Linux/No disponible para Mac):
```
pip3 install torch torchvision torchaudio
```

## Uso

### recortes.py

Este script recorta los momentos de silencio en videos .mkv o .mp4 y los guarda en una carpeta especificada. Modifica las rutas en el script según tus necesidades:

```
if __name__ == "__main__":
    path = r'D:\yt\raw2'
    destino_recortes = r'D:\yt\recortes'
```

Además de exportar para DaVinci Resolve, puedes especificar el formato de exportación para diferentes programas de edición de video. Modifica la línea de comando:
```
nombre_archivo_base, extension = os.path.splitext(os.path.basename(archivo))
        if nombre_archivo_base not in archivos_fcpxml and nombre_archivo_base not in archivos_procesados and nombre_archivo_base not in archivos_procesados_en_destino:
            comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export resolve" ### esta linea
```

en el script según el programa que estés utilizando:

* Para DaVinci Resolve:
```
comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export resolve"
```
* Para Adobe Premiere:
```
comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export premiere"
```
* Para Final Cut Pro:
```
comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export final-cut-pro"
```
* Para ShotCut:
```
comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export shotcut"
```
* Para ninguno de los anteriores:
```
comando = f"auto-editor \"{archivo}\" --edit \"(or audio:3% motion:6%)\" --export clip-sequence"
```

### transcriptions.py
Este script genera transcripciones en formato .srt para videos .mp4 o .mkv. Modifica las rutas y el modelo de Whisper según tus necesidades:

```
if __name__ == "__main__":
    path_videos = r'D:\yt\rawshorts'
    destino_transcripciones = r'D:\yt\transcripciones'
```
Importante tener en cuenta esta tabla

| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|--------|------------|--------------------|--------------------|---------------|----------------|
| tiny   | 39 M       | tiny.en            | tiny               | ~1 GB         | ~32x           |
| base   | 74 M       | base.en            | base               | ~1 GB         | ~16x           |
| small  | 244 M      | small.en           | small              | ~2 GB         | ~6x            |
| medium | 769 M      | medium.en          | medium             | ~5 GB         | ~2x            |
| large  | 1550 M     | N/A                | large              | ~10 GB        | 1x             |

Si vamos a utilizar esta automatización de IA con cpu, solo recomiendo que usen los modelos: tiny, base y como mucho small.

Link a el repositorio de la herramienta de IA (Whisper): https://github.com/openai/whisper

### Modificación de cantidad de longitud de palabras en el subtitulo:
```
word_options = {
            "highlight_words": False,
            "max_line_count": 1,
            "max_words_per_line": 1 
        }
```
Si queremos que el subtitulo tenga en cuenta más de una sola palabra, cambiamos la ultima linea _"max_words_per_line": 1_ a la cantidad de palabras que queramos, reemplazando el 1.

### Modificar el modelo (que repercute en la calidad de transcripcion) y también si queremos usar CPU o nuestra gráfica Nvidia:

```
model = whisper.load_model(name='medium', device='cuda')
```

En la parte de name podemos cambiar a lo que está entre comillas a cualquiera de las opciones de la tabla de arriba (Si vamos a utilizar esta automatización de IA con cpu, solo recomiendo que usen los modelos: tiny, base y como mucho small y en cuanto a gráfica dependiendo de la cantidad de VRAM que tengamos seleccionemos un modelo u otro.)

Y en la parte de device podemos seleccionar o "cuda" o "cpu". Si tenemos gráfica con CUDA instalado dejamos "cuda", si tenemos un cpu sin gráfica o una Mac, escribimos "cpu".


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
python /Ruta/A/Tu/Script/recortes.py
deactivate
```

#### transcripts.sh:

```
source /Ruta/A/Tu/Entorno/.venv/bin/activate
python /Ruta/A/Tu/Script/transcriptions.py
deactivate
```

Haz los archivos ejecutables:

```
chmod +x recortes.sh transcripts.sh
```

Ahora puedes ejecutar los scripts con un doble clic.

