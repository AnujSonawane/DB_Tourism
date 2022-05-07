from django.db import models

class user1(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_opinion = models.TextField(max_length=255)
