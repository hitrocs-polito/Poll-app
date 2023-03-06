from django.contrib import admin
from django.utils import timezone
from django.utils.datetime_safe import datetime

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)


@admin.display(
    boolean=True,
    ordering='pub_date',
    description='Published recently?', )
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

