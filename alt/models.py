from django.db import models

# Create your models here.

class UserModel(models.Model):   
    users = models.Manager()
    employee_id = models.CharField(max_length=9, primary_key=True)
    employee_iex_id = models.CharField(max_length=7)
    employee_name = models.CharField(max_length=255)
    employee_wave = models.CharField(max_length=8)
    employee_team_leader = models.CharField(max_length=255)
    employee_manager = models.CharField(max_length=255)
    employee_hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee_id}_{self.employee_name}"