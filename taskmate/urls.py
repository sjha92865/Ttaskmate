
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_views
from user_app import views as user_views
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
]
#line no 9 redirects task link to todolist_app and connect it with url
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('', todolist_views.index,name='index'),
    path('about-us', todolist_views.about,name='abou'),
    path('contact-us', todolist_views.contact,name='contact'),
    path('account/',include('user_app.urls')),

]
