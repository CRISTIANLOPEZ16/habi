from http.server import HTTPServer
from src.controller.query_controller import QueryController
from dotenv import load_dotenv

load_dotenv()
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, QueryController)
    print('Servidor corriendo en http://localhost:8000')
    httpd.serve_forever()

if __name__ == "__main__":
    run()