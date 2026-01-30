from rest_framework import serializers
from .models import StartupApplication,Contact,InvestorApplication



class StartupApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupApplication
        fields = "__all__"
        read_only_fields = ("id", "created_at")



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        

class InvestorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorApplication
        fields = "__all__"
        read_only_fields = ("id", "created_at")        