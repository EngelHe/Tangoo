'''
Copyright (C) 2015 Netease All rights reserved
Author: hzhexin@corp.netease.com
Date: Tues Jul 7 2015
Description:
'''

from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'views', 'likes', 'slug')
	prepopulated_fields = {'slug': ('name',)} # ??

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url', 'views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
