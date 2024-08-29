from pydantic import BaseModel, Field


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
