from django.contrib import admin
from .models import Question, Quiz, Course, Lesson, Answer


admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Answer)