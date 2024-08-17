from django.contrib import admin
from blog.models import contact,Newsletter,Project
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ProjectAdmin(SummernoteModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("title","author","counted_view","status","published_date","updated_date")
    list_filter=("counted_view","status","updated_date","created_date","author","tag")
    search_fields=["title","content"]
    summernote_fields = ('content',)

class contactadmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("name","email","subject","updated_date","created_date")
    list_filter=("created_date","updated_date")
    search_fields=("name","email","message")
    
    
admin.site.register(contact,contactadmin)
admin.site.register(Newsletter)
admin.site.register(Project,ProjectAdmin)
