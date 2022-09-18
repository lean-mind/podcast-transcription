from os import listdir, path, remove
import wget
import zipfile
import wave
import json
from vosk import Model, KaldiRecognizer


class WavToText:

    def __init__(self, src_folder, dst_folder):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"
        self.models_dir = f"{path.abspath('models')}/"

    def transform(self):
        wav_files = [f for f in listdir(self.src_folder) if f.endswith('.wav')]
        for wav_file in wav_files:
            self._parse_to_text(wav_file)

    def _parse_to_text(self, wav_file):
        self._download_spanish_model()
        model = self._build_model()
        abs_src_path = f"{self.src_folder}{wav_file}"
        self._recognize_text(model, abs_src_path)

    def _download_spanish_model(self):
        url = "https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip"
        language_models = [d for d in listdir(
            self.models_dir) if path.isdir(f"{self.models_dir}{d}")]
        if not language_models:
            file_name = "vosk-model-es.zip"
            wget.download(url, f"{self.models_dir}{file_name}")
            self._unzip_model(file_name)

    def _unzip_model(self, file_name: str) -> None:
        abs_file_path = f"{self.models_dir}{file_name}"
        with zipfile.ZipFile(abs_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.models_dir)
            remove(abs_file_path)

    def _build_model(self):
        model_name = [d for d in listdir(
            self.models_dir) if path.isdir(f"{self.models_dir}{d}")][0]
        abs_model_path = f"{self.models_dir}{model_name}"
        return Model(abs_model_path)

    def _recognize_text(self, model, abs_file_path: str) -> None:
        # TODO: look for bad performance, separate file into chunks and check with big dataset model
        recognizer = KaldiRecognizer(model, 16000)
        recognizer.SetWords(True)
        wav = wave.open(abs_file_path, "rb")
        print(wav.getnframes())
        chunk = wav.readframes(400000)
        if recognizer.AcceptWaveform(chunk):
            print(recognizer.Result())