# tests/test_clasificador.py
import pytest
from src.clasificador import clasificar_nota

# --- CASOS NORMALES (N) ---
def test_clasificar_nota_suspenso_normal():
    # Arrange
    nota = 2.5
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == "Suspenso"

def test_clasificar_nota_notable_normal():
    # Arrange
    nota = 8.0
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == "Notable"


# --- CASOS LÍMITE (L) ---
@pytest.mark.parametrize("nota, esperado", [
    (0, "Suspenso"),       # Límite inferior absoluto
    (4.99, "Suspenso"),    # Justo antes del aprobado
    (5, "Aprobado"),       # Inicio aprobado
    (6.9, "Aprobado"),     # Fin aprobado
    (7, "Notable"),        # Inicio notable
    (9, "Sobresaliente"),  # Inicio sobresaliente
    (10, "Sobresaliente")  # Límite superior absoluto
])
def test_clasificar_nota_limites(nota, esperado):
    # Arrange & Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


# --- CASOS DE ERROR (E) ---
def test_clasificar_nota_error_negativa():
    # Arrange
    nota_invalida = -1
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        clasificar_nota(nota_invalida)
    assert "fuera del rango" in str(excinfo.value)

def test_clasificar_nota_error_superior_diez():
    # Arrange
    nota_invalida = 10.1
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        clasificar_nota(nota_invalida)
    print(str(excinfo.value))
    assert "fuera del rango" in str(excinfo.value)

def test_clasificar_nota_error_tipo_incorrecto():
    # Arrange
    nota_invalida = "Falla"
    # Act & Assert
    with pytest.raises(TypeError) as excinfo:
        clasificar_nota(nota_invalida)
    assert "not supported between" in str(excinfo.value)