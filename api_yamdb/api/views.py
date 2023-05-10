from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken


from reviews.models import Title, Categorie, Genre, User, Review, Comment
from api.serializers import (
    TitleSerializer,
    GenresSerializer,
    CategoriesSerializer,
    ReviewSerializer,
    CommentSerializer,
)
from .serializers import TokenSerializer


class TitleVewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer


class ReviewVeiewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')

        title = get_object_or_404(Title, id=title_id)
        review = title.reviews.filter(id=review_id).first()

        if review is None:
            raise ValueError('У произведения нет такого отзыва')

        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')

        title = get_object_or_404(Title, id=title_id)
        review = title.reviews.filter(id=review_id).first()

        if review is None:
            raise ValueError('У произведения нет такого отзыва')

        serializer.save(author=self.request.user, review=review)


class TokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            username=serializer.validated_data['username'],
            confirmation_code=serializer.validated_data['confirmation_code'],
        )
        token = AccessToken().for_user(user)
        return Response({'token': str(token)})
