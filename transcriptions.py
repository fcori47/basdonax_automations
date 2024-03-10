import os
import whisper
from whisper.utils import get_writer 


def transcribir_videos(path, destino_transcripciones):
    archivos_videos = [archivo for archivo in os.listdir(path) if archivo.endswith((".mp4", ".mkv"))]
    for video in archivos_videos:
        ruta_video = os.path.join(path, video)
        nombre_video, extension = os.path.splitext(video)
        destino_srt = os.path.join(destino_transcripciones, f"{nombre_video}.srt")

        if os.path.exists(destino_srt):
            print(f"El archivo {nombre_video}.srt ya existe en el destino, omitiendo.")
            continue

        model = whisper.load_model(name='medium', device='cuda')
        result = model.transcribe(audio=ruta_video, language='Spanish', word_timestamps=True, task="transcribe")

        word_options = {
            "highlight_words": False,
            "max_line_count": 1,
            "max_words_per_line": 1
        }
        vtt_writer = get_writer(output_format='srt', output_dir=destino_transcripciones)
        vtt_writer(result, ruta_video, word_options)
        print(f"Archivo {nombre_video}.srt guardado en {destino_transcripciones}.")


if __name__ == "__main__":
    path_videos = r'D:\yt\rawshorts'
    destino_transcripciones = r'D:\yt\transcripciones'
    
    if not os.path.exists(destino_transcripciones):
        os.makedirs(destino_transcripciones)

    transcribir_videos(path_videos, destino_transcripciones)
