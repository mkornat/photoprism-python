from datetime import datetime

from pydantic import BaseModel, Field


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