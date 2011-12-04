from django.db import models

class Center(models.Model):
    center_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __unicode__(self):
      return self.center_name

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    pass_code = models.IntegerField()
    center_id = models.ForeignKey(Center)

    def __unicode__(self):
      return self.first_name + " " + self.last_name
