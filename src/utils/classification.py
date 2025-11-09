# src/utils/classification.py

from src.utils.rules import RULES

def clasificar_producto(nombre):
    texto = nombre.lower()

    # Recorrer categorías y keywords
    for categoria, keywords in RULES.items():
        for kw in keywords:
            if kw in texto:
                return categoria

    # Fallback final
    return "Alimentos secos"
