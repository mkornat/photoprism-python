from datetime import datetime, timedelta

from pydantic import BaseModel, Field

from photoprism.models import entity


class Album(BaseModel):
    caption: str = Field("", alias="Caption")
    category: str = Field("", alias="Category")
    country: str = Field("", alias="Country")
    created_at: datetime = Field("", alias="CreatedAt")
    day: int = Field(alias="Day")
    deleted_at: datetime | None = Field(None, alias="DeletedAt")
    description: str = Field("", alias="Description")
    favorite: bool = Field(alias="Favorite")
    filter: str = Field("", alias="Filter")
    link_count: int = Field(alias="LinkCount")
    location: str = Field("", alias="Location")
    month: int = Field(alias="Month")
    notes: str = Field("", alias="Notes")
    order: str = Field("", alias="Order")
    parent_uid: str = Field("", alias="ParentUID")
    path: str = Field("", alias="Path")
    photo_count: int = Field("", alias="PhotoCount")
    private: bool = Field(alias="Private")
    slug: str = Field("", alias="Slug")
    state: str = Field("", alias="State")
    template: str = Field("", alias="Template")
    thumb: str = Field("", alias="Thumb")
    thumb_src: str = Field("", alias="ThumbSrc")
    title: str = Field("", alias="Title")
    type: str = Field("", alias="Type")
    uid: str = Field("", alias="UID")
    updated_at: datetime = Field(alias="UpdatedAt")
    year: int = Field(alias="Year")


class Label(BaseModel):
    id: int = Field(alias="ID")
    uid: str = Field("", alias="UID")
    thumb: str = Field("", alias="Thumb")
    thumb_src: str = Field("", alias="ThumbSrc")
    slug: str = Field("", alias="Slug")
    custom_slug: str = Field("", alias="CustomSlug")
    name: str = Field("", alias="Name")
    priority: int = Field(alias="Priority")
    favorite: bool = Field(alias="Favorite")
    description: str = Field("", alias="Description")
    notes: str = Field("", alias="Notes")
    photo_count: int = Field(alias="PhotoCount")
    created_at: datetime = Field("", alias="CreatedAt")
    updated_at: datetime = Field("", alias="UpdatedAt")
    deleted_at: datetime | None = Field(None, alias="DeletedAt")


class Photo(BaseModel):
    id: str = Field("", alias="ID")
    document_id: str = Field("", alias="DocumentID")
    uid: str = Field("", alias="UID")
    type: str = Field("", alias="Type")
    type_src: str = Field("", alias="TypeSrc")
    taken_at: datetime = Field(alias="TakenAt")
    taken_at_local: datetime = Field(alias="TakenAtLocal")
    taken_src: str = Field("", alias="TakenSrc")
    time_zone: str = Field("", alias="TimeZone")
    path: str = Field("", alias="Path")
    name: str = Field("", alias="Name")
    original_name: str = Field("", alias="OriginalName")
    title: str = Field("", alias="Title")
    description: str = Field("", alias="Description")
    year: int = Field(alias="Year")
    month: int = Field(alias="Month")
    day: int = Field(alias="Day")
    country: str = Field("", alias="Country")
    stack: int = Field(alias="Stack")
    favorite: bool = Field(alias="Favorite")
    iso: int = Field(alias="Iso")
    focal_length: int = Field(alias="FocalLength")
    f_number: float = Field(alias="FNumber")
    exposure: str = Field("", alias="Exposure")
    faces: int | None = Field(None, alias="Faces")
    quality: int = Field(alias="Quality")
    resolution: int = Field(alias="Resolution")
    duration: timedelta | None = Field(None, alias="Duration")
    color: int = Field(alias="Color")
    scan: bool = Field(alias="Scan")
    panorama: bool = Field(alias="Panorama")
    camera_id: int = Field(alias="CameraID")
    camera_src: str = Field("", alias="CameraSrc")
    camera_serial: str = Field("", alias="CameraSerial")
    camera_make: str = Field("", alias="CameraMake")
    camera_model: str = Field("", alias="CameraModel")
    lens_id: int = Field(alias="LensID")
    lens_make: str = Field("", alias="LensMake")
    lens_model: str = Field("", alias="LensModel")
    altitude: int | None = Field(None, alias="Altitude")
    lat: float = Field(alias="Lat")
    lng: float = Field(alias="Lng")
    cell_id: str = Field("", alias="CellID")
    cell_accuracy: int | None = Field(None, alias="CellAccuracy")
    place_id: str = Field("", alias="PlaceID")
    place_src: str = Field("", alias="PlaceSrc")
    place_label: str = Field("", alias="PlaceLabel")
    place_city: str = Field("", alias="PlaceCity")
    place_state: str = Field("", alias="PlaceState")
    place_country: str = Field("", alias="PlaceCountry")
    instance_id: str = Field("", alias="InstanceID")
    file_uid: str = Field("", alias="FileUID")
    file_root: str = Field("", alias="FileRoot")
    file_name: str = Field("", alias="FileName")
    hash: str = Field("", alias="Hash")
    width: int = Field(alias="Width")
    height: int = Field(alias="Height")
    portrait: bool = Field(alias="Portrait")
    merged: bool = Field(alias="Merged")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    edited_at: datetime = Field(alias="EditedAt")
    checked_at: datetime = Field(alias="CheckedAt")
    deleted_at: datetime | None = Field(None, alias="DeletedAt")
    files: list[entity.File] | None = Field(alias="Files", default=None)


class Thumb(BaseModel):
    W: int | None = None
    H: int | None = None
    src: str | None = None


class PublicThumbs(BaseModel):
    fit_720: Thumb
    fit_1280: Thumb
    fit_1920: Thumb
    fit_2560: Thumb
    fit_4096: Thumb
    fit_7680: Thumb


class Result(BaseModel):
    uid: str = Field(alias="UID")
    title: str = Field(alias="Title")
    taken_at_local: datetime = Field(alias="TakenAtLocal")
    description: str = Field(alias="Description")
    favorite: bool = Field(alias="Favorite")
    playable: bool = Field(alias="Playable")
    download_url: str = Field(alias="DownloadUrl")
    width: int = Field(alias="Width")
    height: int = Field(alias="Height")
    thumbs: PublicThumbs = Field(alias="Thumbs")


class Face(BaseModel):
    id: str = Field(alias="ID")
    src: str = Field(alias="Src")
    hidden: bool = Field(alias="Hidden")
    face_dist: float | None = Field(None, alias="FaceDist")
    subj_uid: str = Field(alias="SubjUID")
    subj_src: str | None = Field(None, alias="SubjSrc")
    file_uid: str | None = Field(None, alias="FileUID")
    marker_uid: str | None = Field(None, alias="MarkerUID")
    samples: int = Field(alias="Samples")
    sample_radius: float = Field(alias="SampleRadius")
    collisions: int = Field(alias="Collisions")
    collision_radius: float = Field(alias="CollisionRadius")
    name: str = Field(alias="Name")
    size: int | None = Field(None, alias="Size")
    score: int | None = Field(None, alias="Score")
    review: bool = Field(alias="Review")
    invalid: bool = Field(alias="Invalid")
    thumb: str = Field(alias="Thumb")
    matched_at: datetime = Field(alias="MatchedAt")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
