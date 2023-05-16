from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField()
    priority = models.IntegerField()