from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
# admin.site.register(TendaProject)
# admin.site.register(TendaSkill)

@admin.register(TendaProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'techonogies_use')
    search_fields = ('description', 'title')
    list_filter = ('title',  'user')

@admin.register(TendaSkill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'category')
    search_fields = ('name', 'category')
    list_filter = ('name',  'user')

admin.site.site_header = "Portfolio Administration"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Administration"

