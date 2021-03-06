# このファイル（"models.py)で「Model」と呼ばれるオブジェクトを全て定義する。
#   これが「ブログポスト」を定義する場所となる。

from django.conf import settings
from django.db import models
from django.utils import timezone

# ブログポストモデルの定義
class Post(models.Model):
    objects = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ブログを公開するメソッド。"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


