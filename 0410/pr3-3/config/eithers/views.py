from django.shortcuts import render,redirect
from .models import Question, Comment
from .forms import QuestionForm,CommentForm
import random as ra
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions':questions,}
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
        pass
    
    # GET일 때 create.html 을 사용자에게 보여줌

    form = QuestionForm()
    context = {
        'form':form,
    }    
    return render(request,'eithers/create.html',context)

def detail(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    # 역참조
    comments = question.comments.all()
    comment_form = CommentForm()
    context = {
        'question':question,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'eithers/detail.html',context)

# 댓글 생성
def comment(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 사용자가 직접 question을 입력하지 않으므로
        # views.py에 지정해준 후 저장
        comment = form.save(commit=False) # DB에는 반영XXX
        comment.question = question
        comment.save()
        return redirect('eithers:detail',question_pk)
    

from django.db.models import Max

def random(request):
    # 있는지 없는지부터,,
    # count = Question.objects.count()
    # if count <= 0:
    #     return redirect('eithers:index')
    
    # random = Question.list_pk()
    # random_page = random.chice(random)

    # 이거는 전체를 가져오는거,, python에서 선택하는거
    # question = ra.choice(Question.objects.all())

    # 이거는 DB가 정렬 후 하나만 장고로 !! 오는거
    # question = Question.objects.order_by('?').first()

    # 데이터가 적을 때 일반적으로 사용하는 방법
    # max_id 기준으로 randint 사용하기
    max_id = Question.objects.all().aggregate(max_id=Max('id'))['max_id']
    question_pk = ra.randint(1,max_id)
    if Question.objects.filter(pk=question_pk).exists():
        return redirect('eithers:detail', question_pk)
    
    else:
        return redirect('eithers:random')
    
    # context = {
    #     'question':question,
    # }
    # return render(request,'eithers:detail',context)