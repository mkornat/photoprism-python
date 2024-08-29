from abc import ABC

from photoprism.session import PhotoprismSession


class PhotoprismApiBase(ABC):
    def __init__(self, session: PhotoprismSession):
        self._session = session
