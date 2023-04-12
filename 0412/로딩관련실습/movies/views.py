from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# 쿼리문 보기
# 1. views.py 에서 django 내부 모듈을 이용해서 print하는 방법
# 2. Logger를 이용해서 Log로 남기는 방법

from django.db import connection
from django.db import reset_queries

@require_safe
def index(request):
    # 현재까지 사용된 모든 SQL문 안보이게 하기
    reset_queries()
    
    # movies = Movie.objects.all().order_by('-pk')
    
    # 가장 간단한 개선법
    # movies = list(Movie.objects.all().order_by('-pk'))
    
    # movies = Movie.objects.order_by('-pk')
    # 쿼리문 3번호출
    # print(movies[0].title)
    # print(movies[1].title)
    # print(movies[2].title)
    
    # 이미 movies에 대한 데이터를 가지고 있어서 쿼리가 1번만 날아감
    # for i in range(len(movies)):
    #     print(movies[i].title)
    
    # 미리 다 가져오기: 즉시 로딩(Eager Loading)
    # 정참조: select_related
    # 역참조: prefetch_related
    movies = Movie.objects.all().select_related('user').prefetch_related('comment_set').order_by('-pk')
    
    
    # RESET 후 사용한 모든 쿼리문을 query_info 변수에 할당
    query_info = connection.queries
    for query in query_info:
        print(query['sql'])

    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
            return redirect('movies:index')
    return redirect('movies:detail', movie.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)

def likes(request,movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')