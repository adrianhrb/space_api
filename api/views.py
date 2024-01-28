from rest_framework import viewsets

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import SpaceMissions
from .serializers import SpaceMissionsSerializer

class SpaceMissionsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to retrieve all space missions
    '''
    queryset = SpaceMissions.objects.all()
    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SpaceMissionByCompany(ListAPIView):
    '''
    API endpoint to retrieve space missions by company name
    '''
    serializer_class = SpaceMissionsSerializer
    
    def get_queryset(self):
        company_name = self.kwargs['company_name']
        return SpaceMissions.objects.filter(company__icontains=company_name)

class SpaceMissionByMissionName(ListAPIView):
    '''
    API endpoint to retrieve space missions by mission name
    '''
    serializer_class = SpaceMissionsSerializer

    def get_queryset(self):
        mission_name = self.kwargs['mission_name']
        return SpaceMissions.objects.filter(mission__icontains=mission_name)


class SuccessMissions(ListAPIView):
    queryset = SpaceMissions.objects.filter(success=True)
    
    def list(self, request):
        success_misions = self.get_queryset()
        serializer = SpaceMissionsSerializer(success_misions)
        return Response(serializer.data)

# class SuccessMissions(ListAPIView):
#     '''
#     API endpoint to retrieve all succcesful missions
#     '''
#     serializer_class = SpaceMissionsSerializer

#     def get_queryset(self):
#         return SpaceMissions.objects.filter(success=True)
    
# class UnsuccessMissions(ListAPIView):
#     '''
#     API endpoint to retrieve all unsucccesful missions
#     '''
#     serializer_class = SpaceMissionsSerializer

#     def get_queryset(self):
#         return SpaceMissions.objects.filter(success=False)