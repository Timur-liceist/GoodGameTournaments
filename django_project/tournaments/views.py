from django.shortcuts import render
from django.views import View

from tournaments.forms import TournamentCreateForm


class TournamentDetailView(View):
    pass


class TournamentCreateView(View):
    def get(self, request):
        form = TournamentCreateForm()

        context = {
            "form": form,
        }

        return render(
            request,
            "tournaments/create_tournament.html",
            context=context,
        )

    def post(self, request):
        form = TournamentCreateForm(request.POST)

        if form.is_valid():
            form.save()

        context = {
            "form": form,
        }

        return render(
            request,
            "tournaments/create_tournament.html",
            context=context,
        )
