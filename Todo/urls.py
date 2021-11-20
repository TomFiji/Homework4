from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('delete/<str:todo_id>', views.delete, name='delete'),
    path('update/<str:todo_id>', views.update, name='update')
]