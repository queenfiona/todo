from django.db import models

class Todo(models.Model):
	item = models.CharField(max_length=100,blank=True,default='')

	
