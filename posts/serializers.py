from .models import Post
from django.contrib.auth.models import User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "travel_headline",
            "description",
            "from_date",
            "to_date",
            "travel_itenary",
            "author",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)

        user = User.objects.get(pk=response.get("author"))

        response["user"] = {"username": user.username, "email": user.email}

        return response
