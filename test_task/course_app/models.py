from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    auto_increment_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    lecture_number = models.IntegerField()