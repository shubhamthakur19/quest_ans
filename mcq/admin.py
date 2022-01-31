from django.contrib import admin

from .models import Question_Sets, Questions, Option
# Register your models here.

admin.site.register(Question_Sets)
admin.site.register(Questions)
admin.site.register(Option)


# from django.contrib import admin

# from .models import Questions


# class ChoiceInline(admin.StackedInline):
#     model = Option
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['text', 'image']
#     inlines = [ChoiceInline]


# admin.site.register(Questions, QuestionAdmin)


# class QuestAdmin(admin.StackedInline):
#     model = Questions


# class QuestionSetAdmin(admin.ModelAdmin):
#     fields = ['section']
#     inlines = [QuestAdmin]


# admin.site.register(Question_Sets, QuestionSetAdmin)
