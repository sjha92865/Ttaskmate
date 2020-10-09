from django.urls import path
from todolist_app import views

# since i need to connect views with urls 
'''
urlpatterns = [
    path('', views.todolist,name='todolist'),
    ]
'''

# here we need to tell what we do with urls.py of taskmate
#and urls send from there.

#line 6 we tell, since it is a app, we need to coonect it with view to show the functionality,
#hence--views.todolist, name of link is todolist
#domain/task is our url
#view is todolist and name is todolist
#move to view.py where u need to write all the functions of the views



urlpatterns = [
    path('', views.todolist,name='todolist'),
    path('delete/<task_id>', views.delete,name='delete_task'),
    path('edit/<task_id>', views.edit_task,name='edit_task'),
    path('complete/<task_id>', views.complete,name='completed_task'),
    path('pending/<task_id>', views.pending,name='pending_task'),
    
        ]

'''
1st argument name displayed on website,
3rd is name of function in views.py,
'''