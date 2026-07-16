from app.db.queries.brands import (
    get_all_brands,get_brand_by_id,
    create_brand,
    update_brand as update_brand_query,
    delete_brand as delete_brand_query  
)

def list_brands():
    return get_all_brands()

def get_brand(id):
    return get_brand_by_id(id)

def add_brand(data):
    return create_brand(data)

def edit_brand(id,data):
    return update_brand_query(id,data)

def delete_brand(id):
    return delete_brand_query(id) 
