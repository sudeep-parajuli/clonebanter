from banter_app.api.serializers import *
from banter_app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateContactView(APIView):
       
    def post(self, request):
        serializer = CreateContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
