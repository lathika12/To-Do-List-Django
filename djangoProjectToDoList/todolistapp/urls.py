from django.urls import path
from .views import addtask, index, edittask, deletetask, updatetask, savetask

app_name = 'todolistapp'

urlpatterns = [
    path('', addtask, name='index'),
    path('addtask/', addtask, name='addtask'),
    path('edittask/<int:id>/', edittask, name='edittask'),
    path('updatetask/<int:id>/', updatetask, name='updatetask'),
    path('deletetask/<int:id>/', deletetask, name='deletetask'),
]
