# text_module.py
from .old_functions import ContentElement, TextStyle, ElementStyle, BorderStyle, Inches, Pt, RGBColor
from typing import Dict

class AdvancedTextModule:
    def __init__(self):
        self.FONT_CONFIG = {
            "title": {"base": 22, "min": 18, "max": 32},
            "subtitle": {"base": 20, "min": 18, "max": 24},
            "main": {"base": 16, "min": 14, "max": 18},
            "caption": {"base": 12, "min": 10, "max": 14},
            "footnote": {"base": 10, "min": 8, "max": 12}
        }
    
    def create_text_element(self, text: str, x: float = None, y: float = None, 
                          width: float = None, height: float = None, **kwargs) -> ContentElement:
        from .old_functions import create_text_element
        element = create_text_element(text, x, y, width, height, **kwargs)
        
        # Применяем стили с проверкой на None
        if 'background_color' in kwargs:
            element.style.background_color = kwargs['background_color']
        
        if 'border_color' in kwargs:
            if element.style.border is None:
                element.style.border = BorderStyle()
            element.style.border.color = kwargs['border_color']
        
        if 'border_width' in kwargs:
            if element.style.border is None:
                element.style.border = BorderStyle()
            element.style.border.width = kwargs['border_width']
        
        if 'padding' in kwargs:
            element.style.padding = kwargs['padding']
        
        # Обработка текстовых стилей
        if any(key in kwargs for key in ['text_color', 'bold', 'italic', 'align', 'font_size']):
            if element.style.text_style is None:
                element.style.text_style = TextStyle()
            
            if 'text_color' in kwargs:
                element.style.text_style.font_color = kwargs['text_color']
            if 'bold' in kwargs:
                element.style.text_style.bold = kwargs['bold']
            if 'italic' in kwargs:
                element.style.text_style.italic = kwargs['italic']
            if 'align' in kwargs:
                element.style.text_style.align = kwargs['align']
            if 'font_size' in kwargs:
                element.style.text_style.font_size = kwargs['font_size']
        
        return element
    
    def calculate_font_size(self, element: ContentElement, available_width: float, available_height: float) -> float:
        if not isinstance(element.content, str):
            return self.FONT_CONFIG["main"]["base"]
        
        text = element.content
        text_type = self._detect_text_type(element, text)
        config = self.FONT_CONFIG[text_type]
        
        base_size = config["base"]
        min_size = config["min"]
        max_size = config["max"]
        
        # Упрощенный расчет
        chars_per_inch = 7
        max_chars_per_line = available_width * chars_per_inch
        
        if len(text) > max_chars_per_line and max_chars_per_line > 0:
            lines_needed = len(text) / max_chars_per_line
            reduction = min(4, (lines_needed - 1) * 1.5)
            base_size = max(min_size, base_size - reduction)
        
        return max(min_size, min(max_size, base_size))
    
    def _detect_text_type(self, element: ContentElement, text: str) -> str:
        if element.style.text_style and element.style.text_style.font_size:
            if element.style.text_style.font_size >= 20:
                return "title"
            elif element.style.text_style.font_size <= 10:
                return "footnote"
        
        if len(text) < 15:
            return "caption"
        
        if any(marker in text for marker in ['•', '-', '—', '·', '1.', '2.', '3.']):
            return "subtitle"
        
        if len(text) > 100:
            return "main"
        
        if len(text) < 50 and (text.isupper() or text[0].isupper() and text[-1] in '!?:'):
            return "title"
        
        return "main"