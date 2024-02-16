from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})
