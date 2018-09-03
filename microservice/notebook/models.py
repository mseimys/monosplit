import uuid
from django.conf import settings
from django.db import models


class Notebook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.UUIDField()
    name = models.CharField(max_length=255)


class Note(models.Model):
    notebook = models.ForeignKey(Notebook, related_name='notes', on_delete=models.CASCADE)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
