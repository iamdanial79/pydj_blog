from typing_extensions import Required
from  rest_framework import serializers

class singlearticleserialazers(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=130)
    cover = serializers.ImageField(required=True, allow_null=False)
    content = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=2050)
    created_at = serializers.DateTimeField(required=True, allow_null=False)


class SubmitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=130)
    cover = serializers.ImageField(required=True , allow_null= False)
    content = serializers.CharField(required=True, allow_null =False, allow_blank=False, max_length=2050)
    category_id = serializers.IntegerField(required=True, allow_null =False)
    author_id = serializers.IntegerField(required=True, allow_null =False)
    poromote = serializers.BooleanField(required=True, allow_null=False )


class UpdateCoverSerializers(serializers.Serializer):
    article_id = serializers.IntegerField(required=True,allow_null= False)
    cover = serializers.ImageField(required =True , allow_null= False , allow_empty_file=False)

class DeleteArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True , allow_null=False)