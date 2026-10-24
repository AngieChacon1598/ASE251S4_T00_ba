from flask import Blueprint, jsonify


from app.services.analytics import product_service



products_bp = Blueprint(

    "products",

    __name__

)



# ==========================================
# Indicador MongoDB
# Productos por categoría
# ==========================================

@products_bp.route(

    "/analytics/products-by-category",

    methods=["GET"]

)

def products_by_category():


    result = product_service.count_products_by_category()



    return jsonify(

        result.__dict__

    )


# ==========================================
# Indicador Integrado
# Producto más vendido del mes
# Fuente:
# SQL Server + MongoDB
# ==========================================

@products_bp.route(

    "/analytics/top-product",

    methods=["GET"]

)

def top_product_month():


    result = product_service.get_top_product_month()



    if result is None:


        return jsonify({

            "message":

            "No se encontró información"

        }),404




    return jsonify(

        result.__dict__

    )