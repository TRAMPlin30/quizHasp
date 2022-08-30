from django.urls import path

from workers.views import worker_create

app_name = 'workers'

urlpatterns = [
    path('worker_create/', worker_create, name='worker_create'),
]