from photoprism.api.base import PhotoprismApiBase
from photoprism.models import entity


class PhotoprismErrorsApi(PhotoprismApiBase):
    async def search(
        self,
        count: int,
        offset: int | None = None,
        q: str | None = None,
    ) -> list[entity.Error]:
        data = await self._session.req(
            method="GET",
            path="errors",
            params={"count": count, "offset": offset, "q": q},
        )
        return [entity.Error(**item) for item in data]

    async def clear(self) -> None:
        await self._session.req(method="DELETE", path="errors")
