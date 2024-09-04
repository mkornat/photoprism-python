import asyncio
from pathlib import Path
from typing import Any, Literal, overload, Mapping

import aiohttp
from aiohttp import ClientTimeout
from yarl import URL

from photoprism.exceptions import (
    PhotoprismUnauthorizedError,
    PhotoprismNotFoundError,
    PhotoprismBadRequestError,
    PhotoprismTimeoutError,
    PhotoprismError,
)


class PhotoprismSession:
    DEFAULT_TIMEOUT = 10.0

    def __init__(
        self,
        username: str,
        password: str,
        host: str,
        protocol: Literal["http", "https"] = "http",
        timeout: float = DEFAULT_TIMEOUT,
        loop: asyncio.AbstractEventLoop | None = None,
    ):
        self._username = username
        self._password = password
        self._url = f"{protocol}://{host}/api/v1/"
        self._user_agent = "Photoprism Python Client"
        self._timeout = ClientTimeout(total=timeout)
        self._auth_token: str | None = None
        self._download_token: str | None = None
        self._preview_token: str | None = None
        self._loop = loop or asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self._loop)

    @property
    def default_headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "User-Agent": self._user_agent,
        }

    @overload
    async def req(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        method: Literal["GET", "POST", "PUT", "DELETE"] = "GET",
        mode: Literal["JSON"] = "JSON",
        file_dir: None = None,
        filename: None = None,
        timeout: float | None = None,
        include_auth_token: bool = True,
    ) -> dict[str, Any] | list[dict[str, Any]]: ...

    @overload
    async def req(
        self,
        path: str,
        file_dir: Path,
        mode: Literal["DOWNLOAD", "PREVIEW"],
        filename: str | None = None,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        method: Literal["GET", "POST", "PUT", "DELETE"] = "GET",
        timeout: float | None = None,
        include_auth_token: bool = True,
    ) -> Path: ...

    async def req(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        method: Literal["GET", "POST", "PUT", "DELETE"] = "GET",
        mode: Literal["JSON", "DOWNLOAD", "PREVIEW"] = "JSON",
        file_dir: Path | None = None,
        filename: str | None = None,
        timeout: float | None = None,
        include_auth_token: bool = True,
    ) -> dict[str, Any] | Path:
        if timeout is None:
            timeout = self._timeout
        else:
            timeout = ClientTimeout(total=timeout)
        auth_token = (await self.get_auth_token()) if include_auth_token else None
        headers = {
            **self.default_headers,
            **(headers or {}),
            **({"Authorization": f"Bearer {auth_token}"} if auth_token else {}),
        }
        params = params or {}
        if mode == "DOWNLOAD":
            params["t"] = await self.get_download_token()
        elif mode == "PREVIEW":
            params["t"] = await self.get_preview_token()
        cleaned_params = {p_k: p_v for p_k, p_v in params.items() if p_v is not None}
        url = URL(self._url).join(URL(path)).update_query(cleaned_params)
        try:
            async with self._session.request(
                method=method,
                url=url,
                json=data,
                headers=headers,
                raise_for_status=True,
                timeout=timeout,
            ) as response:
                if mode == "JSON":
                    return await response.json()
                elif mode in ("DOWNLOAD", "PREVIEW"):
                    filename = filename or self.determine_filename(response.headers)
                    file_path = file_dir / filename
                    with open(file_path, "wb") as f:
                        async for chunk, _ in response.content.iter_chunks():
                            f.write(chunk)
                    await self._session.close()
                    return file_path

        except aiohttp.ClientResponseError as exc:
            await self._session.close()
            match exc.status:
                case 401 | 403:
                    raise PhotoprismUnauthorizedError(exc) from exc
                case 404:
                    raise PhotoprismNotFoundError(exc) from exc
                case 400:
                    raise PhotoprismBadRequestError(exc) from exc
                case _:
                    raise PhotoprismError(exc) from exc
        except asyncio.TimeoutError as exc:
            await self._session.close()
            raise PhotoprismTimeoutError from exc
        except Exception as exc:
            await self._session.close()
            raise PhotoprismError(exc) from exc

    def determine_filename(self, headers: Mapping[str, str]) -> str:
        header_filename = headers["Content-Disposition"].split("; ")[1].split("=")[1]
        # Sometimes the filename in the header is enclosed, sometimes it isn't.
        # This is to account for that.
        if header_filename[0] == '"' and header_filename[-1:] == '"':
            filename = header_filename[1:-1]
        else:
            filename = header_filename
        return filename

    async def get_auth_token(self) -> str:
        if self._auth_token is None:
            response = await self.req(
                path="session",
                data={
                    "username": self._username,
                    "password": self._password,
                },
                method="POST",
                include_auth_token=False,
            )
            self._auth_token = response["access_token"]
            self._download_token = response["config"]["downloadToken"]
            self._preview_token = response["config"]["previewToken"]
        return self._auth_token

    async def get_download_token(self) -> str:
        if self._download_token is None:
            await self.get_auth_token()
        return self._download_token

    async def get_preview_token(self) -> str:
        if self._preview_token is None:
            await self.get_auth_token()
        return self._preview_token
