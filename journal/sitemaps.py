from django.contrib import sitemaps
from django.urls import reverse

from .models import Post


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['journal:home', 'journal:list', 'about:index', 'about:circles']

    def location(self, item):
        return reverse(item)


class PostSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at
