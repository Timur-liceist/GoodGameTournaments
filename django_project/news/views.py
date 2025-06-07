from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from news.forms import NewsForm
from news.models import GeneralNewsModel


class AllNewsView(View):
    def get(self, request):
        general_news = GeneralNewsModel.objects.all()

        context = {
            "general_news": general_news,
        }

        return render(
            request,
            "news/general_news.html",
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
