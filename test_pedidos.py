import unittest
from pedidos import procesar_pedido, procesar_presupuesto

SOCIO = {"socio": True}
NO_SOCIO = {"socio": False}


def item(tipo, precio, cantidad):
    return {"tipo": tipo, "precio": precio, "cantidad": cantidad}


class TestProcesarPedido(unittest.TestCase):
    def test_pedido_nulo(self):
        self.assertEqual(procesar_pedido(None, SOCIO), 0)

    def test_pedido_sin_items(self):
        self.assertEqual(procesar_pedido({"items": []}, SOCIO), 0)

    def test_electronica_socio(self):
        # arrange
        pedido = {"items": [item("electronica", 1000, 2)]}
        # act
        resultado = procesar_pedido(pedido, SOCIO)
        # assert
        self.assertAlmostEqual(resultado, 1800)

    def test_ropa_no_socio(self):
        pedido = {"items": [item("ropa", 500, 3)]}
        self.assertAlmostEqual(procesar_pedido(pedido, NO_SOCIO), 1500)

    def test_ropa_socio(self):
        pedido = {"items": [item("ropa", 500, 3)]}
        self.assertAlmostEqual(procesar_pedido(pedido, SOCIO), 1200)

    def test_alimento_socio(self):
        pedido = {"items": [item("alimento", 100, 10)]}
        self.assertAlmostEqual(procesar_pedido(pedido, SOCIO), 950)

    def test_tipo_desconocido_no_suma(self):
        pedido = {"items": [item("juguete", 100, 1)]}
        self.assertEqual(procesar_pedido(pedido, SOCIO), 0)

    def test_bonificacion_total_mayor_a_10000(self):
        pedido = {"items": [item("electronica", 6000, 2)]}
        self.assertAlmostEqual(procesar_pedido(pedido, NO_SOCIO), 11500)


class TestProcesarPresupuesto(unittest.TestCase):
    def test_presupuesto_sin_bonificacion(self):
        pedido = {"items": [item("electronica", 6000, 2)]}
        self.assertAlmostEqual(procesar_presupuesto(pedido, NO_SOCIO), 12000)

    def test_presupuesto_mixto_socio(self):
        pedido = {
            "items": [
                item("electronica", 1000, 1),
                item("ropa", 1000, 1),
                item("alimento", 1000, 1),
            ]
        }
        self.assertAlmostEqual(procesar_presupuesto(pedido, SOCIO), 2650)

    def test_presupuesto_nulo(self):
        self.assertEqual(procesar_presupuesto(None, NO_SOCIO), 0)


if __name__ == "__main__":
    unittest.main()
