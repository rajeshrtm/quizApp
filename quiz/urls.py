from django.urls import path

from .views import QuizListView, QuizDetailView

app_name = 'quiz'
urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
]