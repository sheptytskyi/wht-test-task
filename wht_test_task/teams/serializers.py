from rest_framework import serializers

from teams.models.team import TeamModel
from teams.models.person import PersonModel


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = TeamModel
        fields = '__all__'
