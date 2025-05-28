from src.model.query_repository import PropertyRepository

def consultar_propiedades(filters, repo=None):
    """
    Consulta propiedades usando filtros.
    :param filters: dict con filtros, e.g. {"year":2020, "city":"Bogotá"}
    :param repo: Inyección de dependencia para pruebas
    :return: lista de propiedades
    """
    if repo is None:
        repo = PropertyRepository()
    return repo.get_properties(filters)