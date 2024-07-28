#blog/sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['blog:home', 'blog:about', 'blog:team','blog:testimonials','blog:services','blog:portfolio','blog:contact']

    def location(self, item):
        return reverse(item)