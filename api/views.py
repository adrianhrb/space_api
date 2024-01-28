from rest_framework import viewsets

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import SpaceMissions
from .serializers import SpaceMissionsSerializer

class SpaceMissionsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to get all space missions
    '''
    queryset = SpaceMissions.objects.all()
    serializer_class = SpaceMissionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SpaceMissionByCompany(ListAPIView):
    serializer_class = SpaceMissionsSerializer
    
    def get_queryset(self):
        company_name = self.kwargs['company_name']
        return SpaceMissions.objects.filter(company__icontains=company_name)
    