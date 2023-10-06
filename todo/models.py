import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    
    
    def time_passed(self):
        today = date.today()
        delta = today - self.created_at
        return  delta.days
