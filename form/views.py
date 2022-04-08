from django.shortcuts import render, redirect

from form.models import Message


def task_create_view(request):
    task = request.POST.get('task')

    if task:
        Task.objects.create(name=task)

        return redirect('form:task-list')

    return render(
        request,
        'taskapp/new_form.html',
    )


def task_list_view(request):
    tasks = Task.objects.all()

    return render(
        request,
        'taskapp/new_list.html',
        context={
            'tasks': tasks,
        }
    )
