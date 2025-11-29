# __init__.py
from .core import (
    PresentationGenerator,
    create_presentation,
    Slide,
    ContentElement,
    ContentType,
    ElementStyle,
    TextStyle,
    BorderStyle,
    SizeConstraints,
    LayoutStrategy,
    Inches,
    Pt,
    RGBColor,
    PP_ALIGN,
    MSO_SHAPE
)

__version__ = "4.0.0"
__author__ = "Presentation Generator Team"

__all__ = [
    'PresentationGenerator',
    'create_presentation',
    'Slide',
    'ContentElement',
    'ContentType',
    'ElementStyle',
    'TextStyle',
    'BorderStyle',
    'SizeConstraints',
    'LayoutStrategy',
    'Inches',
    'Pt',
    'RGBColor',
    'PP_ALIGN',
    'MSO_SHAPE'
]