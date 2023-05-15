from krBackend.serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsUserOrReadOnly, IsAuthorUpdateOnly, IsAdmin


class ArticleAPIListAndPost(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView,
                       generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorUpdateOnly,)


class AuthorAPIPost(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class AuthorAPIAdmList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdmin,)


#class UserAPIList(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = (IsAdmin,)

#class ArticleViewSet(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.ListModelMixin,
#                     GenericViewSet):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer


#class AuthorViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#    queryset = Author.objects.all()
#    serializer_class = AuthorSerializer


# Create your views here.


# Create your views here.
