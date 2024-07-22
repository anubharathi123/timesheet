from django.db import models

class EmployeeDetail(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    project_name = models.CharField(max_length=100)
    date = models.DateField()
    comments = models.TextField()
    lead_approval = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending')

    def __str__(self):
        return self.name

class TimeSheet(models.Model):
    employee = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    week = models.CharField(max_length=20)
    mon = models.IntegerField()
    tue = models.IntegerField()
    wed = models.IntegerField()
    thu = models.IntegerField()
    fri = models.IntegerField()
    total = models.IntegerField()
    lead_approval = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending')

    def calculate(self, *args, **kwargs):
        self.total = self.mon + self.tue + self.wed + self.thu + self.fri - 5
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.week}"
