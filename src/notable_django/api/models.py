from django.db import models

# Create your models here.
# api/models.py
class Note(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): 
		return '{} : {}'.format(self.title, self.body)
		#return(self.title + " : " + self.body)