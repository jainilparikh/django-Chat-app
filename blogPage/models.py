from django.db import models

class Language(models.Model):
    lan1 = models.TextField()
    name = models.TextField()


class Message(models.Model):
    sender = models.TextField()
    receiver = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)