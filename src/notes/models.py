from django.db import models
from django.shortcuts import redirect, reverse
# Create your models here.
LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('S', 'success'),
    ('D', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('D', 'dark')
)


class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
