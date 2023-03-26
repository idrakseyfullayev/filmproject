from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from film.api.serializers import (
    ActorModelListSerializer, ActorModelCreateSerializer, ActorModelUpdateSerializer,
    FilmModelListSerializer,
    LikeModelListSerializer,
    CommentModelListSerializer,
    CategoryModelListSerializer,
    ViewNumberModelListSerializer,)
from film.models import ActorModel, FilmModel, LikeModel, CommentModel, CategoryModel, ViewNumberModel


class ActorModelListAPIview(ListAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorModelListSerializer

class ActorModelCreateAPIView(CreateAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorModelCreateSerializer

class ActorModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ActorModel.objects.all()
    lookup_field = "id"
    serializer_class = ActorModelUpdateSerializer

class ActorModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = ActorModel.objects.all()
    lookup_field = "id"
    serializer_class = ActorModelListSerializer


class FilmModelListAPIView(ListAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmModelListSerializer

class FilmModelCreateAPIView(CreateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmModelListSerializer

class FilmModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = FilmModel.objects.all()
    lookup_field = "id"
    serializer_class = FilmModelListSerializer

class FilmModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = FilmModel.objects.all()
    lookup_field = "id"
    serializer_class = FilmModelListSerializer


class LikeModelListAPIView(ListAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeModelListSerializer

class LikeModelCreateAPIView(CreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeModelListSerializer

class LikeModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = LikeModel.objects.all()
    lookup_field = "id"
    serializer_class = LikeModelListSerializer

class LikeModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = LikeModel.objects.all()
    lookup_field = "id"
    serializer_class = LikeModelListSerializer



class CommentModelListAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelListSerializer

class CommentModelCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelListSerializer

class CommentModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = "id"
    serializer_class = CommentModelListSerializer

class CommentModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = "id"
    serializer_class = CommentModelListSerializer



class CategoryModelListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelListSerializer

class CategoryModelCreateAPIView(CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelListSerializer

class CategoryModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CategoryModel.objects.all()
    lookup_field = "id"
    serializer_class = CategoryModelListSerializer

class CategoryModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = CategoryModel.objects.all()
    lookup_field = "id"
    serializer_class = CategoryModelListSerializer


class ViewNumberModelListAPIView(ListAPIView):
    queryset = ViewNumberModel.objects.all()
    serializer_class = ViewNumberModelListSerializer

class ViewNumberModelCreateAPIView(CreateAPIView):
    queryset = ViewNumberModel.objects.all()
    serializer_class = ViewNumberModelListSerializer

class ViewNumberModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ViewNumberModel.objects.all()
    lookup_field = "id"
    serializer_class = ViewNumberModelListSerializer    

class ViewNumberModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = ViewNumberModel.objects.all()
    lookup_field = "id"
    serializer_class = ViewNumberModelListSerializer

    