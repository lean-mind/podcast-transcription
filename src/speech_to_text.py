import whisper
from os import listdir

from src.model_sizes import ModelSize


class SpeechToText:

    def __init__(self, src_folder: str, dst_folder: str):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"

    def transform(self):
        mp3_filenames = [f for f in listdir(self.src_folder) if f.endswith('.mp3')]
        for mp3_filename in mp3_filenames:
            podcast_content = self._parse_audio_into_text(mp3_filename)
            self._save_text(podcast_content, mp3_filename)

    def _parse_audio_into_text(self, mp3_filename: str) -> str:
        abs_src_path = f"{self.src_folder}{mp3_filename}"
        print(f"PARSING FILE: {mp3_filename}")
        model = whisper.load_model(ModelSize.base) # Here we select the model size
        result = model.transcribe(abs_src_path)
        print(f"PARSED FILE: {mp3_filename}")
        return result["text"]

    def _save_text(self, podcast_content: str, mp3_filename: str):
        abs_src_path = f"{self.dst_folder}{mp3_filename}".replace(".mp3", ".txt")
        with open(abs_src_path, 'w') as file:
            file.write(podcast_content)
            print(f"CONTENT SAVED ON: {abs_src_path}")
            
