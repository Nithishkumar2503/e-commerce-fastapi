from uuid import UUID
from fastapi import APIRouter

from app.schemas.brands import (
    BrandCreate,
    BrandUpdate,
)
from app.services.brands import (
    list_brands,
    get_brand,
    add_brand,
    edit_brand,
    delete_brand,
)

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("/")
def get_brands():
    return list_brands()


@router.get("/{brand_id}")
def get_single_brand(brand_id: UUID):
    return get_brand(brand_id)


@router.post("/")
def create_new_brand(data: BrandCreate):
    return add_brand(data)


@router.put("/{brand_id}")
def update_single_brand(brand_id: UUID, data: BrandUpdate):
    return edit_brand(brand_id, data)


@router.delete("/{brand_id}")
def delete_single_brand(brand_id: UUID):
    return delete_brand(brand_id)
