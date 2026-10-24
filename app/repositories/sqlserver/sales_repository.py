from app.database.sqlserver import get_sqlserver_connection


class SalesRepository:


    # ==========================================
    # INDICADOR SIMPLE
    # Total de ventas
    # ==========================================

    def get_total_sales(self):

        connection = get_sqlserver_connection()

        cursor = connection.cursor()


        query = """
        SELECT 
            SUM(total_amount)
        FROM sales
        """


        cursor.execute(query)


        result = cursor.fetchone()


        connection.close()


        return result[0]



    # ==========================================
    # INDICADOR INTEGRADO
    # Producto más vendido
    # ==========================================

    def get_top_product(self):

        connection = get_sqlserver_connection()

        cursor = connection.cursor()


        query = """

        SELECT TOP 1

            product_id,

            SUM(quantity) AS total_quantity


        FROM sales_detail


        GROUP BY product_id


        ORDER BY total_quantity DESC

        """


        cursor.execute(query)


        result = cursor.fetchone()


        connection.close()



        if result:

            return {

                "product_id": result[0],

                "quantity": result[1]

            }


        return None