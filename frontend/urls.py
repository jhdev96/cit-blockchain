from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_user, name='logout'),
    path('transactions', views.blocks, name='transactions'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.student_detail, name='student')
]
