from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class DownloadName(StrEnum):
    FILE = "file"
    ORIGINAL = "original"
    SHARE = "share"


class DownloadSettings(BaseModel):
    disabled: bool = False
    media_raw: bool = Field(alias="mediaRaw")
    media_sidecar: bool = Field(alias="mediaSidecar")
    name: DownloadName | None
    originals: bool

    @field_validator("name", mode="before")
    def validate_name(cls, v: str) -> str | None:
        if len(v) == 0:
            return None
        return v


class FeatureSettings(BaseModel):
    account: bool
    albums: bool
    archive: bool
    delete: bool
    download: bool
    edit: bool
    estimates: bool
    favorites: bool
    files: bool
    folders: bool
    import_: bool = Field(alias="import")
    labels: bool
    library: bool
    logs: bool
    moments: bool
    people: bool
    places: bool
    private: bool
    ratings: bool
    reactions: bool
    review: bool
    search: bool
    services: bool
    settings: bool
    share: bool
    upload: bool
    videos: bool


class ImportSettings(BaseModel):
    move: bool
    path: str


class IndexSettings(BaseModel):
    convert: bool
    path: str
    rescan: bool
    skip_archived: bool = Field(alias="skipArchived")


class MapsSettings(BaseModel):
    animate: int
    style: str


class SearchSettings(BaseModel):
    batch_size: int = Field(alias="batchSize")


class ShareSettings(BaseModel):
    title: str


class StackSettings(BaseModel):
    meta: bool
    name: bool
    uuid: bool


class TemplateSettings(BaseModel):
    default: str


class UiSettings(BaseModel):
    language: str
    scrollbar: bool
    theme: str
    time_zone: str = Field(alias="timeZone")
    zoom: bool


class Settings(BaseModel):
    download: DownloadSettings
    features: FeatureSettings
    import_: ImportSettings = Field(alias="import")
    index: IndexSettings
    maps: MapsSettings
    search: SearchSettings
    share: ShareSettings
    stack: StackSettings
    templates: TemplateSettings
    ui: UiSettings
