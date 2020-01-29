from django.urls import path
# "blog"アプリの全てのビューをインポートする。
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]

# 「post_list」という名前のビューをルートURLに割り当てる。このURLパターンは空の文字列に一致する。
# Djangoはビューを見つけるとき、URLのパス（path)の前にくっつくドメイン名（つまり、"http://127.0.0.1:8000/"
# の部分）を無視する。このパターンは誰かがあなたのWebサイトの"http://127.0.0.1:8000/"というアドレスに
# アクセスした来たら「views.post_list」が正しい行き先だということをDjangoに伝える。

# 最後の「name='post_list'」は、ビューを識別するために使われるURLの名前である。これはビューと同じ名前に
#   することもできるが、全然別の名前にすることもできる。プロジェクトでは名前付けされたURLを後で使うことになるので、
#   アプリのそれぞれのURLに名前を付けておくのは重要である。