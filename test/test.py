import unittest
from modelo.helicoptero import Helicoptero

class TestHelicoptero(unittest.TestCase):

    def setUp(self):
        self.heli = Helicoptero("Bell", "206")

    def test_encender_motor(self):
        self.assertEqual(self.heli.encender_motor(), "Motor encendido correctamente.")
        self.assertTrue(self.heli.motor_encendido) 

    def test_apagar_motor_en_tierra(self):
        self.heli.encender_motor()
        self.assertEqual(self.heli.apagar_motor(), "Motor apagado correctamente.")
        self.assertFalse(self.heli.motor_encendido) 

    def test_no_apagar_motor_en_vuelo(self):
        self.heli.encender_motor()
        self.heli.despegar()
        resultado = self.heli.apagar_motor()
        self.assertEqual(resultado, "No es posible apagar el motor mientras el helicoptero esta en vuelo.")

    def test_despegar_sin_motor_encendido(self):
        self.assertEqual(self.heli.despegar(), "Debe encender el motor antes de despegar.")

    def test_despegar_correctamente(self):
        self.heli.encender_motor()
        resultado = self.heli.despegar()
        self.assertEqual(resultado, "Despegue realizado con exito.")
        self.assertEqual(self.heli.altitud, 100) 

    def test_volar_sin_despegar(self):
        self.heli.encender_motor()
        self.assertEqual(self.heli.volar(), "Debe despegar antes de volar.")

    def test_volar_correctamente(self):
        self.heli.encender_motor()
        self.heli.despegar()
        resultado = self.heli.volar()
        self.assertIn("Volando", resultado)
        self.assertEqual(self.heli.velocidad, 150) 

    def test_aterrizar_correctamente(self):
        self.heli.encender_motor()
        self.heli.despegar()
        resultado = self.heli.aterrizar()
        self.assertEqual(resultado, "Aterrizaje realizado con exito.")
        self.assertEqual(self.heli.altitud, 0) 
        self.assertEqual(self.heli.velocidad, 0) 

if __name__ == "__main__":
    unittest.main()