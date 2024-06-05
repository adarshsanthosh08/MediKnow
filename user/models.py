from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    rawtext = models.TextField()
    result = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user_name} - {self.rawtext} - {self.datetime}"
    
    
