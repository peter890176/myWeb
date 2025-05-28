from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = [
            'full_name',
            'job_title',
            'bio',
            'skills_summary',
            'experience_summary',
            'hobbies',
            'contact_email',
            'additional_info', 
        ] 