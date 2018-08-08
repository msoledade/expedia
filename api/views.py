from django.contrib.auth.models import User
from api.models import Process
from api.serializers import UserSerializer
from api.serializers import ProcessSerializer
from rest_framework import generics
from rest_framework import permissions

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
