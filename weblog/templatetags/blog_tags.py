from django import template
from weblog.models import post,Category
register=template.Library()

@register.simple_tag(name="posts")
def counterposts():
    posts=post.objects.filter(status=1).count()
    return posts
    
@register.inclusion_tag("blog/latestpost.html")
def latestpost():
    posts=post.objects.filter(status=1).order_by("published_date")[:4]
    return {"posts": posts}

@register.inclusion_tag("blog/post_categorys.html")
def postcategories():
    posts=post.objects.filter(status=1)
    categories=Category.objects.all()
    cate_dict={}
    for name in categories:
       cate_dict[name]=posts.filter(Category=name).count()
    return {"categries":cate_dict}
    