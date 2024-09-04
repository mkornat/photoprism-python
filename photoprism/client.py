from photoprism import api
from photoprism.session import PhotoprismSession


class PhotoprismClient:
    def __init__(self, session: PhotoprismSession):
        self._session = session

    @property
    def config(self) -> api.PhotoprismConfigApi:
        return api.PhotoprismConfigApi(self._session)

    @property
    def albums(self) -> api.PhotoprismAlbumsApi:
        return api.PhotoprismAlbumsApi(self._session)

    @property
    def labels(self) -> api.PhotoprismLabelsApi:
        return api.PhotoprismLabelsApi(self._session)

    @property
    def photos(self) -> api.PhotoprismPhotosApi:
        return api.PhotoprismPhotosApi(self._session)

    @property
    def files(self) -> api.PhotoprismFilesApi:
        return api.PhotoprismFilesApi(self._session)

    @property
    def errors(self) -> api.PhotoprismErrorsApi:
        return api.PhotoprismErrorsApi(self._session)

    @property
    def faces(self) -> api.PhotoprismFacesApi:
        return api.PhotoprismFacesApi(self._session)

    @property
    def library(self) -> api.PhotoprismLibraryApi:
        return api.PhotoprismLibraryApi(self._session)
