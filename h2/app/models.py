from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.IntegerField
    UserName = models.CharField(max_length=40)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    Age = models.IntegerField()
    Height = models.FloatField(max_length=200)
    Weight = models.FloatField(max_length=200)
    Gender = models.FloatField(max_length=200)
    Ethnicity = models.FloatField(max_length=200)
    Hydration = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user.username


# class MyModel(models.Model):
#     Ethnicity = models.IntegerField()
#     Gender = models.IntegerField()
#     AgeGroup = models.IntegerField()
#     BMI = models.FloatField(max_length=200)
#     Hydration = models.FloatField()
#
#     class Meta:
#         db_table = 'hyd'


class Image1(models.Model):
    image_data = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=40)
    user_id = models.IntegerField
    date = models.DateTimeField()
    activity = models.IntegerField()
    work_time = models.IntegerField()
    Hydration = models.FloatField()

    def __str__(self):
        return self.user.username
