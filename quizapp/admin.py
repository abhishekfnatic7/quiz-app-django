from django.contrib import admin

from quizapp.models import Questionpage

# Register your models here.

class Show(admin.ModelAdmin):
    list_display=['questiontext','ans']
admin.site.register(Questionpage,Show)