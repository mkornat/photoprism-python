from typing import Any

from pydantic import BaseModel, Field

from photoprism.models import entity, env, customize
from photoprism.models.base import OptionalList


class CategoryLabel(BaseModel):
    name: str = Field(alias="Name")
    slug: str = Field(alias="Slug")
    uid: str = Field(alias="UID")


class ClientCounts(BaseModel):
    albums: int
    all: int
    archived: int
    cameras: int
    countries: int
    favorites: int
    files: int
    folders: int
    hidden: int
    label_max_photos: int = Field(alias="labelMaxPhotos")
    labels: int
    lenses: int
    live: int
    moments: int
    months: int
    people: int
    photos: int
    places: int
    private: int
    private_albums: int
    private_folders: int
    private_moments: int
    private_months: int
    private_states: int
    review: int
    states: int
    stories: int
    videos: int


class ClientDisable(BaseModel):
    backups: bool
    classification: bool
    darktable: bool
    exiftool: bool
    faces: bool
    ffmpeg: bool
    heifconvert: bool
    imagemagick: bool
    jpegxl: bool
    places: bool
    raw: bool
    rawtherapee: bool
    restart: bool
    settings: bool
    sips: bool
    tensorflow: bool
    vectors: bool
    vips: bool
    webdav: bool


class ClientPosition(BaseModel):
    cid: str
    lat: float
    lng: float
    uid: str
    utc: str


class ThumbSize(BaseModel):
    h: int
    size: str
    usage: str
    w: int


class ClientConfig(BaseModel):
    about: str
    acl: dict[str, dict[str, bool] | None]
    album_categories: OptionalList[str] = Field(alias="albumCategories")
    albums: OptionalList[entity.Album]
    api_uri: str = Field(alias="apiUri")
    app_color: str = Field(alias="appColor")
    app_icon: str = Field(alias="appIcon")
    app_mode: str = Field(alias="appMode")
    app_name: str = Field(alias="appName")
    auth_mode: str = Field(alias="authMode")
    base_uri: str = Field(alias="baseUri")
    cameras: OptionalList[entity.Camera]
    categories: OptionalList[CategoryLabel]
    clip: int
    colors: OptionalList[dict[str, str]]
    content_uri: str = Field(alias="contentUri")
    copyright: str
    count: ClientCounts
    countries: OptionalList[entity.Country]
    css_uri: str = Field(alias="cssUri")
    customer: str
    debug: bool
    demo: bool
    disable: ClientDisable
    download_token: str = Field(alias="downloadToken")
    edition: str
    experimental: bool
    ext: dict[str, Any]
    flags: str
    js_uri: str = Field(alias="jsUri")
    legal_info: str = Field(alias="legalInfo")
    legal_url: str = Field(alias="legalUrl")
    lenses: OptionalList[entity.Lens]
    login_uri: str = Field(alias="loginUri")
    manifest_uri: str = Field(alias="manifestUri")
    map_key: str = Field(alias="mapKey")
    membership: str
    mode: str
    name: str
    password_length: int = Field(alias="passwordLength")
    password_reset_uri: str = Field(alias="passwordResetUri")
    people: OptionalList[entity.Person]
    pos: ClientPosition
    preview_token: str = Field(alias="previewToken")
    public: bool
    readonly: bool
    register_uri: str = Field(alias="registerUri")
    restart: bool
    server: env.Resources
    settings: customize.Settings
    site_author: str = Field(alias="siteAuthor")
    site_caption: str = Field(alias="siteCaption")
    site_description: str = Field(alias="siteDescription")
    site_domain: str = Field(alias="siteDomain")
    site_preview: str = Field(alias="sitePreview")
    site_title: str = Field(alias="siteTitle")
    site_url: str = Field(alias="siteUrl")
    sponsor: bool = Field(alias="sponsor")
    static_uri: str = Field(alias="staticUri")
    test: bool
    thumbs: OptionalList[ThumbSize]
    tier: int
    trace: bool
    upload_nsfw: bool = Field(alias="uploadNSFW")
    users_path: str = Field(alias="usersPath")
    version: str
    video_uri: str = Field(alias="videoUri")
    wallpaper_uri: str = Field(alias="wallpaperUri")
    years: OptionalList[int]
