from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Question, Selection

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True
    readonly_fields = ('question_link',)
    fields = ('index', 'content', 'seconds', 'score', 'question_link')

    def question_link(self, obj):
        if obj.id:
            url = reverse('admin:quiz_question_change', args=[obj.id])
            return format_html('<a href="{}">상세보기</a>', url)
        return "저장 후 링크가 생성됩니다"

    question_link.short_description = "상세 링크"

class SelectionInline(admin.TabularInline):
    model = Selection
    extra = 1