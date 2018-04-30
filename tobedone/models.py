from django.db import models

# Create your models here.
class Tobedone(models.Model):
	text = models.CharField(max_length = 40)
	ip_address = models.CharField(max_length = 40)
	complete = models.BooleanField(default = False)

	def __str__(self):
		return self.text