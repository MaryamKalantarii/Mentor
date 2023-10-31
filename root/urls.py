from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",HomeView.as_view(),name = "home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("trainer",trainer,name="trainer"),
    path("course-detail/<int:id>",course_detail,name="course_detail"),
]
