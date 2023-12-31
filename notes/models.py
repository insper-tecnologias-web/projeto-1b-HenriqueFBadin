from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)

    def __str__(self):
        titulo = self.title
        id = self.id
        return f'{id}.{titulo}'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    notes = models.ManyToManyField(Note)

    def __str__(self):
        return self.name
