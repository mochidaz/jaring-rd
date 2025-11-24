from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('posts/', views.post_list, name='post_list'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('posts/delete/<int:pk>/', views.post_delete, name='post_delete'),

    path('circles/', views.circle_list, name='circle_list'),
    path('circles/new/', views.circle_create, name='circle_create'),
    path('circles/edit/<int:pk>/', views.circle_edit, name='circle_edit'),
    path('circles/delete/<int:pk>/', views.circle_delete, name='circle_delete'),
]
