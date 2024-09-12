from django.urls import path
from .views import MainPageView, StartQuizView, QuizQuestionView, QuizResultView, QuizFeedbackView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('quiz/<int:test_id>/start/', StartQuizView.as_view(), name='start_quiz'),
    path('quiz/<int:test_id>/<str:session_id>/<int:question_number>/', QuizQuestionView.as_view(), name='quiz_question'),
    path('quiz/<int:test_id>/result/<str:session_id>/', QuizResultView.as_view(), name='quiz_result'),
    path('quiz/<int:test_id>/feedback/', QuizFeedbackView.as_view(), name='quiz_feedback'),
]