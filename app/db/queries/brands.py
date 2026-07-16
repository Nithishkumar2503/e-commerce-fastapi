from app.db.connection import get_db_connection


from app.schemas.brands import (
    BrandUpdate,
)


def get_all_brands():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            id,name,slug,description,is_active
            FROM brands ORDER BY created_at DESC
        """
    )

    rows = cur.fetchall()
    print("Print: ", rows)
    cur.close()
    conn.close()

    return rows


def get_brand_by_id(brand_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM brands
        WHERE id=%s
    """,
        (brand_id,),
    )

    rows = cur.fetchone()

    cur.close()
    conn.close()

    return rows


def create_brand(data):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
    INSERT INTO brands (
        name,
        slug,
        description
    )
    VALUES (%s,%s,%s)
    RETURNING *
    """,
        (data.name, data.slug, data.description),
    )


def update_brand(brand_id, data: BrandUpdate):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
    UPDATE brands
        SET
            name=%s,
            slug=%s,
            description=%s,
            updated_at=NOW()
        WHERE id=%s
        RETURNING *
    """,
        (data.name, data.slug, data.description, brand_id),
    )

    brand = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return brand


def delete_brand(brand_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM brands WHERE id=%s
        """,
        (brand_id,),
    )

    conn.commit()

    cur.close()
    conn.close()
