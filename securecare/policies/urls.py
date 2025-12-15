from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('add/', views.add_policy, name='add'),
    path('edit/<int:policy_id>/', views.edit_policy, name='edit_policy'),
    path('delete/<int:policy_id>/', views.delete_policy, name='delete_policy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:policy_id>/', views.take_quiz, name='take_quiz'),
]
