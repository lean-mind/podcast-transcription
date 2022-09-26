from os import path
from src.speech_to_text import SpeechToText

MP3_FOLDER = path.abspath("audio_mp3_folder")
TEXT_FOLDER = path.abspath("audio_text_folder")

def main():
    _parse_speech_to_text()
    
def _parse_speech_to_text():
    message = "----Transforming speech into text----"
    print(f"START: {message}")
    SpeechToText(MP3_FOLDER, TEXT_FOLDER).transform()
    print(f"FINISH: {message}")

if __name__ == '__main__':
    main()
