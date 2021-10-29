from django.urls import path
from .views import HomePage, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/', # Создаем новый маршрут
    BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',
    BlogUpdateView.as_view(), name='post_edit'), # Новый маршрут
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePage.as_view(),name='index')
]
