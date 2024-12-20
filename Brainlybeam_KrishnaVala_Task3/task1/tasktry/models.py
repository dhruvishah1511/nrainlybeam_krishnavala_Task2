
from django.db import models

class ErrorLog(models.Model):
    message = models.TextField()
    error_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()

    def __str__(self):
        return f"{self.error_type} - {self.status_code} at {self.timestamp}"
