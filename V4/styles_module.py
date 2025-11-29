# styles_module.py - СИСТЕМА СТИЛЕЙ И ТЕМ
from .old_functions import ContentElement, ElementStyle, BorderStyle, TextStyle, RGBColor, Pt
from typing import Dict

class StyleSystem:
    """Система управления стилями элементов"""
    
    def __init__(self, theme: Dict):
        self.theme = theme
        self.style_classes = {}
    
    def apply_style(self, element: ContentElement, style_config: Dict) -> ContentElement:
        """Применяет стили к элементу"""
        for key, value in style_config.items():
            if key == 'background_color':
                element.style.background_color = value
            elif key == 'border_color':
                # Исправление: гарантируем что border не None
                if element.style.border is None:
                    element.style.border = BorderStyle()
                element.style.border.color = value
            elif key == 'border_width':
                # Исправление: гарантируем что border не None
                if element.style.border is None:
                    element.style.border = BorderStyle()
                element.style.border.width = Pt(value) if isinstance(value, (int, float)) else value
            elif key == 'padding':
                element.style.padding = value
            elif key == 'text_color':
                if element.style.text_style is None:
                    element.style.text_style = TextStyle()
                element.style.text_style.font_color = value
            elif key == 'font_size':
                if element.style.text_style is None:
                    element.style.text_style = TextStyle()
                element.style.text_style.font_size = Pt(value) if isinstance(value, (int, float)) else value
            elif key == 'bold':
                if element.style.text_style is None:
                    element.style.text_style = TextStyle()
                element.style.text_style.bold = value
            elif key == 'align':
                if element.style.text_style is None:
                    element.style.text_style = TextStyle()
                element.style.text_style.align = value
        
        return element
    
    def define_style_class(self, class_name: str, style_config: Dict):
        """Определяет класс стилей для повторного использования"""
        self.style_classes[class_name] = style_config
    
    def apply_style_class(self, element: ContentElement, class_name: str) -> ContentElement:
        """Применяет класс стилей к элементу"""
        if class_name in self.style_classes:
            return self.apply_style(element, self.style_classes[class_name])
        else:
            print(f"⚠️  Класс стилей '{class_name}' не найден")
            return element
    
    def create_theme_variant(self, base_theme: Dict, is_dark: bool = True) -> Dict:
        """Создает вариант темы (темный/светлый)"""
        variant = base_theme.copy()
        
        if is_dark:
            # Темный вариант
            variant['background'] = RGBColor(25, 25, 35)
            variant['text'] = RGBColor(255, 255, 255)
            variant['footnote'] = RGBColor(180, 180, 180)
        else:
            # Светлый вариант
            variant['background'] = RGBColor(255, 255, 255)
            variant['text'] = RGBColor(33, 33, 33)
            variant['footnote'] = RGBColor(100, 100, 100)
        
        return variant