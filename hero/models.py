from django.db import models

# Create your models here.
class Hero(models.Model):
	"""
	Hero model details
	"""
	unique_id = models.IntegerField(primary_key=True) 
	first_name = models.CharField(max_length=250, null=True, blank=True)
	last_name = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.first_name