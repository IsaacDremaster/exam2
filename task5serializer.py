from rest_framework import serializers
from task5 import Universe, Team


class UniverseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universe
        fields = ('__all__', )


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', )