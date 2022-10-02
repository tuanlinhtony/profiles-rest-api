from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API view"""

    def get(self, requets, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "This is API View"
        ]

        return Response({'message': 'Helloo', 'an_apiview': an_apiview})
