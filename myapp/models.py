from django.db import models

class Transcription(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'myapp'