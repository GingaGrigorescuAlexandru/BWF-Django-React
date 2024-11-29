from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = False)
    location = models.CharField(max_length = 50, null = False)
    description = models.TextField(max_length = 255, null = False, unique = False)
    class Meta:
        unique_together = (('name', 'location'))