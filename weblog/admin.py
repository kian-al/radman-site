from django.contrib import admin
from weblog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postadmin(SummernoteModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("title","author","counted_view","status","published_date","updated_date")
    list_filter=("counted_view","status","updated_date","created_date","author")
    search_fields=["title","content"]
    summernote_fields = ('content',)
admin.site.register(Post,postadmin)
admin.site.register(Category)