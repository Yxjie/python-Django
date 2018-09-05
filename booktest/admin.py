from django.contrib import admin
from booktest.models import *


# Register your models here.
# admin 注册模型类 可以在后台进行数据的管理添加
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
