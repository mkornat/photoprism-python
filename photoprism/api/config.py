from photoprism.api.base import PhotoprismApiBase
from photoprism.models.config import ClientConfig


class PhotoprismConfigApi(PhotoprismApiBase):
    async def get_config(self) -> ClientConfig:
        data = await self._session.req("config")
        return ClientConfig(**data)
