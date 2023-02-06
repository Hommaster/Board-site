from django.contrib import admin
from django.apps import apps
from board.models import *


# Добавляет поисковое поле к админестратору
class BbAdmin(admin.ModelAdmin):
    # Последовательность имен полей, которые должны выводиться в списке записей
    list_display = ('title', 'content', 'price', 'published')
    # Имена-гиперссылки, ведущие на страницу правки записи
    list_display_links = ('title', 'content')
    # Поля для фильтрации
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Bb, BbAdmin)
# admin.site.register()
admin.site.register(Rubric)




# написать позже
# all_models = apps.get_models()
#
# for model in all_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


