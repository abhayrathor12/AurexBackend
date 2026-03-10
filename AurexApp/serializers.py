from rest_framework import serializers
from .models import StartupApplication,Contact,InvestorApplication,EventRegistration



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
        

class EventRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRegistration
        fields = "__all__"

    def validate_bootstrapped(self, value):
        if isinstance(value, str):
            return value.lower() == "true"
        return value

    def validate_interested_in_pitching(self, value):
        if isinstance(value, str):
            return value.lower() == "true"
        return value