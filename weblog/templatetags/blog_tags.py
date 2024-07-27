from django import template
from weblog.models import Post
from weblog.models import Category
from weblog.views import blog_search
register=template.Library()
   
@register.inclusion_tag("blog/blog-latestpost.html")
def latestpost():
    posts=Post.objects.filter(status=1).order_by("published_date")[:5]
    return {"posts": posts}

@register.inclusion_tag("blog/blog-post-ctegories.html")
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cate_dict={}
    for name in categories:
       cate_dict[name]=posts.filter(category=name).count()
    return {"categries":cate_dict}

