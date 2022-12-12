from os import path
from video_parser.video_to_mp3 import VideoToMp3
from audio_parser.logger import task_logger

MP4_FOLDER = path.abspath("data/mp4_folder")
MP3_FOLDER = path.abspath("data/mp3_folder")


@task_logger(message="----Transforming video into audio----")
def main():
    VideoToMp3(MP4_FOLDER, MP3_FOLDER).transform()


if __name__ == '__main__':
    main()
