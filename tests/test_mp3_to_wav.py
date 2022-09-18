from os import path, listdir, remove
from assertpy import assert_that
from unittest import TestCase
from src.mp3_to_wav import Mp3ToWav


class TestMp3ToWav(TestCase):

    def setUp(self) -> None:
        self.fixtures_folder = path.abspath("tests/fixtures/audio_for_test")
        self.mp3_to_wav = Mp3ToWav(self.fixtures_folder, self.fixtures_folder)
        return super().setUp()

    def tearDown(self) -> None:
        self.doCleanups()
        wav_files = [f for f in listdir(self.fixtures_folder) if f.endswith(".wav")]
        for wav in wav_files:
            remove(f"{self.fixtures_folder}/{wav}")
        return super().tearDown()

    def test_only_transforms_mp3_format(self):
        mp3_files = [f for f in listdir(self.fixtures_folder) if f.endswith(".mp3")]
        expected_files = [f.replace(".mp3", ".wav") for f in mp3_files]

        self.mp3_to_wav.transform()

        files_in_folder = [f for f in listdir(
            self.fixtures_folder) if f.endswith(".wav")]
        assert_that(expected_files).is_equal_to(files_in_folder)
