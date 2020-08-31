from django.contrib import admin
from .models import Webdev, Category


class WebdevAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'category',
    )
    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Webdev, WebdevAdmin)
admin.site.register(Category, CategoryAdmin)
