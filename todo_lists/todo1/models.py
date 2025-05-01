from django.db import models

# Create your models here.

class Details(models.Model):
    taskname=models.CharField(max_length=20)
    desc=models.TextField()
    date=models.DateField()
    Complete=models.BooleanField(default=False)

    def __str__(self):
        return self.taskname