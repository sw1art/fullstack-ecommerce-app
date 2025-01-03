from rest_framework import serializers
from .models import ActionLog

class ActionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionLog
        fields = ['log_id', 'user', 'action_type', 'action_description', 'ip_address', 'user_agent', 'created_at']
