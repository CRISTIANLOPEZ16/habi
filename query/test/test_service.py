import pytest
import json
from src.service.query_service import consultar_propiedades
from src.controller.query_controller import QueryController

# Dummy repository for isolated service tests
class DummyRepo:
    def get_properties(self, filters):
        if filters.get("city") == "Bogotá" and filters.get("year") == 2020:
            return [
                    {
                        "address": "calle 95 # 78 - 49",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "hermoso acabado, listo para estrenar",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 95 # 78 - 123",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "hermoso acabado, listo para estrenar",
                        "year": 2020,
                        "status": "pre_venta"
                    }
            ]
        elif filters.get("city") == "Medellín":
            return [
                    {
                        "address": "calle 23 #45-67",
                        "city": "medellin",
                        "price": 210000000,
                        "description": "",
                        "year": 2002,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "vendido"
                    },
                    {
                        "address": "calle 23 #45-67r",
                        "city": "medellin",
                        "price": 210000000,
                        "description": "",
                        "year": 2002,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90e",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21s",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "pre_venta"
                    }
            ]
        else:
            return [
                    {
                        "address": "carrera 100 #15-90",
                        "city": "bogota",
                        "price": 350000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": "en_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "en_venta"
                    },
                    {
                        "address": "Malabar entrada 2",
                        "city": "pereira",
                        "price": 350000000,
                        "description": "Casa campestre con hermosos paisajes",
                        "year": 2021,
                        "status": "en_venta"
                    },
                    {
                        "address": "Maracay casa 24",
                        "city": "pereira",
                        "price": 450000000,
                        "description": "Casa campestre con sala de lujo tecnologica",
                        "year": 2020,
                        "status": "en_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21e",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": "en_venta"
                    },
                    {
                        "address": "carrera 100 #15-90e",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "en_venta"
                    },
                    {
                        "address": "Entrada 8 via cerritos",
                        "city": "pereira",
                        "price": 250000000,
                        "description": "Full casa amoblada",
                        "year": 2020,
                        "status": "en_venta"
                    },
                    {
                        "address": "Cll 1A #11B",
                        "city": "bucaramanga",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2021,
                        "status": "en_venta"
                    },
                    {
                        "address": "calle 23 #45-67",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "Hermoso apartamento en el centro de la ciudad",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "bogota",
                        "price": 350000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67",
                        "city": "medellin",
                        "price": 210000000,
                        "description": "",
                        "year": 2002,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "medellin",
                        "price": 325000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90",
                        "city": "barranquilla",
                        "price": 35000000,
                        "description": "null",
                        "year": 2015,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 95 # 78 - 49",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "hermoso acabado, listo para estrenar",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Entrada 3 via cerritos",
                        "city": "pereira",
                        "price": 250000000,
                        "description": "Full casa amoblada",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Entrada 2 via cerritos",
                        "city": "pereira",
                        "price": 270000000,
                        "description": "Casa campestre con lago",
                        "year": 2021,
                        "status": "pre_venta"
                    },
                    {
                        "address": "M1 C5 Panorama",
                        "city": "dosquebradas",
                        "price": 290000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2017,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Bloque 5 C26 Umbras",
                        "city": "belen de umbria",
                        "price": 120000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67q",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "Hermoso apartamento en el centro de la ciudad",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67q",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "Hermoso apartamento en el centro de la ciudad",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67q",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "Hermoso apartamento en el centro de la ciudad",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90w",
                        "city": "bogota",
                        "price": 350000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90w",
                        "city": "bogota",
                        "price": 350000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 100 #15-90w",
                        "city": "bogota",
                        "price": 350000000,
                        "description": "Amplio apartamento en conjunto cerrado",
                        "year": 2011,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67r",
                        "city": "medellin",
                        "price": 210000000,
                        "description": "",
                        "year": 2002,
                        "status": "pre_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21s",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "carrera 22 #34-96v",
                        "city": "manizales",
                        "price": 39483059,
                        "description": "null",
                        "year": 1800,
                        "status": "pre_venta"
                    },
                    {
                        "address": "",
                        "city": "",
                        "price": 0,
                        "description": "null",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "",
                        "city": "",
                        "price": 0,
                        "description": "null",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "",
                        "city": "",
                        "price": 0,
                        "description": "null",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 95 # 78 - 123",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "hermoso acabado, listo para estrenar",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 18 k 43 - 12e",
                        "city": "cali",
                        "price": 125000000,
                        "description": "null",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "Cll 1A #11B-20v",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2016,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Malabar entrada 2v",
                        "city": "pereira",
                        "price": 350000000,
                        "description": "Casa campestre con hermosos paisajes",
                        "year": 2021,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Maracay casa 24c",
                        "city": "pereira",
                        "price": 450000000,
                        "description": "Casa campestre con sala de lujo tecnologica",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Entrada 4 via cerritos",
                        "city": "pereira",
                        "price": 250000000,
                        "description": "Full casa amoblada",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Entrada 5 via cerritos",
                        "city": "pereira",
                        "price": 270000000,
                        "description": "Casa campestre con lago",
                        "year": 2021,
                        "status": "pre_venta"
                    },
                    {
                        "address": "M8 C6 Panorama",
                        "city": "dosquebradas",
                        "price": 290000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2017,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Bloque 5 C67 Umbras",
                        "city": "belen de umbria",
                        "price": 120000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Cll 1A #11B-234",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2019,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Maracay casa 567c",
                        "city": "pereira",
                        "price": 450000000,
                        "description": "Casa campestre con sala de lujo tecnologica",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Entrada 9 via cerritos",
                        "city": "pereira",
                        "price": 270000000,
                        "description": "Casa campestre con lago",
                        "year": 2021,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Bloque 53 C674 Umbras",
                        "city": "belen de umbria",
                        "price": 120000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 18 k 43",
                        "city": "cali",
                        "price": 125000000,
                        "description": "null",
                        "year": "null",
                        "status": "pre_venta"
                    },
                    {
                        "address": "Cll 1A #20b",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "casa 24c",
                        "city": "pereira",
                        "price": 450000000,
                        "description": "Casa campestre con sala de lujo tecnologica",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "via cerritos",
                        "city": "pereira",
                        "price": 250000000,
                        "description": "Full casa amoblada",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "5 via cerritos",
                        "city": "pereira",
                        "price": 270000000,
                        "description": "Casa campestre con lago",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "C67 Umbras",
                        "city": "belen de umbria",
                        "price": 120000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2020,
                        "status": "pre_venta"
                    },
                    {
                        "address": "Cra 11 A No 18 E 11",
                        "city": "la virginia",
                        "price": 90000000,
                        "description": "Hermosa casa con 3 piezas",
                        "year": 2022,
                        "status": "pre_venta"
                    },
                    {
                        "address": "calle 23 #45-67",
                        "city": "bogota",
                        "price": 120000000,
                        "description": "Hermoso apartamento en el centro de la ciudad",
                        "year": 2000,
                        "status": "pre_venta"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": "vendido"
                    },
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "medellin",
                        "price": 270000000,
                        "description": "",
                        "year": "null",
                        "status": "vendido"
                    },
                    {
                        "address": "Cll 1A #11B-20",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2019,
                        "status": "vendido"
                    },
                    {
                        "address": "carrera 100 #15-90x",
                        "city": "barranquilla",
                        "price": 35000000,
                        "description": "null",
                        "year": 2015,
                        "status": "vendido"
                    },
                    {
                        "address": "",
                        "city": "",
                        "price": 0,
                        "description": "null",
                        "year": "null",
                        "status": "vendido"
                    },
                    {
                        "address": "",
                        "city": "",
                        "price": 0,
                        "description": "null",
                        "year": "null",
                        "status": "vendido"
                    },
                    {
                        "address": "Cll 1A #11B-20b",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2019,
                        "status": "vendido"
                    },
                    {
                        "address": "Cll 1A #11B-123",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2016,
                        "status": "vendido"
                    },
                    {
                        "address": "Malabar entrada 345",
                        "city": "pereira",
                        "price": 350000000,
                        "description": "Casa campestre con hermosos paisajes",
                        "year": 2021,
                        "status": "vendido"
                    },
                    {
                        "address": "M8 C634 Panorama",
                        "city": "dosquebradas",
                        "price": 290000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2017,
                        "status": "vendido"
                    },
                    {
                        "address": "Cll 1A #11B",
                        "city": "pereira",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2020,
                        "status": "vendido"
                    },
                    {
                        "address": "Malabar 2v",
                        "city": "pereira",
                        "price": 350000000,
                        "description": "Casa campestre con hermosos paisajes",
                        "year": 2020,
                        "status": "vendido"
                    },
                    {
                        "address": "C6 Panorama",
                        "city": "dosquebradas",
                        "price": 290000000,
                        "description": "Casa con entrada al centro comercial",
                        "year": 2020,
                        "status": "vendido"
                    }
                ]

