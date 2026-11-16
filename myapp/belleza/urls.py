from django.urls import path
from . import views

app_name = 'belleza'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('point', views.point, name='point'),
    path('commitment', views.commitment, name='commitment'),
    path('price', views.price, name='price'),
    path('questionnaireandbook', views.questionnaireandbook, name='questionnaireandbook'),
    path('access', views.access, name='access'),
    path('news', views.news, name='news'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'), 
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
]
