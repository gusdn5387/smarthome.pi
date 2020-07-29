from django.db import models

# Create your models here.

class LedStatus(models.Model):
    is_on = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class RoomStatus(models.Model):
    people_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
