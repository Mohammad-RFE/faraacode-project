from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    address = models.TextField()
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title