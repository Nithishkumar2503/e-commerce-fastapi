from pydantic import BaseModel
from uuid import UUID


class BrandCreate(BaseModel):
    name: str
    slug: str
    description: str | None = None


class BrandUpdate(BaseModel):
    name: str
    slug: str
    description: str | None = None


class BrandResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    description: str | None = None
    is_active: bool
