from django.contrib import admin

from .models import Test, Question, Selection, UserAnswer
from .inlines import QuestionInline, SelectionInline

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'engagement', 'likes', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'content', 'index', 'seconds', 'score', 'created_at', 'updated_at')
    search_fields = ('content',)
    list_filter = ('test', 'created_at', 'updated_at')
    inlines = [SelectionInline]

@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('content', 'is_correct', 'index', 'question', 'created_at', 'updated_at')
    search_fields = ('content',)
    list_filter = ('is_correct', 'question', 'created_at', 'updated_at')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('session', 'answer', 'created_at')
    search_fields = ('session',)
    list_filter = ('created_at',)

