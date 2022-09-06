from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include('myblog.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]