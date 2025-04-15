from django.contrib import admin
from .models import Test, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    fields = ['text', 'is_correct']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'test']
    inlines = [AnswerInline]

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    show_change_link = True

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'is_pro']
    list_editable = ['is_pro']
    list_filter = ['difficulty', 'is_pro']
    search_fields = ['title']
    inlines = [QuestionInline]