from django.contrib import admin
from .models import Article2
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']                            # 排序
    actions = ['make_published']                    # 批量操作(按make_published函数来操作: 批量更新发布状态.)

    def make_published(self, request, queryset):
        # queryset.update 返回的是一个数字,
        # 表示更新了几条数据.
        updated = queryset.update(status='p')       # queryset 是一个集合对象, update 可以批量对集合做更新操作.

        # 第一个参数: request: HttpRequest
        # 第二个参数: message: str
        # 第三个参数: level: int
        #
        # 其中 message = ngettext(str1, str2, number),
        # ngettext内部源码: 当 number 是 1 时, 返回 str1, 否则返回 str2.
        #
        # 第三个参数: 这里填写的是: messages.SUCCESS; 页面中将会显示绿色背景的提示条.
        #            除了 SUCCESS(绿色) , 有效的值还有  INFO(绿色) / WARNING(黄色) / ERROR(红色) .
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.ERROR)

    make_published.short_description = "Mark selected stories as published"


admin.site.register(Article2, ArticleAdmin)