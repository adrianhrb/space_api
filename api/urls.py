from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('missions', views.SpaceMissionsViewSet)

urlpatterns = [
    path('missions/company/<company_name>/', views.SpaceMissionByCompany.as_view()),
    path('missions/name/<mission_name>/', views.SpaceMissionByMissionName.as_view()),
    path('missions/success/', views.SuccessMissions.as_view()),
    path('missions/unsuccess/', views.UnsuccessMission.as_view()),
    path('', include(router.urls)),
]
