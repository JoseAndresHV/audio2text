from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseBadRequest
from deepgram import Deepgram
from django.conf import settings

from myapp.models import Transcription


@csrf_exempt
def transcribe_view(request):
    """
    API endpoint that transcribes an audio file into text using the Deepgram API.

    This API accepts a POST request with a file parameter named 'audio' containing an audio file in MP3, WAV, or OGG format.
    The Deepgram API is used to transcribe the audio file into text. The text is returned as a JSON response in the format {'text': transcription_text}.

    Example usage:
    curl -X POST -H "Content-Type: multipart/form-data" -F "audio=@/path/to/audio_file.mp3" http://localhost:8000/transcribe/

    Returns:
    - 200 OK with a JSON response containing the transcribed text.
    - 400 Bad Request if the request is invalid or the audio file format is not supported.
    """

    if request.method == 'POST' and request.FILES:
        try:
            audio_file = request.FILES['audio']
            if audio_file.content_type not in ['audio/mpeg', 'audio/wave', 'audio/ogg']:
                raise ValidationError('Invalid audio file format')
        except (KeyError, ValidationError):
            return HttpResponseBadRequest('Error: No audio file found in the request.')

        deepgram_client = Deepgram(settings.DEEPGRAM_API_KEY)
        source = {'buffer': audio_file, 'mimetype': audio_file.content_type}
        options = {"punctuate": True, "model": "general",
                   "language": "en-US", "tier": "enhanced"}

        response = deepgram_client.transcription.sync_prerecorded(
            source, options)
        transcribed_text = response['results']['channels'][0]['alternatives'][0]['transcript']

        transcription = Transcription(text=transcribed_text)
        transcription.save()

        return JsonResponse({'text': transcribed_text})
    else:
        return HttpResponseBadRequest('Error: Invalid request method.')


def get_all_transcriptions(request):
    """
    Retrieve all transcriptions from the database and return them as a JSON response.

    This view function retrieves all `Transcription` objects from the database and returns them as a JSON
    response. Each `Transcription` object is represented as a dictionary with keys `id` and `text`.
    The response is sorted in descending order by `id`.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: A JSON response containing all transcriptions in the database.

    Raises:
    None
    """
    if request.method == 'GET':
        transcriptions = Transcription.objects.all()

        data = {
            'transcriptions': [
                {
                    'id': transcription.id,
                    'text': transcription.text,
                    'created_at': transcription.date_created
                }
                for transcription in transcriptions
            ]
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
