from random import choices
from django.db import models

LABEL_CHOICES = (
    ('P','primary'),
    ('SE','secondary'),
    ('S','success'),
    ('D','danger'),
    ('W','warning'),
    ('I','info'),
    ('L','light'),
    ('D','dark'),
)
class Note(models.Model):
    title = models.CharField(max_length=100)
    dua_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.title
