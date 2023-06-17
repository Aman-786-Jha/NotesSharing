from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=NOTE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    users_shared_with = models.ManyToManyField(User, related_name='shared_notes')

    def __str__(self):
        return self.title

