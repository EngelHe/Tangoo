# -*- coding:utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tangoo.settings')

import django
django.setup()

from rango.models import Category, Page

CATEGORIES = ['Python', 'Django', 'Other Frameworks']

def populate():
	python_cat = add_cat('Python')

	add_page(cat=python_cat,
		title="Official Python Tutorial",
		url="http://docs.python.org/2/tutorial/")

	add_page(cat=python_cat,
		title="How to Think like a Computer Scientist",
		url="http://www.greenteapress.com/thinkpython/")

	add_page(cat=python_cat,
		title="Learn Python in 10 Minutes",
		url="http://www.korokithakis.net/tutorials/python/")

	django_cat = add_cat("Django")

	add_page(cat=django_cat,
		title="Official Django Tutorial",
		url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

	add_page(cat=django_cat,
		title="Django Rocks",
		url="http://www.djangorocks.com/")

	add_page(cat=django_cat,
		title="How to Tango with Django",
		url="http://www.tangowithdjango.com/")

	frame_cat = add_cat("Other Frameworks")

	add_page(cat=frame_cat,
		title="Bottle",
		url="http://bottlepy.org/docs/dev/")

	add_page(cat=frame_cat,
		title="Flask",
		url="http://flask.pocoo.org")

	# Print out what we have added to the user.
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def update_cat():
	add_cat('Python', 128, 64)
	add_cat('Django', 64, 32)
	add_cat('Other Frameworks', 32, 16)

	for c in Category.objects.all():
		print("- {0} -views {1} -likes {2}".format(str(c), c.views, c.likes))

def update_cat_v2():
	for cat in CATEGORIES:
		c = Category.objects.get_or_create(name=cat)[0]
		c.save()

	for c in Category.objects.all():
		print("- {0} -views {1} -likes {2} -slug {3}".format(str(c), c.views, c.likes, c.slug))

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

def add_cat(name, views=0, likes=0):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting Rango population script...")
	# populate()
	# update_cat()
	update_cat_v2()
