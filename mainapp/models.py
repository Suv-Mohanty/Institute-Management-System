from django.db import models

class Courses(models.Model):
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)
    start_date=models.DateField()
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)
    training_mode=models.CharField(max_length=100)

class FormData(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    passout=models.IntegerField()

class FeedbackData(models.Model):
    feed=models.TextField(max_length=1000)
    user_name=models.CharField(max_length=100,default='admin')
