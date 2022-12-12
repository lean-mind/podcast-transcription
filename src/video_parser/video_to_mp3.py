from os import listdir
import moviepy.editor as mp


class VideoToMp3:

    def __init__(self, src_folder: str, dst_folder: str):
        self.src_folder = f"{src_folder}/"
        self.dst_folder = f"{dst_folder}/"

    def transform(self):
        videos = [f for f in listdir(self.src_folder) if f.endswith('.mp4')]
        [self._parse(v) for v in videos]

    def _parse(self, mp3_filename: str):
        video_absolute_path = f"{self.src_folder}{mp3_filename}"
        print(f"PARSING: {video_absolute_path}")
        clip = mp.AudioFileClip(video_absolute_path)
        destination = f"{self.dst_folder}{mp3_filename}".replace(".mp4", ".mp3")
        print(f"SAVING: {destination}")
        clip.write_audiofile(destination)
