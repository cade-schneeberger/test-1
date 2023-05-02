from django.db import models

# Create your models here.

class Department(models.Model):
    dept_id = models.CharField(max_length=4, primary_key=True)
    dept_name = models.CharField(max_length=15)
    dept_location = models.CharField(max_length=15)

    def __str__(self):
        return self.dept_name
    

class Employee(models.Model):
    EMP_TYPE = (('FT', 'Full Time'),('PT', 'Part Time'), ('TE', 'Temp Emp'))
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=15)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_age = models.IntegerField()
    start_date = models.DateField()
    emp_type = models.CharField(max_length=2, choices=EMP_TYPE)
