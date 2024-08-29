from photoprism.api.albums import PhotoprismAlbumsApi
from photoprism.api.config import PhotoprismConfigApi
from photoprism.session import PhotoprismSession


class PhotoprismClient:
    def __init__(self, session: PhotoprismSession):
        self._session = session
    
    @property
    def config(self):
        return PhotoprismConfigApi(self._session)

    @property
    def albums(self):
        return PhotoprismAlbumsApi(self._session)
