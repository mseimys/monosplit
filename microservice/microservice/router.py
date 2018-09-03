from rest_framework.routers import DefaultRouter

from notebook.api import NotebookViewSet, NoteViewSet


router = DefaultRouter()
router.register(r'api/notebooks', NotebookViewSet, base_name='notebook')
router.register(r'api/notes', NoteViewSet, base_name='note')
