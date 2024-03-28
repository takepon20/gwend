from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Academic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    publish = models.BooleanField(default=False)
    # 学校情報
    school = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hp = models.URLField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    admission_date = models.DateField(default=timezone.now)
    graduation_date = models.DateField(default=timezone.now)
    description = models.TextField()
    # 作成と更新
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school
    class Meta:
        ordering = ['-created_at']

class Work(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    publish = models.BooleanField(default=False)
    # 会社情報
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    hp = models.URLField()
    # 仕事内容
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    joining_date = models.DateField(default=timezone.now)
    leaving_date = models.DateField(default=timezone.now)
    # 作成と更新
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

