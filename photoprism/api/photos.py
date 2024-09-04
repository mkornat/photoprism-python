from pathlib import Path

from photoprism.api.base import PhotoprismApiBase
from photoprism.models import search, form, entity


class PhotoprismPhotosApi(PhotoprismApiBase):
    async def search_full(
        self,
        count: int,
        offset: int | None = None,
        order: str | None = None,
        merged: bool | None = None,
        public: bool | None = None,
        quality: int = 0,
        query: str | None = None,
        album_uid: str | None = None,
        path: str | None = None,
        video: bool | None = None,
    ) -> list[search.Photo]:
        search_query = form.SearchPhotos(
            count=count,
            offset=offset,
            order=order,
            merged=merged,
            public=public,
            quality=quality,
            q=query,
            s=album_uid,
            path=path,
            video=video,
        )
        data = await self._session.req(
            method="GET",
            path="photos",
            params=search_query.model_dump(exclude_none=True),
        )
        return [search.Photo(**item) for item in data]

    async def search_viewer(
        self,
        count: int,
        offset: int | None = None,
        order: str | None = None,
        merged: bool | None = None,
        public: bool | None = None,
        quality: int = 0,
        query: str | None = None,
        album_uid: str | None = None,
        path: str | None = None,
        video: bool | None = None,
    ) -> list[search.Result]:
        search_query = form.SearchPhotos(
            count=count,
            offset=offset,
            order=order,
            merged=merged,
            public=public,
            quality=quality,
            q=query,
            s=album_uid,
            path=path,
            video=video,
        )
        data = await self._session.req(
            method="GET",
            path="photos/view",
            params=search_query.model_dump(exclude_none=True),
        )
        return [search.Result(**item) for item in data]

    async def get_by_uid(self, photo_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="GET",
            path="photos/{}".format(photo_uid),
        )
        return entity.Photo(**data)

    async def approve(self, photo_uid: str) -> None:
        await self._session.req(
            method="POST",
            path="photos/{}/approve".format(photo_uid),
        )

    async def set_favorite(self, photo_uid: str, favorite: bool) -> None:
        await self._session.req(
            method="POST" if favorite else "DELETE",
            path="photos/{}/like".format(photo_uid),
        )

    async def update(self, photo_uid: str, photo_data: form.Photo) -> entity.Photo:
        data = await self._session.req(
            method="PUT",
            path="photos/{}".format(photo_uid),
            data=photo_data.model_dump(exclude_none=True),
        )
        return entity.Photo(**data)

    async def download(
        self, photo_uid: str, file_dir: Path, filename: str | None = None
    ) -> Path:
        return await self._session.req(
            method="GET",
            path="photos/{}/dl".format(photo_uid),
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )

    async def set_primary(self, photo_uid: str, file_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="POST",
            path="photos/{}/files/{}/primary".format(photo_uid, file_uid),
        )
        return entity.Photo(**data)

    async def add_label(self, photo_uid: str, label: form.Label) -> entity.Photo:
        data = await self._session.req(
            method="POST",
            path="photos/{}/label".format(photo_uid),
            data=label.model_dump(),
        )
        return entity.Photo(**data)

    async def remove_label(self, photo_uid: str, label_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="DELETE",
            path="photos/{}/label/{}".format(photo_uid, label_uid),
        )
        return entity.Photo(**data)

    async def update_label(self, photo_uid: str, label_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="PUT",
            path="photos/{}/label/{}".format(photo_uid, label_uid),
        )
        return entity.Photo(**data)

    async def unstack(self, photo_uid: str, file_uid: str) -> entity.Photo:
        data = await self._session.req(
            method="POST",
            path="photos/{}/files/{}/unstack".format(photo_uid, file_uid),
        )
        return entity.Photo(**data)

    async def batch_delete(self, selection: form.Selection) -> None:
        await self._session.req(
            method="POST",
            path="batch/photos/delete",
            data=selection.model_dump(exclude_none=True),
        )

    async def batch_toggle_private(self, selection: form.Selection) -> None:
        await self._session.req(
            method="POST",
            path="batch/photos/private",
            data=selection.model_dump(exclude_none=True),
        )

    async def batch_approve(self, selection: form.Selection) -> None:
        await self._session.req(
            method="POST",
            path="batch/photos/approve",
            data=selection.model_dump(exclude_none=True),
        )

    async def batch_restore(self, selection: form.Selection) -> None:
        await self._session.req(
            method="POST",
            path="batch/photos/restore",
            data=selection.model_dump(exclude_none=True),
        )

    async def batch_archive(self, selection: form.Selection) -> None:
        await self._session.req(
            method="POST",
            path="batch/photos/archive",
            data=selection.model_dump(exclude_none=True),
        )
