from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=9)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Chat(models.Model):
    body = models.TextField()
    category = models.CharField(max_length=64, null=True)
    data = models.DateTimeField(null=True)
    Message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Wiadomość: {self.body}, Imie: {self.Message},  Stanowisko: {self.category}, Date: {self.data}"