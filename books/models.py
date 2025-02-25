from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re

def validate_isbn(value):
    if not re.fullmatch(r'\d{10}|\d{13}', value):
        raise ValidationError()

def validate_publication_date(value):
    if value > date.today():
        raise ValidationError()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(validators=[validate_publication_date])
    isbn = models.CharField(max_length=13, unique=True, validators=[validate_isbn])
    summary = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
