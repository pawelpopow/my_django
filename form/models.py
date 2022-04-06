from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    body = models.TextField()

    def __str__(self):
        return f"{self.name}"
