from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Enrollment
from .forms import EnrollmentForm
from django.contrib.auth.decorators import login_required


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user
            enrollment.save()
            return redirect('courses:course_detail', course_id=course.id)
    else:
        form = EnrollmentForm(initial={'course': course})
    return render(request, 'courses/enroll_course.html', {'form': form, 'course': course})
