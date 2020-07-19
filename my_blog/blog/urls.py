from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.showArticle, name='showblog'),
    path('create/', views.createArticle, name='createblog'),
    path('update/<str:pk>/', views.updateArticle, name='updateblog'),
    path('delete/<str:pk>/', views.deleteArticle, name='deleteblog'),
    path('read/<str:pk>/', views.readArticle, name='readblog'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.Signup, name='signup'),
    # path('createauthor/', views.createAuthor, name='createauthor'),
    path('author/', views.AuthorList, name='authors'),
]