from django.db import models
from datetime import datetime

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # created_at = models.DateTimeField(default= datetime.now, blank=True)

