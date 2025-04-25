from django.db import models
from django.utils import timezone

class MotionEvent(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Motion detected at {self.timestamp}"
