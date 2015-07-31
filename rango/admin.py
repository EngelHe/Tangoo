'''
Copyright (C) 2015 Engel All rights reserved
Author: hexin2tt@aliyun.com
Date: Tues Jul 7 2015
Description:
'''

from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'views', 'likes', 'slug')
	prepopulated_fields = {'slug': ('name',)} # ??

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url', 'views')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'website')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
