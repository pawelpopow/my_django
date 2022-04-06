from django.shortcuts import render, redirect

from form.models import Message


def form(request):
    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body')
        )

        return redirect('form:news-list')

    return render(
        request,
        "form/news.html"
    )



