from django.urls import path
from .views import First_student, Second_student


urlpatterns = [
    path('student/', First_student, name='first_student'),
    path('student_second/', Second_student, name='second_student'),
]