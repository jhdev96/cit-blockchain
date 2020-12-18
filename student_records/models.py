from django.db import models


class StudentRecord(models.Model):
  first_name        = models.CharField(max_length=50)
  last_name         = models.CharField(max_length=50)
  address           = models.CharField(max_length=100)
  dob               = models.CharField(max_length=50)
  phone             = models.CharField(max_length=50)
  email             = models.CharField(max_length=100)
  time_pref         = models.CharField(max_length=50, default="Day class")
  empl_status       = models.TextField(default="None")
  commitments       = models.TextField(default="None")
  problem_solving   = models.TextField(default="None")
  data_bg           = models.TextField(default="None")
  mean_med_mode     = models.IntegerField(default=1)
  programming_exp   = models.IntegerField(default=1)
  sql_exp           = models.IntegerField(default=1)
  job_goal          = models.CharField(max_length=100, default="Other")
  events            = models.TextField(default="None")
  other             = models.TextField(default="None")
  how_find_codeit   = models.TextField(default="None")
  has_laptop        = models.CharField(max_length=20, default="Yes")
  operating_sys     = models.CharField(max_length=100, default="Windows")
  bio               = models.TextField(default=f"Enter a bio")
 
  def __str__(self):
    return f"{self.first_name} {self.last_name}"


