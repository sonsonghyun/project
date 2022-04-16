from django.contrib import admin
from . models import Theme

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['pk','theme_title','theme_contents','theme_time','theme_num','category']

admin.site.register(Theme,ThemeAdmin)
