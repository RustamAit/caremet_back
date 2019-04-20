from django.urls import path, include
from rest_framework import routers

from helperRequestApi import views

router = routers.DefaultRouter()
router.register('helpers', views.HelperList)
router.register('helper_request', views.HelperRequestList)

urlpatterns = [
    path('', include(router.urls))

]
