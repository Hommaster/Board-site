from django.contrib.auth.models import User 
from rest_framework import serializers
from board.models import *


class BbSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bb
        fields = ("title", "photo", "slug", "content", "price", "published", "rubric")


class RubricSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rubric 
        fields = ("id", "name", )


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = UserProfileUploads 
        fields = ("user", "product", )
