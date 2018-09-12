import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from services.notebook import Notebook

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def notebooks(self):
        return Notebook.get_notebooks(self.uuid)
