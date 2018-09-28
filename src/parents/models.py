from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_parent = models.BooleanField(default=False)


class ParentStudent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	bio = models.CharField(max_length=120)
	location = models.CharField(max_length=120)
	school = models.ForeignKey('School',
        on_delete=models.CASCADE,)