from django.contrib import admin
from .models import ArticleModel, AuthorModel


# Register your models here.
class AuthorModelAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'author',
                    'date_joined',
                    'author__date_joined', 'custom_field']

    # 普通字段, 这里仅需填写字段名.
    # 如果字段是一个关联字段, 那么这里可以用双下滑线表示要显示关联表中的那个字段(必须是时间类型字段).
    date_hierarchy = 'author__date_joined'

    def author__date_joined(self, queryset):
        return queryset.author.date_joined

    author__date_joined.short_description = "作者加入时间(这是一个关联延申字段)"

    radio_fields = {'author': admin.HORIZONTAL}

    autocomplete_fields = ('author', )

    readonly_fields = ('custom_field', )

    def custom_field(self, model):
        """
        可以在这里显示额外的字段, 以html形式返回, 想提供什么链接都可以.
        readonly_fields 属性, 不适合对已有字段设定readonly,
        因为在新增的时候该字段也不能添加, 这不符合使用场景;
        readonly_fields 更适合额外增加多个自定义字段展示.
        """
        from django.utils.safestring import mark_safe
        return mark_safe("<span class='errors'>show something</span>")


admin.site.register(ArticleModel, ArticleModelAdmin)
admin.site.register(AuthorModel, AuthorModelAdmin)