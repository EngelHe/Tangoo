# -*- coding:utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	# override method
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	# For Python 3, use __unicode__ on Python 2
	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

# For Python 3, use __unicode__ on Python 2
	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	# TODO 没有做图片上传的功能
	# picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username
