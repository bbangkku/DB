from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symmetiical # 너가팔로우한다고 나도팔로우해야하는거,, False 그런거 아니라는뜻
    followings = models.ManyToManyField('self',symmetrical=False, related_name='flollowes')
    pass
