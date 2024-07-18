from django.contrib import admin
from weblog.models import post,Category
# Register your models here.
class postadmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("title","author","counted_view","status","published_date","updated_date")
    list_filter=("counted_view","status","updated_date","created_date","author")
    search_fields=["title","content"]
admin.site.register(post,postadmin)
admin.site.register(Category)