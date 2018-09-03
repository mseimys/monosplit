import requests
from django.conf import settings

class Notebook(object):
    def __init__(self, data):
        self.name = data.get('name')
        self.owner = data.get('uuid')
        self._notes = data.get('notes', [])

    @property
    def notes(self):
        return self._notes

def get_notebooks(uuid):
    headers = {'OWNER-ID': str(uuid)}
    url = settings.NOTEBOOK_URL.rstrip('/') + '/api/notebooks'
    response = requests.get(url, headers=headers)
    return [Notebook(data) for data in response.json()]
