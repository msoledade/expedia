from api.models import Process
from api.serializers import ProcessSerializer
from rest_framework import generics

class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
