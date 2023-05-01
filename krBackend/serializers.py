from krBackend.models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = '__all__'
