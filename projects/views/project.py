from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from django.conf import settings

class project_api(APIView):
    def get(self, request):
        try:
            get_all_data = project.objects.all()
            return_object = {
                "status": "success",
                "data": experienceSerializer(get_all_data, many=True).data
            }

            for i in range(0, len(return_object["data"])):
                return_object["data"][i]["project_image"] = settings.MEDIA_BASE_URL+return_object["data"][i]["project_image"]

            return Response(data=return_object, status=200)
        except Exception as e:
            print (e)