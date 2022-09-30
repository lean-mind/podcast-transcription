import whisper
from os import listdir

from src.model_sizes import ModelSize


class SpeechToText:

    def __init__(self, src_folder: str, dst_folder: str):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"

    def transform(self):
        filenames = [f for f in listdir(self.src_folder) if f.endswith('.mp3')]
        [self._parse_speech_to_text(filename) for filename in filenames]

    def _parse_speech_to_text(self, mp3_filename: str):
        podcast_content = self._transcribe_audio_frames(mp3_filename)
        self._save_text(podcast_content, mp3_filename)

    def _transcribe_audio_frames(self, mp3_filename: str) -> str:
        audio_absolute_path = f"{self.src_folder}{mp3_filename}"
        model = whisper.load_model(ModelSize.base)  # Here we select the model size
        result = model.transcribe(audio_absolute_path)
        return result["text"]

    def _save_text(self, podcast_content: str, mp3_filename: str):
        text_file_destination = f"{self.dst_folder}{mp3_filename}".replace(
            ".mp3", ".txt")
        with open(text_file_destination, 'w') as file:
            file.write(podcast_content)
