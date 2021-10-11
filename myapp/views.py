from django.core import paginator
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from django.http import HttpResponse, request
from django.core.paginator import Page, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Book,Author
from .forms import AuthorForm, Bookform
# Create your views here.
def index(request): # Tham số bắt buộc phải có các hàm views.py 
    # # là resquest : httpresquest
    # print(request.GET['name']) #request.get nằm trên url khi mình gõ
    # name= request.GET.get('name','')
    # request.session['name'] = name
    # response= HttpResponse()
    # response.write("<h1> Alo Hello Thao</h1>")
    # response.write("Đây là app đầu tiên của Thao")
 
    # age=12
    # name="Alice"
    all_authors=Author.objects.all()
    return render(
        request=request,
        template_name="index.html",
    )
def home(request):
    name= request.session.get('name','')
    return HttpResponse('Hello' + name)

def list_author(request):
    all_authors= Author.objects.all()
    # paginator=Paginator(all_authors,5)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    search=request.GET.get('search')
    if search:
        all_authors=all_authors.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        # print(all_authors)
    return render(
        request=request,
        template_name="author/list.html",
        context={
            'all_authors':all_authors
        }
    )

@login_required(login_url="/login") # Dat decorator "login_required" bắt người dùng phải đăng nhập
def add_author(request):
    author_form=AuthorForm()
    if request.method == "POST":
        print(request.POST)
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():   # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu clean_
            print("Form validate OK")
            data = author_form.cleaned_data # cleand_data trong is_valid. tý bật lên sau
            author_form.save()
            return redirect("index")
    return render(
        request=request,
        template_name='author/add.html',
        context={
            'form': author_form
        }
    )
@login_required(login_url="/login")
def add_book(request):
    form_book = Bookform()
    if request.method == "POST":
        print(request.POST)
        form_book = Bookform(request.POST)
        if form_book.is_valid():   # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu clean_
            print("Form validate OK")
            data = form_book.cleaned_data # cleand_data trong is_valid. tý bật lên sau
            form_book.save()
            return redirect("index")
    return render(
        request=request,
        template_name='book/add.html',
        context={
            'form': form_book
        }
    )
@login_required(login_url="/login")
def view_detail_author(request, author_id):
    author_data = Author.objects.get(id=author_id)
    return render(
        request=request,
        template_name= 'author/detail.html',
        context={
            'author': author_data
        }
    )
@login_required(login_url="/login")
def update_author(request, author_id):
    author_data = get_object_or_404(Author,id=author_id)
    author_form=AuthorForm(instance=author_data)
    if request.method == 'POST':
        author_data.first_name = request.POST.get('first_name',author_data.first_name)
        author_data.last_name = request.POST.get('last_name',author_data.last_name)
        author_data.email = request.POST.get('email',author_data.email)
        author_data.save()
        return redirect ("index")
    return render(
        request=request,
        template_name='author/update.html',
        context={
            'form': author_form
        }

    )
@login_required(login_url="/login")
def delete_author(request, author_id):
     author_data = get_object_or_404(Author,id=author_id)
     author_data.delete()
     return redirect ("index")