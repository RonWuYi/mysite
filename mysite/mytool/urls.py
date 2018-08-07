from django.urls import path

from . import views


urlpatterns = [
    # ex: /category/
    path('', views.index, name='index'),
    # ex: /category/5/
    path('<int:category_id>/', views.detail, name='detail'),
    # ex: /category/5/lists/
    path('<int:category_id>/passwords/', views.lists, name='lists'),
    # ex: /category/5/vote/
    # path('<int:category_id>/vote/', views.vote, name='vote'),
]