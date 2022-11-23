from django.contrib import admin

from .models import Car, Category


class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'photo', 'cat', 'is_published',)
    list_editable = ('cat', 'photo', 'is_published',)
    prepopulated_fields = {'slug': ('title', )}
    # empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
