from django.urls import path

from form import views

app_name = "form"

urlpatterns = [
    path('new/', views.form, name="form"),
]