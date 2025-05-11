# src/time_parser.py

import re

# Diccionario
NUMEROS = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "veintiuno": 21, "veintidos": 22, "veintitres": 23, "veinticuatro": 24,
    "veinticinco": 25, "veintiseis": 26, "veintisiete": 27, "veintiocho": 28,
    "veintinueve": 29, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5
}

# Proceso de conversión
def palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        return NUMEROS.get(palabra, 0)

def parse_time_to_hours(texto: str) -> float:
    """
    Acepta formatos como:
      - '1 hora y 30 minutos'
      - '90 minutos'
      - '3600 segundos'
      - '1 hora, 30 minutos y 45 segundos'
    Devuelve el tiempo total en horas (float).
    """
    # Normalizar separadores
    texto = texto.replace(",", " ").replace(" y ", " ")
    # Regex con tres grupos opcionales
    pattern = re.compile(
        r'(?:(\w+)\s*horas?)?\s*'
        r'(?:(\w+)\s*minutos?)?\s*'
        r'(?:(\w+)\s*segundos?)?'
    )
    match = pattern.fullmatch(texto.strip())
    if not match:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: '{texto}'")
    # Asignamos las palabras a cada variable
    horas_word, minutos_word, segundos_word = match.groups()
    # Hacemos uso de nuestro diccionario
    horas   = palabra_a_numero(horas_word or "0")
    minutos = palabra_a_numero(minutos_word or "0")
    segundos= palabra_a_numero(segundos_word or "0")
    return horas + minutos/60 + segundos/3600