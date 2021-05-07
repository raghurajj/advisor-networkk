from rest_framework import serializers
from .models import Advisor

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id','name', 'profile_pic'] 