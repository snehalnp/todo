from rest_framework import serializers

from .models import Todo


class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','Title','Description','Status')
