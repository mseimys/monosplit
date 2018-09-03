"""
API for notebook microservice
"""

from rest_framework import serializers, viewsets
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
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
