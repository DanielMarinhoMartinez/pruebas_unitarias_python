import pytest
from biblioteca import Libro, Biblioteca

# 2.1. Pruebas para la clase Libro

# Verificar que los atributos (titulo, autor, año) se inicializan correctamente
def test_inicializacion_libro():
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    
    assert libro.titulo == "Cien años de soledad"
    assert libro.autor == "Gabriel García Márquez"
    assert libro.anio == 1967
    assert libro.prestado == False  # El libro no está prestado por defecto

# Verificar cuando un libro está prestado o cuando está disponible
def test_estado_libro():
    libro = Libro("1984", "George Orwell", 1949)
    
    # El estado debe ser "disponible" cuando no está prestado
    assert str(libro) == "1984 de George Orwell (1949) - disponible"
    
    # Cambiar el estado a prestado
    libro.prestado = True
    
    # El estado debe ser "prestado" cuando está prestado
    assert str(libro) == "1984 de George Orwell (1949) - prestado"


# 2.2. Pruebas para la clase Biblioteca

# Verificar que un libro se agrega correctamente a la biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    
    biblioteca.agregar_libro(libro)
    
    # Verificar que la lista de libros contiene el libro agregado
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0] == libro


# Verificar que un libro se elimina correctamente de la biblioteca
def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(libro)
    
    biblioteca.eliminar_libro("Cien años de soledad")
    
    # Verificar que la lista de libros está vacía después de eliminar el libro
    assert len(biblioteca.libros) == 0


# Verificar que intentar eliminar un libro que no existe no afecte la lista de libros
def test_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    biblioteca.eliminar_libro("Cien años de soledad")  # Intentar eliminar un libro que no existe
    
    # Verificar que el libro sigue en la lista
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0] == libro


# Verificar que un libro existente se puede encontrar
def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.buscar_libro("Cien años de soledad")
    
    assert resultado == libro


# Verificar que la búsqueda de un libro que no existe devuelve None
def test_buscar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.buscar_libro("Cien años de soledad")  # Libro no agregado
    
    assert resultado is None


# Verificar que la lista de libros se retorna correctamente
def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("1984", "George Orwell", 1949)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    
    libros_listados = biblioteca.listar_libros()
    
    assert len(libros_listados) == 2
    assert "1984 de George Orwell (1949) - disponible" in libros_listados
    assert "Cien años de soledad de Gabriel García Márquez (1967) - disponible" in libros_listados


# Verificar que un libro se presta correctamente
def test_prestar_libro():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.prestar_libro("1984")
    
    assert resultado == "Has pedido prestado el libro '1984'."
    assert libro.prestado == True


# Verificar que intentar prestar un libro ya prestado devuelve un mensaje adecuado
def test_prestar_libro_ya_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("1984")  # Prestar el libro una vez
    
    resultado = biblioteca.prestar_libro("1984")  # Intentar prestarlo nuevamente
    
    assert resultado == "El libro '1984' ya está prestado."


# Verificar que intentar prestar un libro que no existe devuelve un mensaje adecuado
def test_prestar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.prestar_libro("Cien años de soledad")  # Libro no agregado
    
    assert resultado == "El libro 'Cien años de soledad' no se encuentra en la biblioteca."


# Verificar que un libro se devuelve correctamente
def test_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("1984")
    
    resultado = biblioteca.devolver_libro("1984")
    
    assert resultado == "Has devuelto el libro '1984'."
    assert libro.prestado == False


# Verificar que intentar devolver un libro no prestado devuelve un mensaje adecuado
def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.devolver_libro("1984")  # Intentar devolver un libro no prestado
    
    assert resultado == "El libro '1984' no estaba prestado."


# Verificar que intentar devolver un libro que no existe devuelve un mensaje adecuado
def test_devolver_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    
    resultado = biblioteca.devolver_libro("Cien años de soledad")  # Libro no agregado
    
    assert resultado == "El libro 'Cien años de soledad' no se encuentra en la biblioteca."
