from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Astronauts, SpaceMissions
from .serializers import AstronautsSerializer, SpaceMissionsSerializer


# SPACE MISSIONS ENDPOINTS
class SpaceMissionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint to retrieve list and detail space missions
    """

    queryset = SpaceMissions.objects.all()
    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SpaceMissionByCompany(ListAPIView):
    """
    API endpoint to retrieve space missions by company name
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        company_name = self.kwargs['company_name']
        return SpaceMissions.objects.filter(company__icontains=company_name)


class SpaceMissionByMissionName(ListAPIView):
    """
    API endpoint to retrieve space missions by mission name
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        mission_name = self.kwargs['mission_name']
        return SpaceMissions.objects.filter(mission__icontains=mission_name)


class SuccessMissions(ListAPIView):
    """
    API endpoint to retrieve all missions with success
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SpaceMissions.objects.filter(success=True)


class UnsuccessMission(ListAPIView):
    """
    API endpoint to retrieve all unsuccessful missions
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SpaceMissions.objects.filter(success=False)


class SpaceMissionsByRocket(ListAPIView):
    """
    API endpoint to retrieve missions by rocket name
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        rocket = self.kwargs['rocket']
        return SpaceMissions.objects.filter(rocket__icontains=rocket)


class SpaceMissionsByLocation(ListAPIView):
    """
    API endpoint to retrieve missions by location name
    """

    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        location = self.kwargs['location']
        return SpaceMissions.objects.filter(location__icontains=location)


# ASTRONAUTS ENDPOINTSi
class AstronautsListView(ListAPIView):
    """
    API endpoint to retrieve all astronauts
    """

    queryset = Astronauts.objects.all()
    serializer_class = AstronautsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AstronautsRetrieveView(RetrieveAPIView):
    """
    API endpoint to retrieve a single astronaut by id
    """

    queryset = Astronauts.objects.all()
    serializer_class = AstronautsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AstronautsByNationality(ListAPIView):
    """
    API endpoint to retrieve astronauts by their nationality
    """

    serializer_class = AstronautsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        nationality = self.kwargs['nationality']
        return Astronauts.objects.filter(nationality__icontains=nationality)


class AstronautsByName(ListAPIView):
    """
    API endpoint to retrieve astronauts by their name
    """

    serializer_class = AstronautsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        name = self.kwargs['name']
        return Astronauts.objects.filter(fullname__icontains=name)


class AstronautsByMission(ListAPIView):
    """
    API endpoint to retrieve astronauts by the mission name
    """

    serializer_class = AstronautsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        mission = self.kwargs['mission']
        return Astronauts.objects.filter(mission__icontains=mission)
