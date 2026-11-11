import io
import unittest
from contextlib import redirect_stdout

from src.producto import Producto


class TestProducto(unittest.TestCase):
    """Casos de prueba CP01 a CP07 para la funcionalidad Producto."""

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def _salida(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.producto.mostrar_informacion()
        return buffer.getvalue()

    def test_cp01_crear_producto(self):
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.existencia, 10)

    def test_cp02_mostrar_codigo(self):
        self.assertIn("Código: P001", self._salida())

    def test_cp03_mostrar_nombre(self):
        self.assertIn("Nombre: Teclado", self._salida())

    def test_cp04_mostrar_precio(self):
        self.assertIn("Precio: 350", self._salida())

    def test_cp05_mostrar_existencia(self):
        self.assertIn("Existencia: 10", self._salida())

    def test_cp06_mostrar_informacion_completa(self):
        salida = self._salida()
        for linea in ("Código: P001", "Nombre: Teclado", "Precio: 350", "Existencia: 10"):
            self.assertIn(linea, salida)

    def test_cp07_crear_segundo_producto(self):
        segundo = Producto("P002", "Mouse", 180, 5)
        self.assertEqual(segundo.codigo, "P002")
        self.assertEqual(segundo.nombre, "Mouse")
        self.assertEqual(segundo.precio, 180)
        self.assertEqual(segundo.existencia, 5)
        self.assertNotEqual(segundo.codigo, self.producto.codigo)
        self.assertNotEqual(segundo.nombre, self.producto.nombre)


if __name__ == "__main__":
    unittest.main()
