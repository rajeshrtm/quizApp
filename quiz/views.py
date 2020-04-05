from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Quiz


class QuizListView(ListView):

    model = Quiz
    paginate_by = 100

class QuizDetailView(DetailView):

	model = Quiz