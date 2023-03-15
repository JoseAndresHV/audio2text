from django.test import TestCase
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os


class TranscribeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/transcribe/'

    def test_transcribe_with_valid_audio_mp3(self):
        # Load test audio file
        audio_file_path = os.path.join(
            settings.BASE_DIR, 'audio2text', 'static', 'test_files', 'test_audio.mp3')
        audio_file = open(audio_file_path, 'rb')
        audio_content = audio_file.read()
        audio_file.close()
        audio_file = SimpleUploadedFile(
            "test_audio.mp3", audio_content, content_type="audio/mpeg")

        # Make request to transcribe view with test audio file
        response = self.client.post(
            '/transcribe/', {'audio': audio_file}, format='multipart')

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertIn('text', response.json())

    def test_transcribe_with_valid_audio_wav(self):
        # Load test audio file
        audio_file_path = os.path.join(
            settings.BASE_DIR, 'audio2text', 'static', 'test_files', 'test_audio.wav')
        audio_file = open(audio_file_path, 'rb')
        audio_content = audio_file.read()
        audio_file.close()
        audio_file = SimpleUploadedFile(
            "test_audio.wav", audio_content, content_type="audio/wave")

        # Make request to transcribe view with test audio file
        response = self.client.post(
            '/transcribe/', {'audio': audio_file}, format='multipart')

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertIn('text', response.json())

    def test_transcribe_with_valid_audio_ogg(self):
        # Load test audio file
        audio_file_path = os.path.join(
            settings.BASE_DIR, 'audio2text', 'static', 'test_files', 'test_audio.ogg')
        audio_file = open(audio_file_path, 'rb')
        audio_content = audio_file.read()
        audio_file.close()
        audio_file = SimpleUploadedFile(
            "test_audio.ogg", audio_content, content_type="audio/ogg")

        # Make request to transcribe view with test audio file
        response = self.client.post(
            '/transcribe/', {'audio': audio_file}, format='multipart')

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertIn('text', response.json())

    def test_transcribe_view_with_invalid_payload(self):
        # Load test audio file
        invalid_payload = {'foo': 'bar'}

        # Make request to transcribe view with test audio file
        response = self.client.post(self.url, data=invalid_payload)

        # Check response
        self.assertEqual(response.status_code, 400)

    def test_transcribe_view_with_invalid_file_format(self):
        # Load test audio file
        invalid_file = SimpleUploadedFile(
            "test_audio.txt",
            b"file_content",
            content_type="text/plain"
        )
        payload = {'audio': invalid_file}

        # Make request to transcribe view with test audio file
        response = self.client.post(self.url, data=payload)

        # Check response
        self.assertEqual(response.status_code, 400)
