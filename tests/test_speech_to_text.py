from unittest import TestCase
from assertpy import assert_that
from os import listdir, remove
from src.speech_to_text import SpeechToText


class TestSpeechToText(TestCase):

    def setUp(self) -> None:
        self.src_folder = "tests/fixtures"
        self.dst_folder = "tests/fixtures"
        self.speech_to_text = SpeechToText(
            self.src_folder,
            self.dst_folder
        )
        return super().setUp()

    def tearDown(self) -> None:
        [remove(f"{self.dst_folder}/{f}") for f in listdir(
            f"{self.dst_folder}/") if f.endswith('.txt')]
        return super().tearDown()

    def test_conversion_only_takes_mp3_files(self):
        self.speech_to_text.transform()

        dir_txt_files = [f for f in listdir(
            f"{self.dst_folder}/") if f.endswith('.txt')]
        mp3_files = [f for f in listdir(
            f"{self.src_folder}/") if f.endswith('.mp3')]
        expected_txt_files = [f.replace(
            ".mp3", ".txt") for f in mp3_files]
        
        assert_that(dir_txt_files).is_equal_to(expected_txt_files)
        
    def test_conversion_returns_not_empty_files_when_someone_talk(self):
        self.speech_to_text.transform()

        result_files = [f for f in listdir(
            f"{self.dst_folder}/") if f.endswith('.txt')]
        
        with open(f"{self.dst_folder}/{result_files[0]}", 'r') as file:
            content = file.read()
        
        assert_that(content).is_not_empty()
