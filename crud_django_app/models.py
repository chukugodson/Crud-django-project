from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	
	def __str__(self) -> str:
		return self.username


class Comment(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=244, blank=True, null=False)
	text = models.TextField(blank=True, null=False)
	date_published = models.DateTimeField(default=timezone.now)

	def __str__(self) -> str:
		return f"{self.user.username}'s comment"
