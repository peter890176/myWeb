from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def resume(request):
    data = {
        "name": "Yue Wen Peter",
        "job": "Full Stack Developer",
        "skills": ["React", "Django", "Python", "JavaScript", "Docker", "Git"]
    }
    return Response(data)