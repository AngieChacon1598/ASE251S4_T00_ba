from collections import defaultdict


from app.repositories.mongodb import product_repository as product_repo

from app.repositories.sqlserver.sales_repository import SalesRepository

from app.schemas.analytics_schema import IndicatorResponse



# Instancia del Repository SQL Server
sales_repository = SalesRepository()



# ==========================================
# INDICADOR SIMPLE
# Productos por categoría
# Fuente: MongoDB
# ==========================================

def count_products_by_category():

    """
    Genera el indicador:
    Cantidad de productos por categoría
    """


    # 1. Obtener datos desde MongoDB

    products, categories = product_repo.get_products_and_categories()



    # 2. Contador por categoría

    counts = defaultdict(int)



    # 3. Crear mapa de categorías

    cat_map = {

        c["category_id"]: c["name"]

        for c in categories

    }



    # 4. Agrupar productos por categoría

    for product in products:


        category_id = product.get("category_id")



        if category_id in cat_map:


            category_name = cat_map[category_id]


            counts[category_name] += 1




    # 5. Convertir datos al formato gráfico

    data = []


    for category, total in counts.items():

        data.append({

            "label": category,

            "value": total

        })




    # 6. Retornar indicador estándar

    return IndicatorResponse(

        indicator="products_category",

        title="Productos por categoría",

        chart_type="bar",

        data=data,

        sources=[

            "MongoDB"

        ]

    )





# ==========================================
# INDICADOR INTEGRADO
# Producto más vendido del mes
#
# Fuente:
# SQL Server + MongoDB
# ==========================================

def get_top_product_month():

    """
    Obtiene el producto más vendido
    integrando información de SQL Server
    y MongoDB.
    """



    # 1. Obtener ventas desde SQL Server

    sales_data = sales_repository.get_top_product()



    if not sales_data:

        return None





    # 2. Obtener información del producto desde MongoDB

    product = product_repo.get_product_by_id(

        sales_data["product_id"]

    )



    if not product:

        return None





    # 3. Integrar ambas fuentes

    data = {


        "product_id":

        sales_data["product_id"],



        "product":

        product.get("name"),



        "category":

        product.get("category"),



        "quantity":

        sales_data["quantity"]

    }




    # 4. Retornar indicador estándar

    return IndicatorResponse(

        indicator="top_product_month",

        title="Producto más vendido del mes",

        chart_type="card",

        data=data,

        sources=[

            "SQL Server",

            "MongoDB"

        ]

    )