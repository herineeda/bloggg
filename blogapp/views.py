from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})



def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'details':details})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog() #blog 함수 안에 blog 객체 설정
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋 메소드 블로그 객체를 데베에 저장해라 응용)객체.delete
    return redirect('/blog/'+str(blog.id))

def signup(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')