from django.views.generic import ListView, DetailView, RedirectView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Test
import uuid
from django.db.models import F

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MainPageView(ListView):
    model = Test
    template_name = 'quiz/main.html'
    context_object_name = 'tests'

class StartQuizView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        test_id = self.kwargs['test_id']
        test = get_object_or_404(Test, id=test_id)
        test.engagement = F('engagement') + 1
        test.save()
        session_id = str(uuid.uuid4())
        return reverse('quiz_question', kwargs={'test_id': test_id, 'session_id': session_id, 'question_number': 1})

class QuizQuestionView(DetailView):
    model = Test
    template_name = 'quiz/question.html'
    pk_url_kwarg = 'test_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = self.object
        questions = test.question.all().order_by('index')
        
        context.update({
            'questions': questions,
            'session_id': self.kwargs['session_id'],
            'total_questions': questions.count(),
        })
        return context

class SubmitAnswerView(APIView):
    def post(self, request):
        test_id = request.data.get('test_id')
        question_number = int(request.data.get('question_number'))
        test = get_object_or_404(Test, id=test_id)
        
        if question_number >= test.question.count():
            redirect_url = reverse('quiz_result', kwargs={'test_id': test_id, 'session_id': request.data.get('session_id')})
        else:
            redirect_url = reverse('quiz_question', kwargs={
                'test_id': test_id, 
                'session_id': request.data.get('session_id'), 
                'question_number': question_number + 1
            })
        
        return Response({'redirect': redirect_url})

class QuizResultView(DetailView):
    model = Test
    template_name = 'quiz/result.html'
    pk_url_kwarg = 'test_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class QuizFeedbackView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        test_id = self.kwargs['test_id']
        liked = self.request.GET.get('liked') == 'true'
        test = get_object_or_404(Test, id=test_id)
        
        if liked:
            test.likes = F('likes') + 1
        else:
            test.dislikes = F('dislikes') + 1 
        test.save()
        
        return reverse('main_page')
