from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cat

def home(request):
    cats = Cat.objects
    cat_list=Cat.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(cat_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'cats':cats, 'posts':posts})
# Create your views here.
