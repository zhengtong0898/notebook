from django.contrib import admin
from .models import ArticleModel, AuthorModel


# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'author',
                    'date_joined',
                    'author__date_joined']

    # 普通字段, 这里仅需填写字段名.
    # 如果字段是一个关联字段, 那么这里可以用双下滑线表示要显示关联表中的那个字段(必须是时间类型字段).
    date_hierarchy = 'author__date_joined'

    def author__date_joined(self, queryset):
        return queryset.author.date_joined

    author__date_joined.short_description = "作者加入时间(这是一个关联延申字段)"


admin.site.register(ArticleModel, ArticleModelAdmin)
admin.site.register(AuthorModel, admin.ModelAdmin)