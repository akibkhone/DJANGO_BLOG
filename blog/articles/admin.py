from django.contrib import admin
from .models import Article

# Register your models here.

#method 1 to register the model - ( easy but not many features )

# admin.site.register(Article)

#or

# method 2 to register the model -  ( using )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','published','author')
    date_hierarchy = 'published'
    search_fields = ('title','description')
