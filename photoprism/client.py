from photoprism.api.albums import PhotoprismAlbumsApi
from photoprism.api.config import PhotoprismConfigApi
from photoprism.api.labels import PhotoprismLabelsApi
from photoprism.session import PhotoprismSession


class PhotoprismClient:
    def __init__(self, session: PhotoprismSession):
        self._session = session

    @property
    def config(self) -> PhotoprismConfigApi:
        return PhotoprismConfigApi(self._session)

    @property
    def albums(self) -> PhotoprismAlbumsApi:
        return PhotoprismAlbumsApi(self._session)

    @property
    def labels(self) -> PhotoprismLabelsApi:
        return PhotoprismLabelsApi(self._session)
