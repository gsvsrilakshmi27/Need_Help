from django.db import models

# Create your models here.
class Donor(models.Model):
	donar_name = models.CharField(max_length = 25)
	blood_group = models.CharField(max_length = 20)
	city_name = models.CharField(max_length = 20)
	mobile_number = models.BigIntegerField()
	password = models.CharField(max_length = 20)
	def __unicode__(self):              
		return self.donar_name 
