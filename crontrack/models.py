from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField

class Job(models.Model):
	schedule_str = models.CharField('cron schedule string', max_length=100)
	name = models.CharField(max_length=50)
	time_window = models.IntegerField('time window (minutes)', default=0)
	next_run = models.DateTimeField('next time to run')
	last_notified = models.DateTimeField('last time notification received')
	description = models.CharField(max_length=200, blank=True, default='')
	user = models.ForeignKey(User, models.CASCADE)
	
	def __str__(self):
		return f'{self.user}\'s {self.name}: "{self.schedule_str}", {self.description}'
		
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	timezone = TimeZoneField(default='UTC')