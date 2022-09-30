from os import path
from src.speech_to_text import SpeechToText
from src.logger import task_logger


def main():
    _parse_speech_to_text()


@task_logger(message="----Transforming speech into text----")
def _parse_speech_to_text():
    MP3_FOLDER = path.abspath("audio_mp3_folder")
    TEXT_FOLDER = path.abspath("audio_text_folder")
    SpeechToText(MP3_FOLDER, TEXT_FOLDER).transform()


if __name__ == '__main__':
    main()
