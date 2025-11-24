"""
URL configuration for jaringrd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from jaringrd import settings
from journal.sitemaps import StaticViewSitemap, PostSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
}

urlpatterns = [
    path('accounts/login/', LoginView.as_view(
        template_name='registration/login.html',
        next_page='journal:home',
        redirect_authenticated_user=True
    ), name='login'),

    path('accounts/logout/', LogoutView.as_view(next_page='journal:home'), name='logout'),

    path('admin-django/', admin.site.urls),

    path('dashboard/', include('dashboard.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('journal.urls')),
    path('about/', include('about.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
