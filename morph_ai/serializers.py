from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=["user"])
    content = serializers.CharField()
    timestamp = serializers.DateTimeField(required=False)