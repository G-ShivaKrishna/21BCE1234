from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_task(request):
    t=Task.objects.all()
    s=TaskSerializer(t,many=True)
    return Response(s.data)


@api_view(['POST'])
def add_task(request):
    s = TaskSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_task(request, pk):
    try:
        t = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    s = TaskSerializer(t)
    return Response(s.data)


@api_view(['PUT'])
def update_task(request, pk):
    try:
        t = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    s = TaskSerializer(instance=t, data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        t = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    t.delete()
    return Response({'message': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
