"""
API for notebook microservice
"""

from rest_framework import serializers, viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from notebook.models import Notebook, Note

class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = Notebook
        fields = ('url', 'name', 'owner', 'notes')


class NotebookViewSet(viewsets.ModelViewSet):
    serializer_class = NotebookSerializer

    def get_queryset(self):
        # return Notebook.objects.all()
        owner_id = self.request.META.get('HTTP_OWNER_ID')
        if owner_id:
            return Notebook.objects.filter(owner=owner_id)
        return Notebook.objects.none()

    @detail_route(methods=['get', 'post'])
    def notes(self, request, pk):
        if request.method == 'GET':
            notebook = self.get_object()
            notes = notebook.notes.all()
            return Response([note.text for note in notes])

        data = request.data
        data.update(notebook=pk)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
