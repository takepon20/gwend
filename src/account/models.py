from django.contrib.auth.models import AbstractUser
from django.db import models

# カスタムしたUserモデル
class CustomUser(AbstractUser):
    STATES_CHOICES = (
    ('employer', 'employer'),
    ('worker', 'worker'),
    )
    states = models.CharField(max_length=50, choices=STATES_CHOICES, default='')
