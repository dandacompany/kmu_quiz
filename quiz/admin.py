from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Test, Question, Selection
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True
    fields = ('index', 'content', 'seconds', 'score', 'selection_list')
    readonly_fields = ('selection_list',)
    ordering = ('index',)  # 인덱스 순으로 정렬

    def selection_list(self, obj):
        selections = obj.selection.all().order_by('index')
        return format_html("<br>".join([f"{s.index}. {s.content} {' (정답)' if s.is_correct else ''}" for s in selections]))
    selection_list.short_description = "등록된 선택지 목록"

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }

# custom.css 파일에 다음 내용을 추가해야 합니다:
# .field-content { width: 30%; }

class SelectionInline(admin.TabularInline):
    model = Selection
    show_change_link = True
    extra = 1
    fields = ('index', 'content', 'is_correct')

# Test 모델 관리
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'engagement', 'likes', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]

# Question 모델 관리
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'content', 'index', 'seconds', 'score')
    list_filter = ('test',)
    search_fields = ('content',)
    inlines = [SelectionInline]

# Selection 모델 관리
@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'is_correct', 'index')
    list_filter = ('question', 'is_correct')
    search_fields = ('content',)


