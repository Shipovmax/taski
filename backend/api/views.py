from typing import Any

from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """CRUD endpoint for tasks.

    Overrides the default ``destroy`` behaviour to return the deleted
    object's representation (instead of an empty 204 body) so the React
    frontend can update its local state without an extra round trip.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(
        self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        serializer = self.get_serializer(self.get_object())
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
