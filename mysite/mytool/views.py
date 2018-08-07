from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category


def index(request):
    latest_category_list = Category.objects.all()
    context = {'latest_category_list':latest_category_list}
    return render(request, 'mytool/index.html', context)


def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'mytool/detail.html', {'category':category})


def lists(request, category_id):
    response = "You're looking at the password list of category %s."
    return HttpResponse(response % category_id)


# def vote(request, category_id):
#     return HttpResponse("You're viewed on category %s." % category_id)
