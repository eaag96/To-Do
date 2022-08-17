from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=30, verbose_name="Title")
    description=models.TextField(verbose_name="Description")
    complete=models.BooleanField(verbose_name="Complete",default=False)