from django.db import models

class Process(models.Model):
	owner = models.ForeignKey('auth.User', related_name='processes', on_delete=models.CASCADE, default=None)
	name = models.CharField(max_length=200)
	type = models.TextField()
	number = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Process, self).save(*args, **kwargs)