def test_consulta_sin_filtros():
    result = consultar_propiedades({}, repo=DummyRepo())
    # Realizamos una verficacion que ningún resultado venga con un estado diferente a "en_venta", "pre_venta" o "vendido"
    assert len(result) > 0
    for prop in result:
        assert prop["status"] in ["en_venta", "pre_venta", "vendido"]

def test_consulta_con_filtros_city_year():
    result = consultar_propiedades({"city": "Bogotá", "year": 2020}, repo=DummyRepo())
    assert len(result) > 0
    assert all(prop["city"].lower() == "bogota" for prop in result)

def test_consulta_con_filtros_city():
    result = consultar_propiedades({"city": "Medellín"}, repo=DummyRepo())
    assert len(result) > 0
    assert all(prop["city"].lower() == "medellin" for prop in result)

# -- Integration test for the POST endpoint --

from http.server import HTTPServer
import threading
import requests

class DummyHandler(QueryController):
    def do_POST(self):
        # Patch the service to use the DummyRepo for endpoint-level test
        from src.service.query_service import consultar_propiedades as original_service
        def fake_service(filters, repo=None):
            return original_service(filters, repo=DummyRepo())
        self.server.service_func = fake_service
        # Patch locally for this handler instance
        self.consultar_propiedades = fake_service
        super().do_POST()

def run_server_in_thread():
    httpd = HTTPServer(('localhost', 8001), DummyHandler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    return httpd, thread

def test_post_endpoint():
    httpd, thread = run_server_in_thread()
    import time
    import dotenv
    dotenv.load_dotenv()  # Load environment variables if needed
    time.sleep(0.5)  # Allow server to start
    url = "http://localhost:8001/propiedades"
    filtros = {"city": "Bogotá", "year": 2020}
    resp = requests.post(url, json=filtros)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(prop["city"].lower() == "bogota" for prop in data)
    httpd.shutdown()
    thread.join(1)