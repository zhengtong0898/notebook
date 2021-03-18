from django.contrib import admin
from .models import Article, Publication


# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):
    # filter_horizontal = ('publications', )
    filter_vertical = ('publications', )


class PublicationModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Publication, PublicationModelAdmin)