from django.shortcuts import render, redirect
from .models import articles
from .forms import articlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = articles.objects.order_by('-date') #Получить все объекты
    return render(request, 'news/news_home.html', {'news': news}) #Обрабатываем запрос и возвращаем шаблон html из папки templates

class NewsDetailView(DetailView):
    model = articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView): #Это класс, который используется для обновления существующей записи.
    model = articles
    template_name = 'news/create.html'
    form_class = articlesForm

class NewsDeleteView(DeleteView): #Это класс, который используется для удаления существующей записи из базы данных.
    model = articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'

def create(request):
    error = ''
    if request.method == 'POST':
        form = articlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'


    form = articlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)