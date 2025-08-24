from django.db import models

class Footer(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    whatsapp = models.CharField(max_length=40)
    telegram = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)


class MessageForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    message = models.TextField()