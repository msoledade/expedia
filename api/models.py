from django.db import models

class Process(models.Model):
	name = models.CharField(max_length=200)
	type = models.TextField()
	number = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	        return self.name
