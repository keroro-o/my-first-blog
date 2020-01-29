from django.shortcuts import render

# Create your views here.
def post_list(request):
    """
    requestを引数にとる。「blog/post_list.html」テンプレートを（色々なものを合わせて）
    組み立てる「render関数」を呼び出して得た値を返す関数。
    """
    return render(request, "blog/post_list.html", {})



# ビューはアプリのロジックを書いていくところである。ビューは、以前あなたが作った、モデルに
#   情報を要求し、それを「テンプレート」に渡す。テンプレートはこの後作る。