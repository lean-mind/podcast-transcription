# Imagen base de Python
FROM python:3.9-slim-buster

# Copiamos el script y el video a la imagen
COPY input /app/input
COPY video_to_audio.py /app/video_to_audio.py

# Instalamos las bibliotecas necesarias
RUN pip install moviepy

# Definimos la carpeta de trabajo
WORKDIR /app

# Ejecutamos el script al iniciar el contenedor
CMD ["python", "video_to_audio.py"]



