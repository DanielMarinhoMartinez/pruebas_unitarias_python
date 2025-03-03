import pytest
from cine import Pelicula


@pytest.mark.parametrize("nombre, asientos_disponibles, precio, cantidad, expected_resultado, expected_asientos_disponibles", [
    ("Bridget Jones: Loca por él", 100, 8, 5, "Has comprado 5 entradas para Bridget Jones: Loca por él. Total: $40", 95),
    ("Captain America: Brave New World", 50, 10, 10, "Has comprado 10 entradas para Captain America: Brave New World. Total: $100", 40),
    ("Paddington in Peru", 75, 9, 0, "Has comprado 0 entradas para Paddington in Peru. Total: $0", 75),
    ("Bridget Jones: Loca por él", 100, 8, 150, "No hay suficientes asientos disponibles. Solo quedan 100 asientos.", 100),
])

def test_venta_entradas(nombre, asientos_disponibles, precio, cantidad, expected_resultado, expected_asientos_disponibles):

    # Crear una nueva instancia de Pelicula 
    pelicula = Pelicula(nombre, asientos_disponibles, precio)

    # Ejecutar la función
    resultado = pelicula.vender_entradas(cantidad)

    # Verificar que el mensaje es correcto
    assert resultado == expected_resultado

    # Verificar que los asientos disponibles son correctos
    assert pelicula.asientos_disponibles == expected_asientos_disponibles 
