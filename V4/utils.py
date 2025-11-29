# utils.py - ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ И УТИЛИТЫ
from .old_functions import (
    ColorThemes, Inches, Pt, RGBColor, PP_ALIGN, MSO_SHAPE,
    ContentElement, ContentType, ElementStyle, TextStyle, BorderStyle, SizeConstraints
)

# Реэкспортируем все необходимое
__all__ = [
    'ColorThemes', 'Inches', 'Pt', 'RGBColor', 'PP_ALIGN', 'MSO_SHAPE',
    'ContentElement', 'ContentType', 'ElementStyle', 'TextStyle', 'BorderStyle', 'SizeConstraints'
]