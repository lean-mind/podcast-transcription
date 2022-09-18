from os import listdir
from pydub import AudioSegment


class Mp3ToWav:

    def __init__(self, src_folder: str, dst_folder: str):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"
        
    def transform(self):
        mp3_files = [f for f in listdir(self.src_folder) if f.endswith('.mp3')]
        for mp3_file in mp3_files:
            self._parse_mp3_to_wav(mp3_file)
            
    def _parse_mp3_to_wav(self, mp3_file: str):
        abs_src_path = f"{self.src_folder}{mp3_file}"
        abs_dst_path = f"{self.dst_folder}{mp3_file.replace('.mp3', '.wav')}"
        audio = AudioSegment.from_mp3(abs_src_path)
        audio.export(abs_dst_path, format="wav")
        print(f"- Transformed: {mp3_file}")