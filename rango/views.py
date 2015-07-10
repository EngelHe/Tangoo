'''
Copyright (C) 2015 Netease All rights reserved
Author: hzhexin@corp.netease.com
Date: Tues Jul 7 2015
Description:
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from django.core.urlresolvers import reverse

def index(request):

	# '-likes' means descending order, 'likes' means ascending
	category_list = Category.objects.order_by('-likes')
	context_dict = {'categories': category_list}

	# context_dict = {'boldmessage': "I am bold font from the context"}

	return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
	context_dict = {}
	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	return render(request, 'rango/category.html', context_dict)


def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage.
			# return index(request)
			return HttpResponseRedirect(reverse('rango.views.index'))
		else:
			# The supplied form contained errors - just print them to the terminal.
			print(form.errors)
	else:
		# If the request was not a POST, display the form to enter details.
		form = CategoryForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
	context_dict = {}
	try:
		cat = Category.objects.get(slug=category_name_slug)
		context_dict['cat_name'] = cat.name
	except Category.DoesNotExist:
		cat = None
		context_dict['cat_name'] = category_name_slug.replace('_', ' ')

	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()
				return HttpResponseRedirect(reverse('rango.views.category',
													args=(category_name_slug,)))
				# return category(request, category_name_slug)
		else:
			print(form.error)
	else:
		form = PageForm()
	context_dict['form'] = form
	context_dict['category'] = cat
	return render(request, 'rango/add_page.html', context_dict)

def about(request):
	return HttpResponse('This is an about page!!<br/><a href="/rango/">Index</a>')

