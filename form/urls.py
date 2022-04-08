from django.urls import path

from form import views

app_name = "form"

urlpatterns = [
    path('new/', views.task_create_view, name="task-create"),
    path('new-list/', views.task_list_view, name="task-list"),

]