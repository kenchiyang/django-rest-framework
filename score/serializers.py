from rest_framework import serializers
from score.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        # fields = '__all__'
        fields = ('id', 'name', 'score', 'last_modify_date', 'created')