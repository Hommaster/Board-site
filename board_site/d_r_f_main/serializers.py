from rest_framework import serializers
from board.models import *


class BbSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bb
        fields = "__all__"


