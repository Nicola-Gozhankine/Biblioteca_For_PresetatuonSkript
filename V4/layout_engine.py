# layout_engine.py - УМНАЯ СИСТЕМА КОМПОНОВКИ
from .old_functions import Inches, ContentElement
from typing import Tuple, Optional, List

class SmartLayoutEngine:
    """Умная система компоновки элементов на слайде"""
    
    def __init__(self, slide_width: float, slide_height: float):
        self.slide_width = slide_width
        self.slide_height = slide_height
        self.occupied_areas = []
        self.safe_margin = Inches(0.5)
    
    def calculate_bounds(self, element: ContentElement, parent_bounds: Optional[Tuple] = None) -> Optional[Tuple]:
        """Вычисляет границы элемента"""
        if element.layout_strategy == "manual":
            return self._calculate_manual_bounds(element, parent_bounds)
        return self._calculate_manual_bounds(element, parent_bounds)
    
    def _calculate_manual_bounds(self, element: ContentElement, parent_bounds: Optional[Tuple]) -> Tuple:
        """Ручное размещение"""
        if parent_bounds:
            parent_x, parent_y, parent_w, parent_h = parent_bounds
            x = parent_x + (element.x or 0)
            y = parent_y + (element.y or 0)
            width = min(element.width or parent_w, parent_w)
            height = min(element.height or parent_h, parent_h)
        else:
            x = element.x or self.safe_margin
            y = element.y or self.safe_margin
            width = element.width or (self.slide_width - 2 * self.safe_margin)
            height = element.height or (self.slide_height - 2 * self.safe_margin)
        
        return (x, y, width, height)
    
    def reserve_area(self, x: float, y: float, width: float, height: float):
        """Резервирует область как занятую"""
        self.occupied_areas.append((x, y, width, height))
    
    def calculate_child_bounds(self, parent_bounds: Tuple, padding: float) -> Tuple:
        """Вычисляет границы для дочернего элемента"""
        parent_x, parent_y, parent_w, parent_h = parent_bounds
        return (
            parent_x + padding,
            parent_y + padding,
            parent_w - 2 * padding,
            parent_h - 2 * padding
        )
    
    def auto_place_element(self, element: ContentElement, relative_to=None, alignment="top_left"):
        """Автоматическое размещение (заглушка для будущей реализации)"""
        print("⚠️  Автоматическое размещение еще не реализовано, используется ручное")
        return self._calculate_manual_bounds(element, None)