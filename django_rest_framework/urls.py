from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from score import views

router = DefaultRouter()
router.register(r'score', views.ScoreViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]