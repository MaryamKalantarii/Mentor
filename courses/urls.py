from django.urls import path
from .views import *


app_name = 'courses'

urlpatterns = [
     path("", CourseListView.as_view(),name='courses'),
    path("category/<str:cat>",CourseListView.as_view(),name="course_cat"),
    path("teacher/<str:teacher>",CourseListView.as_view(),name="course_teacher"),
    path("search/",CourseListView.as_view(),name="course_search"),
    path("course-detail/<int:id>",course_detail,name="course_detail"),
    path("<int:id>",delete_comment,name="delete"),
    path("edit/comment/<int:id>",edit,name="edit"),
    path("comment/reply/<int:id>",reply,name="reply"),
]