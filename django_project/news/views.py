from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from news.forms import NewsForm
from news.models import NewsModel


class AllNewsView(View):
    def get(self, request):
        all_news = NewsModel.objects.all()

        context = {
            "all_news": all_news,
        }

        return render(
            request,
            "news/all_news.html",
            context=context,
        )


class CreateNewsView(LoginRequiredMixin, View):

    def get(self, request):
        form = NewsForm()

        context = {
            "form": form,
        }

        return render(
            request,
            "news/create_news.html",
            context=context,
        )

    def post(self, request):
        form = NewsForm(request.POST)

        if form.is_valid():
            form.save()

        context = {
            "form": form,
        }

        return render(
            request,
            "news/create_news.html",
            context=context,
        )
