
from django.contrib import admin

from django.urls import path
from . views import studentView
urlpatterns = [
    path(r'getData', studentView.as_view()),
    path(r'createData', studentView.as_view()),
    path(r'updateData',studentView.as_view()),
    path(r'deleteData', studentView.as_view()),

]
