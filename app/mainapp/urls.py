from django.urls import path

from .views import MainListView, AboutListView, NewsListView, FirstProductListView, SecondProductListView, ThirdProductListView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('about/', AboutListView.as_view(), name='about'),
    path('news/', NewsListView.as_view(), name='news'),
    path('docs/', AboutListView.as_view(), name='docs'),
    path('contacts/', AboutListView.as_view(), name='contacts'),
    path('first/product/', FirstProductListView.as_view(), name='first'),
    path('second/product/', SecondProductListView.as_view(), name='second'),
    path('third/product/', ThirdProductListView.as_view(), name='third'),
]