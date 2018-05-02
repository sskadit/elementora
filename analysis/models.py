from django.db import models

# Create your models here.
class Data(models.Model):
	id_generated = models.IntegerField(blank=True,null=True)
	text = models.CharField(max_length=1000)
	number = models.CharField(max_length=1000)
	mms = models.BooleanField()
	sender = models.BooleanField()
	datetime = models.CharField(max_length=1000)
	timestamp_client = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s,%s' % (self.id_generated,self.number)
