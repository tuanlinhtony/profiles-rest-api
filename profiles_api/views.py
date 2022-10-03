from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, requets, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "This is API View"
        ]

        return Response({'message': 'Helloo', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of a object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete a object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test APIViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'This is API ViewSet'
        ]

        return Response({'message' : 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle remove an object"""
        return Response({'method': 'DELETE'})