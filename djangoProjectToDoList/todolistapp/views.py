from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import TodoListForm
from .models import TodoList


def index(request):
    return render(request,'index.html',{'object_list':TodoList.objects.all()})

def addtask(request):
    form = TodoListForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context['form'] = form
    context['object_list'] = TodoList.objects.all()
    return render(request,"index.html",context)
def edittask(request,id):
    context = {}
    obj = get_object_or_404(TodoList, id=id)
    print("Within edit task of obj :", obj)
    tosavetaskform = TodoListForm(request.POST or None, instance=obj)
    context['tosavetaskform'] = tosavetaskform
    context['editing'] = True

    if request.method == 'POST':
        if tosavetaskform.is_valid():
            tosavetaskform.save()
            context['editing'] = False

    context['editing_id'] = id
    context['object_list'] = TodoList.objects.all()

    return render(request, "index.html", context)

def savetask(request,id,updatedcontent):
    obj = get_object_or_404(TodoList, id=id)


def updatetask(request,id):
    context = {}
    obj = get_object_or_404(TodoList, id = id)
    print("Within Update task", obj)

    if obj.done:
        print("Within Done task", obj.done)
        obj.done = False
        context['message'] = "Task has been RESET and UNCHECKED!"
    else:
        print("Within else: ", obj.done)
        obj.done = True
        context['message'] = "COMPLETED! Task has been marked as COMPLETED."
    obj.save()


    context['object_list'] = TodoList.objects.all()
    return render(request,"index.html",context)

def deletetask(request,id):
    context = {}
    obj = get_object_or_404(TodoList, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('todolistapp:index'))

    return render(request,"index.html",context)