from django.db import models


class StudentRecord(models.Model):
  fist_name         = models.CharField(max_length=50)
  last_name         = models.CharField(max_length=50)
  address           = models.CharField(max_length=100)
  dob               = models.CharField(max_length=50)
  phone             = models.CharField(max_length=50)
  email             = models.CharField(max_length=100)
  time_pref         = models.CharField(max_length=20)
  empl_status       = models.TextField()
  commitments       = models.TextField()
  problem_solving   = models.TextField() 
  data_bg           = models.TextField()
  mean_med_mode     = models.IntegerField()
  func_loop_stmt    = models.IntegerField()
  sql_knowledge     = models.IntegerField()
  job_goal          = models.TextField()
  why_data_career   = models.TextField()
  disabilities      = models.TextField()
  how_find_codeit   = models.TextField()
  laptop            = models.BooleanField()
  os_type           = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


