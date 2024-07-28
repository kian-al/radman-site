#weblog/sitemaps.py
from django.contrib.sitemaps import Sitemap
from weblog.models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
        return reverse('weblog:blog_single',kwargs={'pid':item.id})
