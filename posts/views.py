
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
#используется reverse_lazy, 
#таким образом пользователь не будет перенаправлен 
#до тех пор, пока представление не завершит удаление записи из базы данных.
class HomePage(ListView):
    model = Post
    template_name = 'index.html'
class BlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'
class BlogCreateView(CreateView): # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')
