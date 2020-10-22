from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index-view'),
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/([0-9])$', views.students_detail),
]
