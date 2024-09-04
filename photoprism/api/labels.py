from pathlib import Path

from photoprism.api.base import PhotoprismApiBase
from photoprism.models import form, search, entity, query


class PhotoprismLabelsApi(PhotoprismApiBase):
    async def search(self, search_labels: form.SearchLabels) -> list[search.Label]:
        data = await self._session.req(
            method="GET", path="labels", params=search_labels.model_dump()
        )
        return [search.Label(**item) for item in data]

    async def set_favorite(self, label_uid: str, favorite: bool) -> None:
        await self._session.req(
            method="POST" if favorite else "DELETE",
            path="labels/{}/favorite".format(label_uid),
        )

    async def update(self, label_uid: str, name: str) -> entity.Label:
        label_data = form.Label(
            name=name,
        )
        data = await self._session.req(
            method="PUT",
            path="labels/{}".format(label_uid),
            data=label_data.model_dump(),
        )
        return entity.Label(**data)

    async def batch_delete(self, label_uids: list[str]) -> None:
        selection_data = form.Selection(
            labels=label_uids,
        )
        await self._session.req(
            method="POST",
            path="batch/labels/delete",
            data=selection_data.model_dump(),
        )

    async def download_cover_image(
        self,
        label_uid: str,
        size: query.Size,
        file_dir: Path,
        filename: str | None = None,
    ) -> Path:
        token = await self._session.get_download_token()
        return await self._session.req(
            method="GET",
            path="labels/{}/t/{}/{}".format(label_uid, token, size),
            params={"download": "download"},
            file_dir=file_dir,
            filename=filename,
            mode="DOWNLOAD",
        )
