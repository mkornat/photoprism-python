from pathlib import Path

from photoprism.api.base import PhotoprismApiBase
from photoprism.models import entity, form, query


class PhotoprismFilesApi(PhotoprismApiBase):
    async def get_by_uid(self, file_hash: str) -> entity.File:
        data = await self._session.req(
            method="GET",
            path="files/{}".format(file_hash),
        )
        return entity.File(**data)

    async def download(
        self, file_hash: str, file_dir: Path, filename: str | None = None
    ) -> Path:
        return await self._session.req(
            method="GET",
            path="dl/{}".format(file_hash),
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )

    async def download_thumbnail(
        self,
        thumb: str,
        size: query.Size,
        file_dir: Path,
        filename: str | None = None,
    ) -> Path:
        token = await self._session.get_download_token()
        return await self._session.req(
            method="GET",
            path="t/{}/{}/{}".format(thumb, token, size),
            params={"download": "download"},
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )

    async def download_video(
        self,
        thumb: str,
        file_format: str,
        file_dir: Path,
        filename: str | None = None,
    ) -> Path:
        token = await self._session.get_download_token()
        return await self._session.req(
            method="GET",
            path="videos/{}/{}/{}".format(thumb, token, file_format),
            params={"download": "download"},
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )

    async def delete(self, photo_uid: str, file_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="DELETE",
            path="photos/{}/files/{}".format(photo_uid, file_uid),
        )
        return entity.Photo(**data)

    async def update_orientation(
        self, photo_uid: str, file_uid: str, orientation: int
    ) -> entity.Photo:
        orientation_data = form.File(orientation=orientation)
        data = await self._session.req(
            method="PUT",
            path="photos/{}/files/{}/orientation".format(photo_uid, file_uid),
            data=orientation_data.model_dump(),
        )
        return entity.Photo(**data)
