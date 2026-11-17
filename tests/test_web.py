import unittest

from app import app


class TestWeb(unittest.TestCase):
    def test_inicio_muestra_producto_de_ejemplo(self):
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        for texto in ("Sistema de inventario", "P001", "Teclado", "350"):
            self.assertIn(texto, response.get_data(as_text=True))

    def test_archivos_estaticos_disponibles(self):
        cliente = app.test_client()
        for ruta in ("/static/app.js", "/static/style.css"):
            respuesta = cliente.get(ruta)
            self.assertEqual(respuesta.status_code, 200)
            respuesta.close()


if __name__ == "__main__":
    unittest.main()
