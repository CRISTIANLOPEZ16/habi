from src.db import get_connection, close_connection

class PropertyRepository:
    def get_properties(self, filters):
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT p.id,p.address, p.city, p.price, p.description, p.year, s.name as status FROM property p
                    JOIN (
                        SELECT property_id, MAX(id) AS last_status_id
                        FROM status_history
                        GROUP BY property_id
                    ) AS last_sh ON last_sh.property_id = p.id
                    JOIN status_history sh ON sh.id = last_sh.last_status_id
                    JOIN status s ON sh.status_id = s.id WHERE sh.status_id IN (3, 4, 5)"""
            params = []
            if "year" in filters and filters["year"]:
                query += " AND p.year = %s"
                params.append(filters["year"])
            if "city" in filters and filters["city"]:
                query += " AND p.city = %s"
                params.append(filters["city"])
            # Puedes agregar más filtros según se requiera
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar propiedades: {e}")
            return []
        finally:
            close_connection(conn)