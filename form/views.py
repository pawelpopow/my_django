from django.shortcuts import render, redirect, get_object_or_404

from form.models import Message


# Pamięć ulotna RAM
# TASKS = []


def task_create_view(request):
    task = request.POST.get('task')

    if task:
        Message.objects.create(name=task)

        return redirect('form:task-list')

    return render(
        request,
        'form/task_form.html',
    )


def task_list_view(request):
    tasks = Message.objects.all()

    return render(
        request,
        'form/task_list.html',
        context={
            'tasks': tasks,
        }
    )


def task_detail_view(request, pk):

    task = get_object_or_404(Message, pk=pk)

    return render(
        request,
        'form/task_detail.html',
        context={
            'task': task,
        }
    )


def task_update_view(request, pk):
    task = get_object_or_404(Message, pk=pk)

    modified_task = request.POST.get("task")
    if modified_task:
        task.name = modified_task
        task.save()

        return redirect('form:task-list')

    return render(
        request,
        'form/task_form.html',
        context={
            'task': task,
        }
    )


def task_delete_view(request, pk):
    task = get_object_or_404(Message, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect('form:task-list')

    return render(
        request,
        'form/task_confirm_delete.html',
        context={
            'task': task,
        }
    )
