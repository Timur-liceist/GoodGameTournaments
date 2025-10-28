from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from teams.models import MemberModel

from tournaments.forms import RequestTeamTournamentForm, TournamentCreateForm
from tournaments.models import RequestTeamForTournamentModel, TournamentModel


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


class SendRequestToTournamentView(LoginRequiredMixin, views.View):
    def get(self, request, tournament_id):
        form = RequestTeamTournamentForm()
        form.set_team_selecting(leader_user=request.user)
        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/send_request_team_tournament.html",
        )

    def post(self, request, tournament_id):
        form = RequestTeamTournamentForm(request.POST)

        if form.is_valid():
            tournament = TournamentModel.objects.filter(
                id=tournament_id,
            ).first()

            request_team_tournament = RequestTeamForTournamentModel(
                team=form.cleaned_data["team"],
                tournament_id=tournament.id,
            )
            request_team_tournament = request_team_tournament.save()

            return redirect("tournaments:all_tournaments")

        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/send_request_team_tournament.html",
        )
class AllRequestTeamTournament(LoginRequiredMixin, views.View):
    def get(self, request, tournament_id):
        all_teams_id = MemberModel.objects.filter(user=request.user)
        request_team_tournament = RequestTeamForTournamentModel.objects.filter(
            
        )
        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/send_request_team_tournament.html",
        )

    def post(self, request, tournament_id):
        form = RequestTeamTournamentForm(request.POST)

        if form.is_valid():
            tournament = TournamentModel.objects.filter(
                id=tournament_id,
            ).first()

            request_team_tournament = RequestTeamForTournamentModel(
                team=form.cleaned_data["team"],
                tournament_id=tournament.id,
            )
            request_team_tournament = request_team_tournament.save()

            return redirect("tournaments:all_tournaments")

        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/send_request_team_tournament.html",
        )
