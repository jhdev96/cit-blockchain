from django.db import models


class StudentRecord(models.Model):
  fist_name         = models.CharField(max_length=50)
  last_name         = models.CharField(max_length=50)
  address           = models.CharField(max_length=100)
  dob               = models.CharField(max_length=50)
  phone             = models.CharField(max_length=50)
  email             = models.CharField(max_length=100)
  
  

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


