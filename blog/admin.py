from django.contrib import admin
from blog.models import contact, Newsletter, Project
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ProjectAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title", "author", "counted_view", "status", "published_date", "updated_date")
    list_filter = ("counted_view", "status", "updated_date", "created_date", "author", "tag")
    search_fields = ["title", "content"]
    summernote_fields = ('content',)

    class Media:  
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-lite.min.css',  
                'https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font/dist/font-face.css',  
                'custom_css/summernote_custom.css',  
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-lite.min.js',  
            'custom_js/summernote_fa_IR.js', 
        )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # تغییر فونت در فرم
        form.base_fields['content'].widget.attrs.update({
            'style': 'font-family: Vazir, B-Nazanin, sans-serif;',  
        })
        return form

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("name", "email", "subject", "updated_date", "created_date")
    list_filter = ("created_date", "updated_date")
    search_fields = ("name", "email", "message")
    
# Register models
admin.site.register(contact, ContactAdmin)
admin.site.register(Newsletter)
admin.site.register(Project, ProjectAdmin)
