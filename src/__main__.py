from src.mp3_to_wav import Mp3ToWav
from os import path

from src.wav_to_text import WavToText

MP3_FOLDER = path.abspath("audio_mp3_folder")
WAV_FOLDER = path.abspath("audio_wav_folder")
TEXT_FOLDER = path.abspath("audio_text_folder")

def main():
    # _parse_mp3_to_wav()
    _parse_wav_to_text()


def _parse_mp3_to_wav():
    message = "Transforming mp3 into wav"
    print(f"START: {message}")
    Mp3ToWav(MP3_FOLDER, WAV_FOLDER).transform()
    print(f"FINISH: {message}")


def _parse_wav_to_text():
    message = "Transforming wav into text"
    print(f"START: {message}")
    WavToText(WAV_FOLDER, TEXT_FOLDER).transform()
    print(f"FINISH: {message}")

if __name__ == '__main__':
    main()
