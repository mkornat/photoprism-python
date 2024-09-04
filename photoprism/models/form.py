from datetime import datetime

from pydantic import BaseModel, Field

from photoprism.models.entity import Details


class Album(BaseModel):
    caption: str | None = Field(serialization_alias="Caption", default=None)
    category: str | None = Field(serialization_alias="Category", default=None)
    country: str | None = Field(serialization_alias="Country", default=None)
    description: str | None = Field(serialization_alias="Description", default=None)
    favorite: bool | None = Field(serialization_alias="Favorite", default=None)
    filter: str | None = Field(serialization_alias="Filter", default=None)
    location: str | None = Field(serialization_alias="Location", default=None)
    notes: str | None = Field(serialization_alias="Notes", default=None)
    order: str | None = Field(serialization_alias="Order", default=None)
    private: bool | None = Field(serialization_alias="Private", default=None)
    template: str | None = Field(serialization_alias="Template", default=None)
    thumb: str | None = Field(serialization_alias="Thumb", default=None)
    thumb_src: str | None = Field(serialization_alias="ThumbSrc", default=None)
    title: str | None = Field(serialization_alias="Title", default=None)
    type: str | None = Field(serialization_alias="Type", default=None)


class Link(BaseModel):
    password: str | None = Field(serialization_alias="Password", default=None)
    share_slug: str | None = Field(serialization_alias="ShareSlug", default=None)
    link_token: str | None = Field(serialization_alias="LinkToken", default=None)
    link_expires: int | None = Field(serialization_alias="LinkExpires", default=None)
    max_views: int | None = Field(serialization_alias="MaxViews", default=None)
    can_comment: bool | None = Field(serialization_alias="CanComment", default=None)
    can_edit: bool | None = Field(serialization_alias="CanEdit", default=None)


class Selection(BaseModel):
    all: bool | None = None
    files: list[str] | None = None
    photos: list[str] | None = None
    albums: list[str] | None = None
    labels: list[str] | None = None
    places: list[str] | None = None
    subjects: list[str] | None = None


class SearchLabels(BaseModel):
    count: int
    q: str | None = None
    uid: str | None = None
    slug: str | None = None
    name: str | None = None
    all: bool | None = None
    favorite: bool | None = None
    offset: int | None = None
    order: str | None = None


class Label(BaseModel):
    name: str = Field(serialization_alias="Name")
    priority: str = Field(serialization_alias="Priority", default=None)
    uncertainty: str = Field(serialization_alias="Uncertainty", default=None)


class SearchPhotos(BaseModel):
    count: int
    q: str | None = None
    s: str | None = None
    filter: str | None = None
    id: str | None = None
    uid: str | None = None
    type: str | None = None
    path: str | None = None
    folder: str | None = None
    name: str | None = None
    filename: str | None = None
    original: str | None = None
    title: str | None = None
    hash: str | None = None
    primary: bool | None = None
    stack: bool | None = None
    unstacked: bool | None = None
    stackable: bool | None = None
    video: bool | None = None
    vector: bool | None = None
    animated: bool | None = None
    photo: bool | None = None
    raw: bool | None = None
    live: bool | None = None
    scan: str | None = None
    mp: str | None = None
    panorama: bool | None = None
    portrait: bool | None = None
    landscape: bool | None = None
    square: bool | None = None
    error: bool | None = None
    hidden: bool | None = None
    archived: bool | None = None
    public: bool | None = None
    private: bool | None = None
    favorite: str | None = None
    unsorted: bool | None = None
    near: str | None = None
    s2: str | None = None
    olc: str | None = None
    lat: float | None = None
    lng: float | None = None
    alt: str | None = None
    dist: float | None = None
    latlng: str | None = None
    camera: str | None = None
    lens: str | None = None
    iso: str | None = None
    mm: str | None = None
    f: str | None = None
    color: str | None = None
    chroma: int | None = None
    mono: bool | None = None
    diff: int | None = None
    geo: str | None = None
    keywords: str | None = None
    label: str | None = None
    category: str | None = None
    country: str | None = None
    state: str | None = None
    city: str | None = None
    year: str | None = None
    month: str | None = None
    date: str | None = None
    face: str | None = None
    faces: str | None = None
    person: str | None = None
    subjects: str | None = None
    people: str | None = None
    album: str | None = None
    albums: str | None = None
    quality: int | None = None
    review: bool | None = None
    added: datetime | None = None
    updated: datetime | None = None
    edited: datetime | None = None
    taken: datetime | None = None
    before: datetime | None = None
    after: datetime | None = None
    offset: int | None = None
    order: str | None = None
    merged: bool | None = None


