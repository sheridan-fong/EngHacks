from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'upload/file', views.FileUploadViewSet, basename='file')
router.register(r'question', views.QuestionRandomizer, basename='question')


urlpatterns = [
	path('api/', include(router.urls)),
]


