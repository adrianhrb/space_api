from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('missions', views.SpaceMissionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('missions/company/<company_name>/', views.SpaceMissionByCompany.as_view()),
    path('missions/name/<mission_name>/', views.SpaceMissionByMissionName.as_view()),
    path('missions/success/', views.SuccessMissions.as_view()),
]
