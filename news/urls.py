from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
] 