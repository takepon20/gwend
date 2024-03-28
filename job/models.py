from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
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
    # 作成と更新
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['publish', '-created_at']
