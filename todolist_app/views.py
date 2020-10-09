from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):#name "todolist is same name given in urls.py of app"
    if  request.method=="POST":
        form =TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')

    else:
        all_tasks=TaskList.objects.filter(manage=request.user)
        paginator=Paginator(all_tasks,3)
        page=request.GET.get('pg')#?pg=3
        all_tasks=paginator.get_page(page)
        return render(request,'todolist.html',{"all_tasks":all_tasks})

@login_required
def contact(request):#name "todolist is same name given in urls.py of app"
    context={'contact_text':
    'welcome contact us Page',
    }
    return render(request,'contact.html',context)

@login_required
def delete(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted,You Are Not Allowed!"))
    
    return redirect('todolist')

@login_required
def edit_task(request,task_id):#name "todolist is same name given in urls.py of app"
    prev_obj=TaskList.objects.get(pk=task_id)
    if  request.method=="POST":
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        v=prev_obj.task+" changed to "+task.task
        context={'task':v}
        #messages.success(request,(context['task'])) or
        messages.success(request,(v))
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

@login_required
def complete(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=True#here we update from false to true
        task.save()
    else:
        messages.error(request,("Access Restricted,You Are Not Allowed!"))
    return redirect('todolist')

@login_required
def pending(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=False#here we update from false to true
        task.save()
    else:
        messages.error(request,("Access Restricted,You Are Not Allowed!"))
    return redirect('todolist')


def about(request):#name "todolist is same name given in urls.py of app"
    context={'about_text':
    'welcome about Page',
    }
    return render(request,'about.html',context)

#so someone is going to visit our domain name which 127.something\task
#it will be redirected to our todolist_app.url
#they will come to this url, they see its blank('')
#they will redirect to our views, then take the functionality and return whatever is there.

def index(request):#name "todolist is same name given in urls.py of app"
    context={'index_text':
    'welcome to index Page',
    }
    return render(request,'index.html',context)
