from django.db import models

# Create your models here.

class Todo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
