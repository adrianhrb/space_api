from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
astronautrouter = routers.DefaultRouter()
router.register('missions', views.SpaceMissionsViewSet, basename='missions')

urlpatterns = [
    path('missions/success/', views.SuccessMissions.as_view()),
    path('missions/unsuccess/', views.UnsuccessMission.as_view()),
    path('missions/company/<company_name>/', views.SpaceMissionByCompany.as_view()),
    path('missions/name/<mission_name>/', views.SpaceMissionByMissionName.as_view()),
    path('missions/rocket/<rocket>/', views.SpaceMissionsByRocket.as_view()),
    path('missions/location/<location>/', views.SpaceMissionsByLocation.as_view()),
    path('astronauts/', views.AstronautsListView.as_view()),
    path('astronauts/<pk>/', views.AstronautsRetrieveView.as_view()),
    path('astronauts/nationality/<nationality>/', views.AstronautsByNationality.as_view()),
    path('astronauts/name/<name>/', views.AstronautsByName.as_view()),
    path('astronauts/mission/<mission>/', views.AstronautsByMission.as_view()),
    path('', include(router.urls)),
]
