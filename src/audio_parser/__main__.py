from os import path
from audio_parser.speech_to_text import SpeechToText
from audio_parser.logger import task_logger


@task_logger(message="----Transforming speech into text----")
def main():
    MP3_FOLDER = path.abspath("data/mp3_folder")
    TEXT_FOLDER = path.abspath("data/text_folder")
    SpeechToText(MP3_FOLDER, TEXT_FOLDER).transform()


if __name__ == '__main__':
    main()
