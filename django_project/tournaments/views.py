from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from tournaments.forms import TournamentCreateForm
from tournaments.models import TournamentModel


class TournamentDetailView(views.View):
    pass


class TournamentCreateView(LoginRequiredMixin, views.View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("forbidden")
        
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
            tournament = form.save(commit=False)

            tournament.owner = request.user
            tournament.save()

        return redirect("tournaments:all_tournaments")


class AllTournamentsView(LoginRequiredMixin, views.View):
    def get(self, request):
        tournaments = TournamentModel.objects.select_related(
            "owner",
        ).all()

        return render(
            request=request,
            template_name="tournaments/all_tournaments.html",
            context={
                "tournaments": tournaments,
            },
        )
