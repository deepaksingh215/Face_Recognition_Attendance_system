from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.base, name = 'home'),
    path('addStudent/', views.add_student, name = 'addStudent'),
    path('', views.base, name = 'base'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),

    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('StudentUpdate/', views.studentUpdate, name='StudentUpdate'),
    path('attendence/', views.takeAttendence, name='attendence'),
    # path('video_feed/', views.videoFeed, name='video_feed'),
    # path('videoFeed/', views.getVideo, name='videoFeed'),
]