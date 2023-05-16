from django.db import models

# create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    date=models.DateTimeField()
    

    def __str__(self):
        return self.title
    








