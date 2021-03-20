from django.contrib import admin
from .models import ArticleModel


# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):

    list_display = ('title', 'tags', 'author', 'date_joined')
    ordering = ('title', 'date_joined')                             # 按字段排序, 对应sql是: order by .
    sortable_by = ('tags', )

    search_fields = ('title', )
    show_full_result_count = True


admin.site.register(ArticleModel, ArticleModelAdmin)
