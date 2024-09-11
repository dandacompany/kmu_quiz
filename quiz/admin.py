from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Test, Question, Selection

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('index', 'content', 'seconds', 'score', 'selection_list', 'view_link')
    readonly_fields = ('view_link', 'selection_list')
    ordering = ('index',)  # 인덱스 순으로 정렬

    def view_link(self, obj):
        if obj.id:
            url = reverse('admin:quiz_question_change', args=[obj.id])
            return format_html('<a href="{}">상세보기</a>', url)
        return "저장 후 링크 생성"
    view_link.short_description = "상세 링크"

    def selection_list(self, obj):
        selections = obj.selection.all().order_by('index')
        return format_html("<br>".join([f"{s.index}. {s.content} {' (정답)' if s.is_correct else ''}" for s in selections]))
    selection_list.short_description = "등록된 선택지 목록"

class SelectionInline(admin.StackedInline):
    model = Selection
    extra = 1
    fields = ('index', 'content', 'is_correct', 'view_link')
    readonly_fields = ('view_link',)

    def view_link(self, obj):
        if obj.id:
            url = reverse('admin:quiz_selection_change', args=[obj.id])
            return format_html('<a href="{}">상세보기</a>', url)
        return "저장 후 링크 생성"
    view_link.short_description = "상세 링크"

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


