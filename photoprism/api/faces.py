from photoprism.api.base import PhotoprismApiBase
from photoprism.models import form, search, entity


class PhotoprismFacesApi(PhotoprismApiBase):
    async def search_full(self, params: form.SearchFaces) -> list[search.Face]:
        data = await self._session.req(
            method="GET",
            path="faces",
            params=params.model_dump(exclude_none=True),
        )
        return [search.Face(**item) for item in data]

    async def get_by_id(self, face_id: str) -> search.Face:
        data = await self._session.req(
            method="GET",
            path="faces/{}".format(face_id),
        )
        return search.Face(**data)

    async def update(self, face_id: str, face_update: form.Face) -> entity.Face:
        data = await self._session.req(
            method="PUT",
            path="faces/{}".format(face_id),
            data=face_update.model_dump(exclude_none=True),
        )
        return entity.Face(**data)
