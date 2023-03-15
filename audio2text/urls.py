from django.contrib import admin
from django.urls import path
from myapp.views import transcribe_view, get_all_transcriptions

urlpatterns = [
    path('transcribe/', transcribe_view, name='transcribe'),
    path('transcriptions/', get_all_transcriptions, name='transcriptions'),
    path('admin/', admin.site.urls),
]
