from rest_framework import serializers

class TextSerializer(serializers.Serializer):
    neg = serializers.DecimalField(max_digits=5,decimal_places=3)
    neu = serializers.DecimalField(max_digits=5,decimal_places=3)
    pos = serializers.DecimalField(max_digits=5,decimal_places=3)
    pos = serializers.DecimalField(max_digits=5,decimal_places=3)
    overall = serializers.CharField(max_length=20)