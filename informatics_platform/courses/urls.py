from django.urls import path
from .views import *


urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('<int:course_id>', course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('signup/', signup, name='signup'),
]