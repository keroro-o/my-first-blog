# models.pyで作成したポストを追加、編集、削除するのに用いるファイル。

from django.contrib import admin
from .models import Post

# Register your models here.
# PostモデルをAdminページ（管理画面）上で見えるようにするために、モデルを登録する。
admin.site.register(Post)
