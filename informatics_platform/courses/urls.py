from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('<int:course_id>', course_detail, name='course_detail'),
]