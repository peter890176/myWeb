from django.urls import path
from .views import resume

urlpatterns = [
    path('api/resume/', resume, name='resume'),
]