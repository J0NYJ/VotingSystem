from django.contrib import admin
from .models import *

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 在admin页面显示额外三个空白表单


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline,]  # 在admin页面显示内联
    list_display = ('question_text', 'pub_date')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)