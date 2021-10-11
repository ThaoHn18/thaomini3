
from typing import ContextManager
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator # Để đăng nhập song mới cho action trong web
from django.contrib.auth.decorators import login_required
from .models import Author,Book
from .forms import AuthorForm

class AuthorListView(ListView):
    # model= Author
    # queryset= Author.objects.order_by('first_name')
    # Sử dụng Listview phải định nghĩa 3 cái:
    # 1. Model
    # 2. queryset
    # 3. Override method get_queryset()

    context_object_name= "all_authors"  # doi 'object_list' thanh gia tri cua context_object_name cho de nho
    # Template mặc định mà ListView nayf hieenr thị là <tên appname>/< tên class model viết thường>_list
    # App myapp, tên model là author thì nó sẽ hiển thị template là myapp/author_list.html
    # Đổi template mặc định
    template_name= "class_base/list_view.html" # Đổi template qua 'template_name'
    #Thuộc tính để phân trang trong Listview
    paginate_by=5

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['example'] = " Hello from addtional context"
        return context

    def get_queryset(self):
        return Author.objects.all()
@method_decorator(login_required(login_url="/login"), name="dispatch")
class AuthorDetailView(DetailView):
    model = Author
    template_name= 'class_base/detail_view.html'
@method_decorator(login_required(login_url="/login"), name="dispatch")
class AuthorCreateView(CreateView):
    model= Author
    # fields= "__all__" # Không dùng cái này
    form_class=AuthorForm
    template_name = "class_base/create_view.html"
    success_url="all-author"

@method_decorator(login_required(login_url="/login"), name="dispatch")
class AuthorUpdateView(UpdateView):
    model= Author
    # fields= "__all__" # Không dùng cái này
    form_class=AuthorForm
    template_name = "class_base/update_view.html"
    success_url="all-author"
@method_decorator(login_required(login_url="/login"), name="dispatch")
class AuthorDeleteView(DeleteView):
    model= Author
    success_url="all-author"
    template_name="class_base/confirm_delete.html"

