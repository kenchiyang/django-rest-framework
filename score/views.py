# Create your views here.
from score.models import Score
from score.serializers import ScoreSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    #permission_classes = (IsAuthenticated,)