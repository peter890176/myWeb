from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__' # 或者明確列出您想在 API 中暴露的欄位
        # 例如: fields = ['full_name', 'job_title', 'bio', 'skills_summary', 'experience_summary', 'hobbies', 'contact_email'] 