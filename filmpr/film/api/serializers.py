from rest_framework import serializers
from film.models import ActorModel, FilmModel, LikeModel, CommentModel, CategoryModel, ViewNumberModel

class ActorModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"

class ActorModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"

class ActorModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"


class FilmModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"


class LikeModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = "__all__"


class CommentModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"       


class CategoryModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class ViewNumberModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewNumberModel
        fields = "__all__"


