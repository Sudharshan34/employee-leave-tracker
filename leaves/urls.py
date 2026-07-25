from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('my-leaves/', views.my_leaves, name='my_leaves'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    path('manage/<int:leave_id>/<str:new_status>/', views.update_leave_status, name='update_leave_status'),
]