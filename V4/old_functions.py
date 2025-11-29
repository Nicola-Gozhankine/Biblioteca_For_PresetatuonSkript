# old_functions.py - ВСЕ ФУНКЦИИ ИЗ ПРЕДЫДУЩИХ ВЕРСИЙ
"""
Эталонная реализация всех функций из трех предыдущих версий
Обеспечивает обратную совместимость
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union, Tuple
from enum import Enum
import math

# ===== СКОПИРОВАННЫЕ КЛАССЫ ИЗ ПРЕДЫДУЩИХ ВЕРСИЙ =====

class ContentType(Enum):
    TEXT = "text"
    IMAGE = "image"
    SHAPE = "shape"
    CONTAINER = "container"
    INFOGRAPHIC = "infographic"

class LayoutStrategy(Enum):
    MANUAL = "manual"
    GRID = "grid"
    VERTICAL_STACK = "vstack"
    HORIZONTAL_STACK = "hstack"

@dataclass
class SizeConstraints:
    min_width: Optional[float] = None
    max_width: Optional[float] = None
    min_height: Optional[float] = None
    max_height: Optional[float] = None
    aspect_ratio: Optional[float] = None
    grow_priority: int = 1

@dataclass
class BorderStyle:
    color: Optional[RGBColor] = None
    width: float = Pt(1)
    radius: Optional[float] = None

@dataclass
class TextStyle:
    font_size: Optional[float] = None
    font_color: Optional[RGBColor] = None
    bold: bool = False
    italic: bool = False
    align: PP_ALIGN = PP_ALIGN.LEFT
    vertical_align: int = 1

@dataclass
class ElementStyle:
    background_color: Optional[RGBColor] = None
    border: Optional[BorderStyle] = None
    text_style: Optional[TextStyle] = None
    padding: float = Inches(0.1)
    margin: float = Inches(0.05)

@dataclass
class ContentElement:
    id: str
    type: ContentType
    content: Union[str, Dict, List]
    style: ElementStyle = field(default_factory=ElementStyle)
    constraints: SizeConstraints = field(default_factory=SizeConstraints)
    layout_strategy: LayoutStrategy = LayoutStrategy.MANUAL
    parent: Optional['ContentElement'] = None
    children: List['ContentElement'] = field(default_factory=list)
    x: Optional[float] = None
    y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    metadata: Dict = field(default_factory=dict)
    
    def add_child(self, child: 'ContentElement'):
        child.parent = self
        self.children.append(child)
        return self

# ===== СИСТЕМА ТЕМ (из предыдущих версий) =====

class ColorThemes:
    THEMES = {
        "default": {
            "primary": RGBColor(41, 128, 185),
            "secondary": RGBColor(52, 152, 219),
            "accent": RGBColor(230, 126, 34),
            "background": RGBColor(255, 255, 255),
            "text": RGBColor(33, 33, 33),
            "success": RGBColor(39, 174, 96),
            "warning": RGBColor(241, 196, 15),
            "danger": RGBColor(231, 76, 60),
            "footnote": RGBColor(100, 100, 100)
        },
        "dark_pro": {
            "primary": RGBColor(44, 62, 80),
            "secondary": RGBColor(52, 73, 94),
            "accent": RGBColor(231, 76, 60),
            "background": RGBColor(25, 25, 35),
            "text": RGBColor(255, 255, 255),
            "success": RGBColor(39, 174, 96),
            "warning": RGBColor(241, 196, 15),
            "danger": RGBColor(231, 76, 60),
            "footnote": RGBColor(180, 180, 180)
        },
        "blue_tech": {
            "primary": RGBColor(41, 128, 185),
            "secondary": RGBColor(52, 152, 219),
            "accent": RGBColor(230, 126, 34),
            "background": RGBColor(255, 255, 255),
            "text": RGBColor(33, 33, 33),
            "success": RGBColor(39, 174, 96),
            "warning": RGBColor(241, 196, 15),
            "danger": RGBColor(231, 76, 60),
            "footnote": RGBColor(100, 100, 100)
        }
    }
    
    @classmethod
    def get_theme(cls, theme_name: str) -> Dict:
        return cls.THEMES.get(theme_name, cls.THEMES["default"])
    
    @classmethod
    def get_available_themes(cls) -> List[str]:
        return list(cls.THEMES.keys())

# ===== СТАРЫЕ ФУНКЦИИ ДЛЯ ОБРАТНОЙ СОВМЕСТИМОСТИ =====

def create_text_element(text: str, x: float = None, y: float = None, 
                       width: float = None, height: float = None, 
                       element_id: str = None, **kwargs) -> ContentElement:
    """Старая функция создания текстового элемента"""
    element_id = element_id or f"text_{id(text)}"
    element = ContentElement(
        id=element_id,
        type=ContentType.TEXT,
        content=text,
        x=x, y=y, width=width, height=height
    )
    
    # Применяем дополнительные параметры стиля
    for key, value in kwargs.items():
        if hasattr(element.style, key):
            setattr(element.style, key, value)
    
    return element

def create_shape_element(shape_type: str, x: float = None, y: float = None,
                        width: float = None, height: float = None,
                        element_id: str = None, **kwargs) -> ContentElement:
    """Старая функция создания геометрической фигуры"""
    element_id = element_id or f"shape_{shape_type}"
    element = ContentElement(
        id=element_id,
        type=ContentType.SHAPE,
        content={'shape_type': shape_type},
        x=x, y=y, width=width, height=height
    )
    
    for key, value in kwargs.items():
        if hasattr(element.style, key):
            setattr(element.style, key, value)
    
    return element

def create_container_element(x: float = None, y: float = None,
                           width: float = None, height: float = None,
                           element_id: str = None, **kwargs) -> ContentElement:
    """Старая функция создания контейнера"""
    element_id = element_id or f"container_{id(element_id)}"
    element = ContentElement(
        id=element_id,
        type=ContentType.CONTAINER,
        content={},
        x=x, y=y, width=width, height=height
    )
    
    for key, value in kwargs.items():
        if hasattr(element.style, key):
            setattr(element.style, key, value)
    
    return element

# Экспорт всего для обратной совместимости
__all__ = [
    'ContentElement', 'ContentType', 'ElementStyle', 'TextStyle', 
    'BorderStyle', 'SizeConstraints', 'LayoutStrategy',
    'ColorThemes', 'create_text_element', 'create_shape_element', 
    'create_container_element', 'Inches', 'Pt', 'RGBColor', 
    'PP_ALIGN', 'MSO_SHAPE'
]