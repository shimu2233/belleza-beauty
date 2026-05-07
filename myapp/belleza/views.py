from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm
from django.shortcuts import render, get_object_or_404, redirect

class IndexView(generic.ListView):
    model = Shop

class DetailView(generic.DetailView):
    model = Shop

class CreateView(generic.edit.CreateView):
    model = Shop
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Shop
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('belleza:index')

def point(request):
    return render(request, 'belleza/point.html',)

def commitment(request):
    return render(request, 'belleza/commitment.html',)

def price(request):
    return render(request, 'belleza/price.html',)

def questionnaireandbook(request):
    return render(request, 'belleza/questionnaireandbook.html',)

def staff(request):
    return render(request, 'belleza/staff.html',)

def news(request):
    news_data = News.objects.all().order_by('-id')
    return render(request, 'belleza/news.html', {'news_list': news_data})

def access(request):
    return render(request, 'belleza/access.html',)

def news_list(request):
    news_items = News.objects.all().order_by('-id')
    return render(request, 'belleza/news_list.html', {'news_list': news_items})

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/belleza/news') 
    
    else:
        form = NewsForm() 
    return render(request, 'belleza/news_form.html', {'form': form, 'title': '新規投稿'})

@login_required
def news_edit(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('/belleza/news')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'belleza/news_form.html', {'form': form, 'title': '記事の編集'})

@login_required
def news_delete(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_item.delete()
        return redirect('/belleza/news')
    return render(request, 'belleza/news_confirm_delete.html', {'news_item': news_item})
