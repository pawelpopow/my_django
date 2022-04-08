from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.name}"


class Chat(models.Model):
    body = models.TextField()
    Message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.body} -  {self.Message}"