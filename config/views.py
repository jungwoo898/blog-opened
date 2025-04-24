from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)

    context = {
        "post_id": post_id,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    return render(request, "post_add.html")