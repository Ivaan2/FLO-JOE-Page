from django.db import models

# Create your models here.
class PhrasalVerb(models.Model):
    verb = models.CharField(max_length=200)
    definition = models.TextField(max_length=200)
    traduction = models.TextField(max_length=200)
    example = models.TextField(max_length=200)

    def __str__(self):
        return self.verb