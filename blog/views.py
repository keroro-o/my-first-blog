from django.shortcuts import render
from django.utils import timezone
from .models import Post

posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# Create your views here.
def post_list(request):
    """
    requestを引数にとる。「blog/post_list.html」テンプレートを（色々なものを合わせて）
    組み立てる「render関数」を呼び出して得た値を返す関数。
    """
    # クエリセットを変数"posts"に代入。
    posts = Post.objects.filter(published_date__lte=timezone.now()).orderd_by("published_date")

    return render(request, "blog/post_list.html", {"posts": posts})



#★ビューはアプリのロジックを書いていくところである。ビューは、以前あなたが作った、モデルに
#   情報を要求し、それを「テンプレート」に渡す。テンプレートはこの後作る。

#★実際のところ、PostをどうやってHTMLファイルにしゅつりょくすればいいのでしょうか？
#   大まかなイメージとしては、データベースに保存された記事を取り出して、テンプレートのHTMLファイルの中に
#   行儀よく並べれば良さそう。
#  正確には、ビューがモデルとテンプレートの橋渡しをしてくれる。私たちが作業している"post_list"ビューの場合、
#   表示したいデータを取り出して、テンプレートファイルに渡すことになる。どのモデルのデータを、どのテンプレートに
#   表示させるかを、ビューに記述する。
