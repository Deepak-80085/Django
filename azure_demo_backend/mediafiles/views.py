from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from mediafiles.storage_backends import AzureMediaStorage

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=400)

        storage = AzureMediaStorage()
        file_name = storage.save(file_obj.name, file_obj)
        file_url = storage.url(file_name)

        return Response({'url': file_url}, status=201)
