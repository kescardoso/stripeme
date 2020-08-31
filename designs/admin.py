from django.contrib import admin
from .models import Design, Category


class DesignAdmin(admin.ModelAdmin):
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


admin.site.register(Design, DesignAdmin)
admin.site.register(Category, CategoryAdmin)
