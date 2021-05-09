"""Defines URL patterns for labor_info_web."""

from django.urls import path

from . import views

app_name = 'labor_info_web'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page for viewing contact request form.
    path('contact_request/', views.contact_request, name='contact_request'),
    # Page for viewing news.
    path('news/', views.news, name='news'),
    # Page for viewing unemployment issues.
    path('unemployment/', views.unemployment, name='unemployment'),
    # Page for submission confirmation.
    path('submitted/', views.submitted, name='submitted'),
     # Page for wages.
    path('wages/', views.wages, name='wages'),
     # Page for workplace issues.
    path('workplace/', views.workplace, name='workplace'),
    ]