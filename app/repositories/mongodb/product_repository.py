from app.database.mongodb import db



def get_products_and_categories():
    """
    Obtiene productos y categorías desde MongoDB.
    """

    products = db.products.find()

    categories = db.categories.find()


    return list(products), list(categories)




def get_all_products():
    """
    Obtiene todos los productos.
    """

    products = db.products.find()


    return list(products)




def get_all_categories():
    """
    Obtiene todas las categorías.
    """

    categories = db.categories.find()


    return list(categories)




# ==========================================
# INDICADOR INTEGRADO
# Buscar producto por ID
# ==========================================

def get_product_by_id(product_id):
    """
    Obtiene información del producto
    mediante product_id.
    """

    product = db.products.find_one(
        {
            "product_id": product_id
        }
    )


    return product