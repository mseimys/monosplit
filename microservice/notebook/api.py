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
    serializer_class = NotebookSerializer

    def get_queryset(self):
        owner_id = self.request.META.get('HTTP_OWNER_ID')
        if owner_id:
            return Notebook.objects.filter(owner=owner_id)
        return Notebook.objects.none()


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
