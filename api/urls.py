from rest_framework import routers
from django.urls import path, include
from .views import UserRecordView, MyUserViewSet

router = routers.DefaultRouter()
router.register('myuser', MyUserViewSet, basename='MyUser')

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='user'),
    path('', include(router.urls))
]
