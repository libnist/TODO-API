from rest_framework import generics

from todos import models, serializers

# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    
class DetailTodo(generics.RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer