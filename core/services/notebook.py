from collections import namedtuple
import requests
from django.conf import settings

NotebookData = namedtuple('Notebook', ['name', 'notes', 'owner', 'url'])

NOTEBOOK_ROOT = settings.NOTEBOOK_URL.rstrip('/') + '/api/notebooks'

def headers(owner_uuid):
    return {'OWNER-ID': str(owner_uuid)}

class Notebook(NotebookData):
    @staticmethod
    def get_notebooks(owner_uuid):
        response = requests.get(NOTEBOOK_ROOT, headers=headers(owner_uuid))
        return [Notebook(**data) for data in response.json()]

    def add_note(self, note):
        response = requests.post(self.url + 'notes/', headers=headers(self.owner), json={'text': note})
        print('Sending `{}` to {}'.format(note, self.url))
        return response
