# media_module.py - УЛУЧШЕННАЯ СИСТЕМА ПОИСКА
from .old_functions import ContentElement, ContentType, RGBColor
import os
import glob
import re

class MediaManager:
    """Управление изображениями и медиа-контентом"""
    
    def __init__(self):
        self.debug = True
        self.images_base_path = "/home/nic/МоиФайлы/Учеба/Вуз/Нейросеть_для_презентаций/presentation_generator/Вариант4/Картинки"
        self.image_cache = {}  # Кэш путей к изображениям
        self.image_categories = {}  # Категории изображений
        self._build_image_cache()
    
    def _build_image_cache(self):
        """Создает кэш всех изображений в папке и категоризирует их"""
        if os.path.exists(self.images_base_path):
            image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
            for extension in image_extensions:
                pattern = os.path.join(self.images_base_path, extension)
                for image_path in glob.glob(pattern):
                    image_name = os.path.splitext(os.path.basename(image_path))[0]
                    self.image_cache[image_name] = image_path
                    
                    # Автоматически определяем категории
                    self._categorize_image(image_name, image_path)
                    
            if self.debug:
                print(f"🖼️  Загружено {len(self.image_cache)} изображений из кэша")
                self._print_categories()
        else:
            print(f"⚠️  Папка с изображениями не найдена: {self.images_base_path}")
    
    def _categorize_image(self, image_name: str, image_path: str):
        """Автоматически категоризирует изображения по ключевым словам"""
        name_lower = image_name.lower()
        
        categories = {
            'technology': ['tech', 'computer', 'digital', 'ai', 'artificial', 'intelligence', 'robot', 'future'],
            'data': ['data', 'analytics', 'chart', 'graph', 'statistic', 'analysis'],
            'business': ['business', 'office', 'meeting', 'presentation', 'corporate', 'strategy'],
            'education': ['education', 'learn', 'study', 'book', 'school', 'university'],
            'network': ['network', 'connection', 'web', 'internet', 'cloud'],
            'innovation': ['innovation', 'creative', 'idea', 'lightbulb', 'solution'],
            'teamwork': ['team', 'collaboration', 'group', 'people', 'teamwork'],
            'success': ['success', 'growth', 'achievement', 'goal', 'target']
        }
        
        for category, keywords in categories.items():
            if any(keyword in name_lower for keyword in keywords):
                if category not in self.image_categories:
                    self.image_categories[category] = []
                self.image_categories[category].append(image_name)
    
    def _print_categories(self):
        """Показывает автоматически определенные категории"""
        print("\n📂 АВТОМАТИЧЕСКИЕ КАТЕГОРИИ:")
        for category, images in self.image_categories.items():
            print(f"   {category}: {len(images)} изображений")
    
    def create_image_element(self, image_path: str, x: float = None, y: float = None,
                           width: float = None, height: float = None, **kwargs) -> ContentElement:
        """Создает элемент изображения по полному пути"""
        element = ContentElement(
            id=f"image_{os.path.basename(image_path)}",
            type=ContentType.IMAGE,
            content=image_path,
            x=x, y=y, width=width, height=height
        )
        
        # Применяем дополнительные параметры
        for key, value in kwargs.items():
            if hasattr(element, key):
                setattr(element, key, value)
        
        if self.debug:
            print(f"🖼️  Создан элемент изображения: {os.path.basename(image_path)}")
        
        return element
    
    def create_image_by_name(self, image_name: str, x: float = None, y: float = None,
                           width: float = None, height: float = None, **kwargs) -> ContentElement:
        """Создает элемент изображения по имени файла (без расширения)"""
        image_path = self.get_image_path(image_name)
        
        if image_path:
            return self.create_image_element(image_path, x, y, width, height, **kwargs)
        else:
            print(f"⚠️  Изображение '{image_name}' не найдено в папке")
            # Создаем заглушку
            return self._create_placeholder_element(image_name, x, y, width, height, **kwargs)
    
    def get_image_path(self, image_name: str) -> str:
        """Возвращает полный путь к изображению по имени"""
        # Прямой поиск в кэше
        if image_name in self.image_cache:
            return self.image_cache[image_name]
        
        # Попробуем найти с различными расширениями
        possible_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        for ext in possible_extensions:
            possible_path = os.path.join(self.images_base_path, image_name + ext)
            if os.path.exists(possible_path):
                self.image_cache[image_name] = possible_path
                return possible_path
        
        return None
    
    def _create_placeholder_element(self, image_name: str, x: float, y: float,
                                  width: float, height: float, **kwargs) -> ContentElement:
        """Создает элемент-заглушку если изображение не найдено"""
        placeholder = ContentElement(
            id=f"placeholder_{image_name}",
            type=ContentType.SHAPE,
            content={'shape_type': 'rectangle'},
            x=x, y=y, width=width, height=height
        )
        
        # Стиль для заглушки
        placeholder.style.background_color = kwargs.get('fallback_color', RGBColor(100, 100, 150))
        
        # Текст с названием изображения
        placeholder.metadata['placeholder_text'] = f"Изобр: {image_name}"
        
        print(f"🟦 Создана заглушка для: {image_name}")
        return placeholder
    
    def list_available_images(self):
        """Показывает все доступные изображения"""
        print("\n📁 ДОСТУПНЫЕ ИЗОБРАЖЕНИЯ:")
        print("=" * 50)
        for name, path in self.image_cache.items():
            print(f"🎨 {name}")
            print(f"   📁 {path}")
        print(f"\nВсего: {len(self.image_cache)} изображений")
    
    def search_images(self, keyword: str):
        """Ищет изображения по ключевому слову в названии"""
        matches = [name for name in self.image_cache.keys() if keyword.lower() in name.lower()]
        return matches
    
    def get_images_by_category(self, category: str):
        """Возвращает изображения по категории"""
        return self.image_categories.get(category, [])
    
    def get_all_categories(self):
        """Возвращает все доступные категории"""
        return list(self.image_categories.keys())
    
    def suggest_images_for_topic(self, topic: str):
        """Предлагает изображения для заданной темы"""
        topic_lower = topic.lower()
        suggestions = []
        
        # Сопоставляем тему с категориями
        topic_mappings = {
            'искусственный интеллект': ['technology', 'innovation'],
            'машинное обучение': ['technology', 'data'],
            'анализ данных': ['data', 'business'],
            'бизнес': ['business', 'teamwork', 'success'],
            'образование': ['education', 'innovation'],
            'технологии': ['technology', 'innovation'],
            'нейросети': ['technology', 'network'],
            'инновации': ['innovation', 'technology']
        }
        
        for topic_key, categories in topic_mappings.items():
            if topic_key in topic_lower:
                for category in categories:
                    suggestions.extend(self.get_images_by_category(category))
        
        # Убираем дубликаты
        return list(set(suggestions))
    
    def add_animation(self, element: ContentElement, animation_type: str = "fade"):
        """Добавляет анимацию к элементу (заглушка)"""
        print(f"⚠️  Анимации типа '{animation_type}' еще не реализованы")
        element.metadata['animation'] = animation_type
        return element