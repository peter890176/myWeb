from django.urls import path
from .views import ActivePersonalInfoView

urlpatterns = [
    path('info/', ActivePersonalInfoView.as_view(), name='active-personal-info'),
] 