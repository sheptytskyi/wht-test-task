from django.http.request import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from teams.models.team import TeamModel
from teams.models.person import PersonModel
from teams import services, serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = serializers.PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = serializers.TeamSerializer

    @action(methods=['POST'], detail=True, url_path='add_member/(?P<member_id>[^/.]+)')
    def add_member(self, request: HttpRequest, pk: int, member_id: int) -> Response:
        try:
            services.add_team_member(team_id=pk, member_id=member_id)
            data = self.get_serializer(self.queryset, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            data = {'error': str(e)}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=True, url_path='remove_member/(?P<member_id>[^/.]+)')
    def remove_member(self, request: HttpRequest, pk: int, member_id: int) -> Response:
        try:
            services.remove_team_member(team_id=pk, member_id=member_id)
            data = self.get_serializer(self.queryset, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            data = {'error': str(e)}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
