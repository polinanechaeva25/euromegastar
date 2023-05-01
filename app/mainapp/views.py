from django.contrib.auth.models import User
from django.views.generic import ListView


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        return context


class MainListView(TitleContextMixin, ListView):
    title = 'Главная'
    template_name = 'mainapp/index.html'
    model = User


class AboutListView(TitleContextMixin, ListView):
    title = 'О нас'
    template_name = 'mainapp/about.html'
    model = User


class NewsListView(TitleContextMixin, ListView):
    title = 'Новости'
    template_name = 'mainapp/news.html'
    model = User


class FirstProductListView(TitleContextMixin, ListView):
    title = 'Avrilé Universal'
    template_name = 'mainapp/first_uni.html'
    model = User


class SecondProductListView(TitleContextMixin, ListView):
    title = 'Avrilé Color Save'
    template_name = 'mainapp/second_color.html'
    model = User


class ThirdProductListView(TitleContextMixin, ListView):
    title = 'Avrilé Deep Black'
    template_name = 'mainapp/third_black.html'
    model = User