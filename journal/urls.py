from django.urls import path

from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.home, name='home'),
    path('jurnal/', views.post_list, name='list'),
    path('jurnal/<slug:slug>/', views.post_detail, name='detail'),
]
