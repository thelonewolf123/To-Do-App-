from django.shortcuts import render, redirect
from .models import ToDo


def index(request):
    template = "index.html"
    todo = ToDo.objects.all().order_by("-id")
    context = {'todo': todo}
    return render(request, template, context)


def add(request):
    item = request.GET['text']
    ToDo.objects.create(text=item)
    return redirect('index')


def delete(request, id):
    ToDo.objects.get(pk=id).delete()
    return redirect('index')