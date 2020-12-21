from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.business_logic import send_request_to_imdb, send_request_to_open_lib
from app.serializers import IMDBSerializer, LibrarySerializer


class IMDBAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, **kwargs) -> Response:
        serializer = IMDBSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        imdb_response = send_request_to_imdb(**serializer.validated_data)
        return Response(imdb_response)


class OpenLibraryAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, **kwargs) -> Response:
        serializer = LibrarySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        lib_response = send_request_to_open_lib(**serializer.validated_data)
        return Response(lib_response)


# write one test for business_logic.py
