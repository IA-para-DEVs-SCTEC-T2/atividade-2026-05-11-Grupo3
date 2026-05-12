import pytest
from teste import validar_senha


# Senhas inválidas
def test_senha_muito_curta():
    assert validar_senha("Ab1") == False

def test_senha_sem_maiuscula():
    assert validar_senha("abcdefg1") == False

def test_senha_sem_numero():
    assert validar_senha("Abcdefgh") == False

def test_senha_curta_sem_maiuscula_sem_numero():
    assert validar_senha("abc") == False


# Senhas válidas
def test_senha_valida_minima():
    assert validar_senha("Abcdef1g") == True

def test_senha_valida_longa():
    assert validar_senha("Senha123Segura") == True

def test_senha_valida_multiplos_numeros():
    assert validar_senha("Abc12345") == True
