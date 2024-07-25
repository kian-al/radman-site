from django.contrib import admin
from blog.models import contact,Newsletter
# Register your models here.


class contactadmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("name","email","subject","updated_date","created_date")
    list_filter=("created_date","updated_date")
    search_fields=("name","email","message")
    
    
admin.site.register(contact,contactadmin)
admin.site.register(Newsletter)
