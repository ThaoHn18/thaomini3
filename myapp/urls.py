from myapp import user_views
from myapp.user_views import register_user
from django.conf.urls import url
# from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views # đổi tên cho khỏi trùng views dưới
from .import views # file urls.py và views.py cùng 1 folder
from .import base_class_views
urlpatterns = [
    # URl cua Ham
    url(r"^$", views.index , name="index"),   #^$ là bắt đầu và kết thúc luôn thì nó rỗngn :))
    url(r"^list-author$", views.list_author, name="list_author"),
    url(r"^add-author$",views.add_author, name='add_author'),
    url(r"^add-book$",views.add_book, name='add_book'),
    url(r"^author/(?P<author_id>[0-9]+)$",views.view_detail_author, name="view_detail_author" ),
    url(r"^update-author/(?P<author_id>[0-9]+)$", views.update_author, name= "update_author"),
    url(r"^delete-author/(?P<author_id>[0-9]+)$", views.delete_author, name= "delete_author"),
    url(r"^home$", views.home, name="home"),

    # Class Base View
    url(r"^all-author$",base_class_views.AuthorListView.as_view(), name="all-author"),
    url(r"^view-author/(?P<pk>[0-9]+)$", base_class_views.AuthorDetailView.as_view(), name='view-author'),
    url(r"^insert-author$", base_class_views.AuthorCreateView.as_view(), name='insert-author'),
    url(r"^edit-author/(?P<pk>[0-9]+)$",base_class_views.AuthorUpdateView.as_view(), name='edit-author'),
    url(r"^remove-author/(?P<pk>[0-9]+)$",base_class_views.AuthorDeleteView.as_view(), name='remove-author'),

    #User authentication/authorization
    url(r"^register$",user_views.register_user, name='register'),
    url(r"^login$",user_views.login_user, name='login'),
    url(r"^logout$", auth_views.LogoutView.as_view(next_page="/"),name='logout_user'),
    url(r"^change-password$", auth_views.PasswordChangeView.as_view(template_name="user/change_password.html"),name='change_password'),

]