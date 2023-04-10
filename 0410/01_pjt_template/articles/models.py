from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 작성한 유저
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 좋아요
    # like_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='like_articles')
    # related_name의 장점
    # 1. 가독성(_set 쓰기 싫을 경우) (선택사항)
    # 2. 역참조 이름 겹치는 경우 (필수사항)
    # 
    # 유저입장
    # 내가 작성한 게시글 역참조
    # user.article_set.title

    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

# 댓글 > 게시글 정참조
# 게시글 > 댓글로  역참조

# 정참조 : 외래키를 가지고 있는 쪽에서 참조하는 방법
#comment.article.~~~
# 역참조 : 참조당하는 쪽에서 데이터를 조회하는 방법
#article = Article.objects.get(pk=article_pk)
#article.comment_set.all()
#article.comment_set.filter() 등등
## > > 모델명.set

# 이렇게 적으면 안됨 ! (인스턴스에서참조를해야지 클래스에서 참조 XX)
#Comment.article.title