from datetime import datetime

from pydantic import BaseModel, Field


class Album(BaseModel):
    caption: str = Field("", alias="Caption")
    category: str = Field("", alias="Category")
    country: str = Field("", alias="Country")
    created_at: datetime = Field(alias="CreatedAt")
    created_by: str = Field("", alias="CreatedBy")
    day: int = Field(alias="Day")
    deleted_at: datetime | None = Field(alias="DeletedAt")
    description: str = Field("", alias="Description")
    favorite: bool = Field(alias="Favorite")
    filter: str = Field("", alias="Filter")
    id: int = Field(alias="ID")
    location: str = Field("", alias="Location")
    month: int = Field(alias="Month")
    notes: str = Field("", alias="Notes")
    order: str = Field("", alias="Order")
    parent_uid: str = Field("", alias="ParentUID")
    path: str = Field("", alias="Path")
    private: bool = Field(alias="Private")
    published_at: datetime | None = Field(None, alias="PublishedAt")
    slug: str = Field("", alias="Slug")
    state: str = Field("", alias="State")
    template: str = Field("", alias="Template")
    thumb: str = Field("", alias="Thumb")
    thumb_src: str = Field("", alias="ThumbSrc")
    title: str = Field("", alias="Title")
    type: str = Field("", alias="Type")
    uid: str = Field("", alias="UID")
    updated_at: datetime = Field("", alias="UpdatedAt")
    year: int = Field(alias="Year")


class Camera(BaseModel):
    description: str = Field(alias="Description")
    id: int = Field(alias="ID")
    make: str = Field(alias="Make")
    model: str = Field(alias="Model")
    name: str = Field(alias="Name")
    slug: str = Field(alias="Slug")
    type: str = Field(alias="Type")


class Country(BaseModel):
    description: str = Field(alias="Description")
    id: str = Field(alias="ID")
    name: str = Field(alias="Name")
    notes: str = Field(alias="Notes")
    slug: str = Field(alias="Slug")


class Lens(BaseModel):
    description: str = Field(alias="Description")
    id: int = Field(alias="ID")
    make: str = Field(alias="Make")
    model: str = Field(alias="Model")
    name: str = Field(alias="Name")
    notes: str = Field(alias="Notes")
    slug: str = Field(alias="Slug")
    type: str = Field(alias="Type")


class Person(BaseModel):
    alias: str = Field(alias="Alias")
    favorite: bool = Field(alias="Favorite")
    hidden: bool = Field(alias="Hidden")
    name: str = Field(alias="Name")
    uid: str = Field(alias="UID")


class Link(BaseModel):
    uid: str = Field(alias="UID")
    share_uid: str = Field(alias="ShareUID")
    slug: str = Field(alias="Slug")
    token: str = Field(alias="Token")
    expires: int = Field(alias="Expires")
    views: int = Field(alias="Views")
    max_views: int = Field(alias="MaxViews")
    verify_password: bool = Field(alias="VerifyPassword")
    comment: str = Field("", alias="Comment")
    perm: int | None = Field(None, alias="Perm")
    created_by: str = Field(alias="CreatedBy")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")


class Label(BaseModel):
    id: int = Field(alias="ID")
    uid: str = Field(alias="UID")
    slug: str = Field(alias="Slug")
    custom_slug: str = Field(alias="CustomSlug")
    name: str = Field(alias="Name")
    priority: int = Field(alias="Priority")
    favorite: bool = Field(alias="Favorite")
    description: str = Field(alias="Description")
    notes: str = Field(alias="Notes")
    photo_count: int = Field(alias="PhotoCount")
    thumb: str = Field(alias="Thumb")
    thumb_src: str = Field(alias="ThumbSrc")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    published_at: datetime = Field(alias="PublishedAt")
    deleted_at: datetime = Field(alias="DeletedAt")
