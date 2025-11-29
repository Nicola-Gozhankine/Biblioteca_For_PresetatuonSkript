# graphics_module.py - ИНФОГРАФИКА И ДИАГРАММЫ
from .old_functions import ContentElement, ContentType, ElementStyle, BorderStyle, RGBColor, Inches, Pt
from typing import Dict, List
from pptx.enum.shapes import MSO_SHAPE

class GraphicsBuilder:
    """Создатель графиков, диаграмм и инфографики"""
    
    def __init__(self):
        self.debug = True
    
    def create_shape(self, shape_type: str, x: float = None, y: float = None,
                    width: float = None, height: float = None, **kwargs) -> ContentElement:
        """Создает геометрическую фигуру"""
        from .old_functions import create_shape_element
        element = create_shape_element(shape_type, x, y, width, height, **kwargs)
        
        # Применяем стили с проверкой на None
        if 'background_color' in kwargs:
            element.style.background_color = kwargs['background_color']
        
        # Исправление: создаем BorderStyle если его нет
        if 'border_color' in kwargs:
            if element.style.border is None:
                element.style.border = BorderStyle()
            element.style.border.color = kwargs['border_color']
        
        return element
    
    def create_chart(self, chart_type: str, data: Dict, x: float = None, y: float = None,
                    width: float = None, height: float = None, **kwargs) -> ContentElement:
        """Создает диаграмму (заглушка)"""
        print(f"⚠️  Диаграммы типа '{chart_type}' еще не реализованы")
        
        # Создаем текстовое представление данных
        chart_text = f"Диаграмма: {chart_type}\n\n"
        for key, value in data.items():
            chart_text += f"{key}: {value}\n"
        
        element = ContentElement(
            id=f"chart_{chart_type}",
            type=ContentType.TEXT,
            content=chart_text,
            x=x, y=y, width=width, height=height
        )
        
        # Стили для визуального отличия
        element.style.background_color = RGBColor(240, 240, 240)
        if element.style.border is None:
            element.style.border = BorderStyle()
        element.style.border.color = RGBColor(100, 100, 100)
        element.style.border.width = Pt(2)
        element.style.padding = Inches(0.2)
        
        return element
    
    def create_table(self, data: List[List], headers: List[str] = None, x: float = None, 
                    y: float = None, width: float = None, height: float = None, **kwargs) -> ContentElement:
        """Создает таблицу через текстовый модуль"""
        from .text_module import AdvancedTextModule
        text_module = AdvancedTextModule()
        return text_module.create_table(data, headers, x=x, y=y, width=width, height=height, **kwargs)
    
    def _get_shape_type(self, shape_name: str) -> MSO_SHAPE:
        """Возвращает тип фигуры по имени"""
        shapes = {
            'rectangle': MSO_SHAPE.RECTANGLE,
            'rounded_rect': MSO_SHAPE.ROUNDED_RECTANGLE,
            'oval': MSO_SHAPE.OVAL,
            'circle': MSO_SHAPE.OVAL,
            'triangle': MSO_SHAPE.ISOSCELES_TRIANGLE,
            'diamond': MSO_SHAPE.DIAMOND,
            'star': MSO_SHAPE.STAR_5_POINT,
        }
        return shapes.get(shape_name, MSO_SHAPE.RECTANGLE)