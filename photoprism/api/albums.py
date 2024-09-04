from pathlib import Path
from typing import Literal

from photoprism.api.base import PhotoprismApiBase
from photoprism.models import search, entity, form, query


class PhotoprismAlbumsApi(PhotoprismApiBase):
    async def filter(
        self,
        count: int,
        offset: int | None = None,
        order: Literal["favorites", "name", "title", "added", "edited"] | None = None,
        q: str | None = None,
    ) -> list[search.Album]:
        data = await self._session.req(
            method="GET",
            path="albums",
            params={
                "count": count,
                "offset": offset,
                "order": order,
                "q": q,
            },
        )
        return [search.Album(**item) for item in data]

    async def get_by_uid(self, album_uid: str) -> entity.Album:
        data = await self._session.req(
            method="GET",
            path="albums/{}".format(album_uid),
        )
        return entity.Album(**data)

    async def create(self, title: str, favorite: bool = False) -> entity.Album:
        data = await self._session.req(
            method="POST",
            path="albums",
            data={
                "Title": title,
                "Favorite": favorite,
            },
        )
        return entity.Album(**data)

    async def update(self, album_uid: str, album_data: form.Album) -> entity.Album:
        data = await self._session.req(
            method="PUT",
            path="albums/{}".format(album_uid),
            data=album_data.model_dump(),
        )
        return entity.Album(**data)

    async def delete(self, album_uid: str) -> None:
        await self._session.req(
            method="DELETE",
            path="albums/{}".format(album_uid),
        )

    async def batch_delete(self, album_uids: list[str]) -> None:
        selection_data = form.Selection(
            albums=album_uids,
        )
        await self._session.req(
            method="POST",
            path="batch/albums/delete",
            data=selection_data.model_dump(),
        )

    async def clone(
        self, source_album_uids: list[str], destination_album_uid: str
    ) -> entity.Album:
        selection_data = form.Selection(albums=source_album_uids)
        data = await self._session.req(
            method="POST",
            path="albums/{}/clone".format(destination_album_uid),
            data=selection_data.model_dump(),
        )
        return entity.Album(**data["a"])

    async def create_link(
        self,
        album_uid: str,
        slug: str,
        max_views: int | None = None,
        expire_seconds: int | None = None,
        password: str | None = None,
    ) -> entity.Link:
        link_data = form.Link(
            share_slug=slug,
            max_views=max_views,
            link_expires=expire_seconds,
            password=password,
        )
        data = await self._session.req(
            method="POST",
            path="albums/{}/links".format(album_uid),
            data=link_data.model_dump(),
        )
        return entity.Link(**data)

    async def update_link(
        self,
        album_uid: str,
        link_uid: str,
        slug: str | None = None,
        max_views: int | None = None,
        expire_seconds: int | None = None,
        password: str | None = None,
        link_token: str | None = None,
    ) -> entity.Link:
        link_data = form.Link(
            share_slug=slug,
            max_views=max_views,
            link_expires=expire_seconds,
            password=password,
            link_token=link_token,
        )
        data = await self._session.req(
            method="PUT",
            path="albums/{}/links/{}".format(album_uid, link_uid),
            data=link_data.model_dump(),
        )
        return entity.Link(**data)

    async def delete_link(
        self,
        album_uid: str,
        link_uid: str,
    ) -> None:
        await self._session.req(
            method="DELETE",
            path="albums/{}/links/{}".format(album_uid, link_uid),
        )

    async def get_links(self, album_uid: str) -> list[entity.Link]:
        data = await self._session.req(
            method="GET",
            path="albums/{}/links".format(album_uid),
        )
        return [entity.Link(**item) for item in data]

    async def set_favorite(self, album_uid: str, favorite: bool) -> None:
        await self._session.req(
            method="POST" if favorite else "DELETE",
            path="albums/{}/like".format(album_uid),
        )

    async def add_photos(
        self,
        album_uid: str,
        files: list[str] | None = None,
        photos: list[str] | None = None,
        albums: list[str] | None = None,
        labels: list[str] | None = None,
        places: list[str] | None = None,
        subjects: list[str] | None = None,
    ) -> entity.Album:
        selection_data = form.Selection(
            files=files,
            photos=photos,
            albums=albums,
            labels=labels,
            places=places,
            subjects=subjects,
        )
        data = await self._session.req(
            method="POST",
            path="albums/{}/photos".format(album_uid),
            data=selection_data.model_dump(),
        )
        return entity.Album(**data)

    async def remove_photos(
        self,
        album_uid: str,
        photos: list[str],
    ) -> entity.Album:
        selection_data = form.Selection(
            photos=photos,
        )
        data = await self._session.req(
            method="DELETE",
            path="albums/{}/photos".format(album_uid),
            data=selection_data.model_dump(),
        )
        return entity.Album(**data)

    async def download_to_zip(
        self,
        album_uid: str,
        file_dir: Path,
        filename: str | None = None,
    ) -> Path:
        return await self._session.req(
            method="GET",
            path="albums/{}/dl".format(album_uid),
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )

    async def download_cover_image(
        self,
        album_uid: str,
        size: query.Size,
        file_dir: Path,
        filename: str | None = None,
    ) -> Path:
        token = await self._session.get_download_token()
        return await self._session.req(
            method="GET",
            path="albums/{}/t/{}/{}".format(album_uid, token, size),
            params={"download": "download"},
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )
