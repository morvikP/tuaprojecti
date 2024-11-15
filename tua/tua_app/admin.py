from django.contrib import admin
from .models import Category, Job, plan, deli, vak
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'image')
    fields = ('title', 'category', 'price', 'image')
admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(plan, JobAdmin)
admin.site.register(deli)
admin.site.register(vak, JobAdmin)