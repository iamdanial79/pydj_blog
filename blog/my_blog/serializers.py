from  rest_framework import serializers

class singlearticleserialazers(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=130)
    cover = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=260)
    content = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=2050)
    created_at = serializers.DateTimeField(required=True, allow_null=False)