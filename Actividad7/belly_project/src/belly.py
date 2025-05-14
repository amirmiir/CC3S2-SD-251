# src/belly.py
# from src.clock import get_current_time

class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    # Ejercicio 2: Modificar funcionamiento para aceptar flotantes
    def comer(self, pepinos):
        """
        pepinos: float or int. Must be >= 0.
        """
        try:
            cantidad = float(pepinos)
        except (TypeError, ValueError):
            raise ValueError(f"Cantidad no válida de pepinos: {pepinos!r}")
        if cantidad < 0:
            raise ValueError(f"No se permiten cantidades negativas: {cantidad}")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False