from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ArticleListSerializer
from .models import Article,Comment
from rest_framework.response import Response
from rest_framework import status
# 전체 조회, 생성
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'POST':

        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
    # GET 이라면
    articles = Article.objects.all()

    # serializer 는 쉽게 말하면 포장해 주는 것
    serializer = ArticleListSerializer(articles,many=True)
    return Response(serializer.data)
    # return JsonResponse({'message':'okay'})

# 상세 조회, 수정, 삭제
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "PUT":
        # article instance 를 파라미터로 전달
        serializer = ArticleListSerializer(article, data=request.data)
        # raise_exception=True 면 valid 하지 못할 때 바로 오류를 반환함
        # 유효성 검증 실패 시 에러를 반환 해줌
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_201_CREATED)
    serializer = ArticleListSerializer(article)

    return Response(serializer.data)
    