from django.contrib import admin

from todos import models

# 
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body"
    )

# Register your models here.


admin.site.register(models.Todo, TodoAdmin)