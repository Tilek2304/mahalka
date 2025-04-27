from django.db import models

class RobotStatus(models.Model):
    command = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)