from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer

# Create your views here.

class ActivePersonalInfoView(APIView):
    """
    API view to retrieve the currently active personal information.
    It fetches the latest entry marked as 'is_active'.
    """
    def get(self, request, format=None):
        try:
            # Get the latest active profile
            # Orders by -last_updated to get the newest if multiple are active (though ideally only one is)
            active_info = PersonalInfo.objects.filter(is_active=True).order_by('-last_updated').first()
            if active_info:
                serializer = PersonalInfoSerializer(active_info)
                return Response(serializer.data)
            else:
                return Response({"error": "No active personal information found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception e if you have logging setup
            return Response({"error": "An error occurred while retrieving personal information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
