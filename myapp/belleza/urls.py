from django.urls import path
from . import views

app_name = 'belleza'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('point', views.point, name='point'),
    path('commitment', views.commitment, name='commitment'),
    path('price', views.price, name='price'),
    path('questionnaireandbook', views.questionnaireandbook, name='questionnaireandbook'),
    path('staff', views.staff, name='staff'),
    path('access', views.access, name='access'),
    path('news', views.news, name='news'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'), 
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
]
