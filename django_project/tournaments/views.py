from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from teams.models import MemberModel

from tournaments.forms import (
    BattleForm,
    RequestTeamTournamentForm,
    TournamentCreateForm,
)
from tournaments.models import (
    BattleModel,
    RequestTeamForTournamentModel,
    TournamentModel,
)


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

        tournament = TournamentModel.objects.filter(
            id=tournament_id,
        ).first()

        if tournament.is_closed_for_requests:
            return redirect("tournaments:tournament_reg_is_closed")

        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/send_request_team_tournament.html",
        )

    def post(self, request, tournament_id):
        template_name = "tournaments/send_request_team_tournament.html"

        form = RequestTeamTournamentForm(request.POST)

        if form.is_valid():
            tournament = TournamentModel.objects.filter(
                id=tournament_id,
            ).first()

            if tournament.is_closed_for_requests:
                return redirect("tournaments:tournament_reg_is_closed")

            request_team_tournament = (
                RequestTeamForTournamentModel.objects.filter(
                    team_id=form.cleaned_data["team"].id,
                    tournament_id=tournament.id,
                ).first()
            )

            if request_team_tournament:  # noqa: SIM102
                if request_team_tournament.status == "pending":
                    form.add_error(
                        None,
                        "Вы уже послали заявку\
                        и она ожидает ответа",
                    )
                    context = {
                        "form": form,
                    }
                    return render(
                        request=request,
                        context=context,
                        template_name=template_name,
                    )

            request_team_tournament = RequestTeamForTournamentModel(
                team=form.cleaned_data["team"],
                tournament_id=tournament.id,
            )
            request_team_tournament = request_team_tournament.save()

            return redirect("tournaments:all_tournaments")

        return redirect("tournaments:user_all_request_team_tournament")


class UserAllRequestTeamTournament(LoginRequiredMixin, views.View):
    def get(self, request):
        team_ids = MemberModel.objects.filter(
            user=request.user,
        ).values_list(
            "team_id",
            flat=True,
        )
        requests_team_tournament = (
            RequestTeamForTournamentModel.objects.filter(
                team_id__in=team_ids,
            ).select_related(
                "tournament",
            )
        )
        context = {
            "requests_team_tournament": requests_team_tournament,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/user_all_request_team_tournament.html",
        )


class ManageTournamentBattles(LoginRequiredMixin, views.View):
    def get(self, request, tournament_id):
        battles = BattleModel.objects.filter(
            tournament_id=tournament_id,
        )
        context = {
            "battles": battles,
            "tournament_id": tournament_id,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/manage_tournament_battles.html",
        )


class BattleCreateView(LoginRequiredMixin, views.View):
    def get(self, request, tournament_id):
        form = BattleForm()
        tournament = (
            TournamentModel.objects.filter(
                id=tournament_id,
            )
            .prefetch_related(
                "judges",
            )
            .prefetch_related(
                "team_members",
            )
            .first()
        )

        form.set_team_selecting(
            teams_by_tournament=tournament.team_members,
            judges_by_tournament=tournament.judges,
        )
        context = {
            "form": form,
        }

        return render(
            request=request,
            context=context,
            template_name="tournaments/create_battle.html",
        )

    def post(self, request, tournament_id):
        form = BattleForm(request.POST)
        if form.is_valid():
            new_battle = form.save(commit=False)

            new_battle.tournament_id = tournament_id
            new_battle.save()

            return redirect("homepage")

        context = {
            "form": form,
        }
        return render(
            request=request,
            context=context,
            template_name="tournaments/create_battle.html",
        )


class ManageBattleView(LoginRequiredMixin, views.View):
    def get(self, request, tournament_id):
        battles_by_tournament = (
            BattleModel.objects.filter(
                tournament__id=tournament_id,
            )
            .select_related(
                "first_team",
            )
            .select_related(
                "second_team",
            )
            .select_related(
                "judge",
            )
            .all()
        )

        tournament = (
            TournamentModel.objects.filter(
                id=tournament_id,
            )
            .only(
                "owner",
            )
            .select_related(
                "owner",
            )
            .first()
        )

        context = {
            "battles": battles_by_tournament,
            "owner_tournament": tournament.owner,
            "tournament_id": tournament_id,
        }
        return render(
            request=request,
            template_name="tournaments/manage_battles.html",
            context=context,
        )
