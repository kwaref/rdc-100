from rest_framework import generics

from .serializers import ClipSerializer
from .models import Clip
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# class ClipView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         clips = Clip.objects.all()
#         serializer = ClipSerializer(clips, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         clips_serializer = ClipSerializer(data=request.data)
#         if clips_serializer.is_valid():
#             clips_serializer.save()
#             return Response(clips_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', clips_serializer.errors)
#             return Response(clips_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClipList(generics.ListCreateAPIView):
    # parser_classes = (MultiPartParser, FormParser)
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer


class ClipDetail(generics.RetrieveDestroyAPIView):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
