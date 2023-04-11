from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            
            # 공백으로 구분지어서 출력
            # content의 개행(\r\n)을 띄어쓰기로 변경 
                                # -> 공백을 기준으로 split
            contents = article.content.replace('\r\n',' ').split(' ')
            for content in contents:
                if content.startswith('#'):
                    # get_or_create : 
                    #       새로운 데이터는저장 / 기존에 있으면 가져와라
                    # 반환값 : 생성(조회)한 객체, 생성여부
                    hashtag, created = Hashtag.objects.get_or_create(content=content[1:]) # #을 없애주기위해 1: 을 한다
                    # created는 그냥 저장용으로 만들어준거 get or create니까
                    article.hashtags.add(hashtag)

            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user: 
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@require_POST
def likes(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')


def profile(request,username):
    # 조건에 맞는 데이터를 반환 filter이기떄문에 first()로 하나만 반환
    user = get_user_model().objects.filter(username=username).first()
    
    # 유저가 작성한 게시글
    articles = user.article_set.all()
    
    # 유저가 좋아요를 누른 게시글
    like_articles = user.like_article.all()
    context = {
        'user':user,
        'articles':articles,
        'like_articles':like_articles,
    }
    return render(request, 'articles/profile.html',context)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    # 역순으로 조회해야하기 때문에
    articles = hashtag.article_set.all().order_by('-pk')
    context = {
        'hashtag':hashtag,
        'articles':articles
    }
    return render(request, 'articles/hashtag.html',context)