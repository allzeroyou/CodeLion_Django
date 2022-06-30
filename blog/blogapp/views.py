from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.
def home(request):
  # 블로그 글들을 모조리 띄우는 코드
  posts= Blog.objects.all()
  Blog.objects.filter().order_by('date')

  return render(request, 'index.html', {'posts': posts})

# 글 작성하는 new 함수
def new(request):
  return render(request, 'new.html')

# 글 작성 html을 보여주는 함수 create
def create(request):
  if(request.method=='POST'):
    post=Blog()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    post.save()

  return redirect('home')

# django form을 이용해 입력값을 받는 함수
# 장고는 get/post 요청 둘다 처리가 가능하다!
# get요청 => 입력값을 받을 수 있는 html을 갖다 줘야!
# post요청 => 입력한 내용을 데이터 베이스에 저장 즉, form에서 입력한 내용 처리

def formcreate(request):
  # 입력을 받을 수 있는 html을 갖다주기
  if request.method == 'POST':
    form = BlogForm(request.POST)
    if form.is_valid(): # 유효 검사
      post = Blog()
      post.title = form.cleaned_data['title']
      post.body = form.cleaned_data['body']
      post.save()
      return redirect('home')
  else:
    form = BlogForm()
  return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
  # 입력을 받을 수 있는 html을 갖다주기
  if request.method == 'POST':
    form = BlogModelForm(request.POST)
    if form.is_valid(): # 유효 검사
      form.save()
      return redirect('home')
  else:
    form = BlogModelForm()
  return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
  # blog_id 번째 블로그 글을 데이터베이스로부터 가져와서 detail.html로 띄워주는 코드
  blog_detail = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'detail.html', {'detail':blog_detail})
