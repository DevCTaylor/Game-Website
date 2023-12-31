import json
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import GameScores
from review.models import Review


def record_score(request):
    data = json.loads(request.body)
    username = request.user
    score = data["score"]
    gamelength = data["gamelength"]
    maxnum = data["maxnum"]
    operation = data["operation"]
    game = data["game"]
    new_score = GameScores(username=username, game=game, score=score, maxnum=maxnum, gamelength=gamelength, operation=operation)
    new_score.save()
    response = {"success": True}
    return JsonResponse(response)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


class GamesView(TemplateView):
    template_name = "games/games.html"


class GameScoresView(TemplateView):
    template_name = "games/game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        return context


class MyScoresView(TemplateView):
    template_name = "games/myscores.html"

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['myscores'] = GameScores.objects.all().filter(username=self.request.user)
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score').filter(username=self.request.user)
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score').filter(username=self.request.user)

        return context
