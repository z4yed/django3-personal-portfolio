from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100)
	time = models.DateTimeField(default=datetime.now)
	description = models.TextField()

	def __str__(self):
		return self.title