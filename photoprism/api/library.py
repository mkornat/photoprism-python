from photoprism.api.base import PhotoprismApiBase
from photoprism.models import form


class PhotoprismLibraryApi(PhotoprismApiBase):
    async def index(self, options: form.IndexOptions) -> None:
        await self._session.req(
            method="POST",
            path="index",
            data=options.model_dump(),
        )
