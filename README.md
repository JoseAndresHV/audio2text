# AUDIO2TEXT
## Overview
This is a REST API built with Django that provides speech-to-text transcription services using Deepgram's speech recognition API.
The API allows users to submit audio files for transcription and retrieve the resulting text. It also provides an endpoint for retrieving all transcriptions stored in the database.

## Requirements
- Python 3.7 or higher
- Deepgram API credentials

## Setup
1. Clone the repository to your local machine:
```
git clone https://github.com/JoseAndresHV/audio2text.git
```
2. Create a virtual environment and activate it:
```
virtualenv venv
venv\Scripts\activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Set up the database:
```
python manage.py migrate
```
5. Set up Deepgram API credentials (.env)
```
echo DEEPGRAM_API_KEY=your_api_key_here > .env
```
6. Run the server
```
python manage.py runserver
```
You should now be able to access the API at http://localhost:8000.

## Endpoints
The API provides the following endpoints:
## POST /transcribe
Submits an audio file for transcription. Audio files can be uploaded using multipart/form-data and the audio key. </br>
![image](https://user-images.githubusercontent.com/30439829/225222117-a6d1dba2-4f30-4fce-a9e1-35aa5419fe9a.png)

## GET /transcriptions
Retrieves all transcriptions stored in the database.
![image](https://user-images.githubusercontent.com/30439829/225222407-b34f8249-c52b-47a5-b1c9-d8a899d7cb6b.png)

## Error handling
The API handles common errors such as missing files and incorrect file formats. If an error occurs, an appropriate error message is returned.

## Tests
This API includes a suite of automated tests to ensure that it functions correctly in a variety of scenarios. The tests are located in the tests.py file in the root of the project directory.
To run the tests, you can use the following command:
```
python manage.py test
```
