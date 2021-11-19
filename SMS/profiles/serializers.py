from rest_framework import serializers, viewsets
from .models import Profile



# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'username',
            'avatar',
            'XP',
            'info',
            'level',
            'global_rank',
            'puzzles_completed',
            'courses_completed',
            'languages'
        ]


class HighscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'username',
            'XP',
            'level',
        ]
    