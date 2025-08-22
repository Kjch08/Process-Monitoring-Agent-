from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from django.utils.timezone import now
from .models import Process
from .serializers import ProcessSerializer



# Create your views here.
class ProcessDataView(APIView):
    def post(self, request):
        # 🔑 Check API key
        api_key = request.headers.get("Authorization")
        if api_key != f"Api-Key {settings.API_KEY}":
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        
        # Expecting list of processes in request.data
        serializer = ProcessSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Process data saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, hostname=None):
    #     if hostname:
    #         latest = Process.objects.filter(hostname=hostname).order_by('-timestamp')[:50]  # latest 50
    #         serializer = ProcessSerializer(latest, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response({"error": "Hostname required"}, status=status.HTTP_400_BAD_REQUEST)
    
   
    def get(self, request, hostname=None):
        if hostname:
            processes = Process.objects.filter(hostname=hostname)
        else:
            processes = Process.objects.all()
        serializer = ProcessSerializer(processes, many=True)
        return Response(serializer.data)

    # def get(self, request, hostname=None):
    #     if not hostname:
    #         return Response({"error": "Hostname required"}, status=status.HTTP_400_BAD_REQUEST)

    #     # Step 1: Find the latest timestamp for each PID on this hostname
    #     latest_per_pid = (
    #         Process.objects.filter(hostname=hostname)
    #         .values('pid')
    #         .annotate(latest_timestamp=Max('timestamp'))
    #     )

    #     # Step 2: Get the corresponding Process objects
    #     timestamps = [x['latest_timestamp'] for x in latest_per_pid]
    #     processes = Process.objects.filter(hostname=hostname, timestamp__in=timestamps)

    #     # Step 3: Serialize and return
    #     serializer = ProcessSerializer(processes, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)













""" for manually testing api -
python manage.py shell

from monitor.models import Process

Process.objects.create(
    hostname='server1',
    pid=101,
    ppid=1,
    name='TestProcess',
    cpu=20.0,
    memory=50.0
)

after this in browser- http://127.0.0.1:8000/api/process-data/server1/

"""