from src.mp3_to_wav import Mp3ToWav
from os import path


def main():
    src_folder = path.abspath("audio_mp3_folder")
    dst_folder = path.abspath("audio_wav_folder")
    Mp3ToWav(src_folder, dst_folder).transform()


if __name__ == '__main__':
    main()
