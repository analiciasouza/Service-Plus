from rest_framework import mixins, generics
from models import User
from serializers import UserSerializer

class UserList(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserList(mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    