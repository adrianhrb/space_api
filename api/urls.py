from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('missions', views.SpaceMissionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('missions/company/<company_name>/', views.SpaceMissionByCompany.as_view())
]
