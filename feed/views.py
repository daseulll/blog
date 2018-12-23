from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, Hashtag
# Create your views here.

def index(request):
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = Hashtag.objects.all()
    if not category and not hashtag :
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.objects.filter(hashtag__name=hashtag)
    # category_list = set([])
    # #중복되면 안되므로 set 사용
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])
    #파이썬의 문법이므로, 외워두면 좋다.

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    # comment_list = Comment.objects.filter(article__id=article__id)
    comment_list = article.article_comments.all()
    # comment_list = article.article_comments.filter(content__choices=PERMISSION)
    hashtag_list = Hashtag.objects.all()

    ctx = {
    "article" : article,
    "comment_list" : comment_list,
    "hashtag_list" : hashtag_list,
    }
    if request.method == "GET" :
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        Comment.objects.create(
            article=article,
            username=username,
            content=content,
        )

        return HttpResponseRedirect("/{}/".format(article_id))

    return render(request, "detail.html", ctx)

def about(request):
    pass
