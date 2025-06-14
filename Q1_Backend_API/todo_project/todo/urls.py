from django.urls import path
from . import views
urlpatterns=[
    path('tasks/',views.get_all_tasks),
    path('tasks/create/',views.add_task),
    path('tasks/<int:pk>/',views.get_task),
    path('tasks/update/<int:pk>',views.update_task),
    path('tasks/delete/<int:pk>/',views.delete_task),
]