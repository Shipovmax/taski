from django.db import models


class Task(models.Model):
    """A single to-do item with a title, description, and status flag."""

    title = models.CharField(verbose_name='Title', max_length=120)
    description = models.TextField(verbose_name='Description')
    completed = models.BooleanField(verbose_name='Completed', default=False)

    def __str__(self) -> str:
        return self.title
