import os
from moviepy.editor import VideoFileClip

# Obtenemos la ruta absoluta del directorio actual
current_path = os.path.abspath(".")

# Definimos la ruta de entrada relativa al directorio actual
video_path = os.path.join(current_path, "input", "video.mp4")

# Cargamos el video
print("Cargando video...")
video = VideoFileClip(video_path)
print("Video cargado.")

# Calculamos la duración del video en segundos
total_duration = int(video.duration)

# Definimos la duración deseada para cada fragmento en segundos (3 minutos = 180 segundos)
fragment_duration = 180

# Definimos la ruta de salida para los archivos de audio
output_path = os.path.join(current_path, "output")

# Creamos la carpeta de salida si no existe
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Inicializamos el tiempo inicial y final para el primer fragmento
start_time = 0
end_time = fragment_duration

# Mientras no hayamos llegado al final del video
while end_time <= total_duration:
    # Extraemos el fragmento de video en el intervalo de tiempo definido
    print(f"Extrayendo fragmento {start_time}-{end_time}...")
    fragment = video.subclip(start_time, end_time)

    # Extraemos el audio del fragmento de video y lo guardamos en un archivo MP3
    file_name = f"audio_{start_time}-{end_time}.mp3"
    file_path = os.path.join(output_path, file_name)
    try:
        audio_fragment = fragment.audio
        audio_fragment.write_audiofile(file_path)
        print(f"Fragmento {start_time}-{end_time} procesado correctamente.")
    except Exception as e:
        print(f"Error procesando fragmento {start_time}-{end_time}: {e}")

    # Actualizamos los tiempos para el siguiente fragmento
    start_time = end_time
    end_time += fragment_duration

# Si el último fragmento no tiene la duración completa, extraemos el audio restante
if start_time < total_duration:
    print(f"Extrayendo fragmento {start_time}-{total_duration}...")
    final_fragment = video.subclip(start_time, total_duration)
    file_name = f"audio_{start_time}-{total_duration}.mp3"
    file_path = os.path.join(output_path, file_name)
    try:
        final_fragment.audio.write_audiofile(file_path)
        print(f"Fragmento {start_time}-{total_duration} procesado correctamente.")
    except Exception as e:
        print(f"Error procesando fragmento {start_time}-{total_duration}: {e}")

print("Proceso completado.")
