from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/schedule/new/', views.schedule_create, name='schedule_create'),
    path('schedule/<int:schedule_id>/update/', views.schedule_update, name='schedule_update'),
    path('schedule/<int:schedule_id>/delete/', views.schedule_delete, name='schedule_delete'),
]