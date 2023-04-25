from django.db import models
from django.db.models import Model, CharField, EmailField, SlugField, TextField


# Create your models here.
class ContactModel(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255, unique=True)
    slug = SlugField(max_length=255, unique=True)
    message = TextField()
    subject = CharField(max_length=255)

    def _get_unique_slug(self):
        pass
