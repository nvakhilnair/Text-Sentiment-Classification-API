from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer
from .classfication import classify
# Create your views here.

class InputTextViews(views.APIView):
    def post(self, request):
        input = request.data
        data = classify(input)
        serializer = TextSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)