class Photo(BaseModel):
    type: str | None = Field(serialization_alias="Type", default=None)
    type_src: str | None = Field(serialization_alias="TypeSrc", default=None)
    taken_at: datetime | None = Field(serialization_alias="TakenAt", default=None)
    taken_at_local: datetime | None = Field(
        serialization_alias="TakenAtLocal", default=None
    )
    taken_src: str | None = Field(serialization_alias="TakenSrc", default=None)
    time_zone: str | None = Field(serialization_alias="TimeZone", default=None)
    year: int | None = Field(serialization_alias="Year", default=None)
    month: int | None = Field(serialization_alias="Month", default=None)
    day: int | None = Field(serialization_alias="Day", default=None)
    title: str | None = Field(serialization_alias="Title", default=None)
    title_src: str | None = Field(serialization_alias="TitleSrc", default=None)
    description: str | None = Field(serialization_alias="Description", default=None)
    description_src: str | None = Field(
        serialization_alias="DescriptionSrc", default=None
    )
    details: Details | None = Field(serialization_alias="Details", default=None)
    stack: int | None = Field(serialization_alias="Stack", default=None)
    favorite: bool | None = Field(serialization_alias="Favorite", default=None)
    private: bool | None = Field(serialization_alias="Private", default=None)
    scan: bool | None = Field(serialization_alias="Scan", default=None)
    panorama: bool | None = Field(serialization_alias="Panorama", default=None)
    altitude: int | None = Field(serialization_alias="Altitude", default=None)
    lat: float | None = Field(serialization_alias="Lat", default=None)
    lng: float | None = Field(serialization_alias="Lng", default=None)
    iso: int | None = Field(serialization_alias="Iso", default=None)
    focal_length: int | None = Field(serialization_alias="FocalLength", default=None)
    f_number: float | None = Field(serialization_alias="FNumber", default=None)
    exposure: str | None = Field(serialization_alias="Exposure", default=None)
    country: str | None = Field(serialization_alias="Country", default=None)
    cell_id: str | None = Field(serialization_alias="CellID", default=None)
    cell_accuracy: str | None = Field(serialization_alias="CellAccuracy", default=None)
    place_id: str | None = Field(serialization_alias="PlaceID", default=None)
    place_src: str | None = Field(serialization_alias="PlaceSrc", default=None)
    camera_id: int | None = Field(serialization_alias="CameraID", default=None)
    camera_src: str | None = Field(serialization_alias="CameraSrc", default=None)
    lend_id: int | None = Field(serialization_alias="LendID", default=None)
    original_name: str | None = Field(serialization_alias="OriginalName", default=None)


class File(BaseModel):
    orientation: int = Field(serialization_alias="Orientation")


class SearchFaces(BaseModel):
    count: int
    offset: int | None = None
    order: str | None = None
    q: str | None = None
    uid: str | None = None
    subject: str | None = None
    unknown: str | None = None
    hidden: str | None = None
    markers: bool | None = None


class Face(BaseModel):
    hidden: bool | None = Field(serialization_alias="Hidden", default=None)
    subj_uid: str | None = Field(serialization_alias="SubjUID", default=None)


class IndexOptions(BaseModel):
    path: str | None = None
    rescan: bool | None = None
    cleanup: bool | None = None
