from os import listdir, path
from pydub import AudioSegment
from pydub.silence import split_on_silence
import wget


class WavToText:

    def __init__(self, src_folder, dst_folder):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"
        self.models_dir = f"{path.abspath('models')}/"

    def transform(self):
        self._download_spanish_model()
        wav_files = [f for f in listdir(self.src_folder) if f.endswith('.wav')]
        for wav_file in wav_files:
            self._parse_to_text(wav_file)

    def _parse_to_text(self, wav_file):
        ## TODO: Implement parsing to text format using VOSK
        abs_src_path = f"{self.src_folder}{wav_file}"
        print(self.models_dir)

    def _download_spanish_model(self):
        url = "https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip"
        files_in_folder = [f for f in listdir(self.models_dir) if not f.startswith('.')]
        if not files_in_folder:
            response = wget.download(url, self.models_dir)
            print(response)
