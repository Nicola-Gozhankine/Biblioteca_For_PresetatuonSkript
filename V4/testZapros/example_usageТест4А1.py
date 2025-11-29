# example_usage.py - ПРИМЕР ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ
from Вариант4.core import create_presentation, Inches, RGBColor, Pt , PresentationGenerator
from Вариант4.old_functions import PP_ALIGN
import math
from Вариант4.media_module import MediaManager
import inspect
import sys
import os


def create_future_tech_presentation():
    """Создает презентацию о будущем технологий с использованием сгенерированных изображений"""
    
    print("🚀 СОЗДАНИЕ ПРЕЗЕНТАЦИИ О БУДУЩЕМ ТЕХНОЛОГИЙ")
    print("=" * 60)
    
    presentation = create_presentation(theme="dark_pro")
    
    # Ожидаемые изображения
    expected_images = [
        "ai_brain_network",
        "data_analysis_dashboard",
        "quantum_computing_core", 
        "smart_city_future",
        "cybersecurity_shield",
        "biotech_dna_helix",
        "blockchain_network",
        "robotics_automation",
        "virtual_reality_metaverse"
    ]
    
    # Проверяем доступность изображений
    available_images = []
    for img_name in expected_images:
        if img_name in presentation.media_manager.image_cache:
            available_images.append(img_name)
        else:
            print(f"⚠️  Изображение отсутствует: {img_name}")
    
    print(f"📊 Доступно изображений: {len(available_images)} из {len(expected_images)}")
    
    # ===== СЛАЙД 1: ТИТУЛЬНЫЙ =====
    slide1 = presentation.create_slide("Будущее Технологий: 2025-2035")
    _create_title_slide(presentation, slide1, available_images)
    
    # ===== СЛАЙД 2: ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ =====
    slide2 = presentation.create_slide("Искусственный Интеллект и Нейросети")
    _create_ai_slide(presentation, slide2, available_images)
    
    # ===== СЛАЙД 3: АНАЛИЗ ДАННЫХ =====
    slide3 = presentation.create_slide("Большие Данные и Аналитика")
    _create_data_slide(presentation, slide3, available_images)
    
    # ===== СЛАЙД 4: КВАНТОВЫЕ ВЫЧИСЛЕНИЯ =====
    slide4 = presentation.create_slide("Квантовые Вычисления")
    _create_quantum_slide(presentation, slide4, available_images)
    
    # ===== СЛАЙД 5: УМНЫЕ ГОРОДА =====
    slide5 = presentation.create_slide("Умные Города и IoT")
    _create_smart_city_slide(presentation, slide5, available_images)
    
    # ===== СЛАЙД 6: КИБЕРБЕЗОПАСНОСТЬ =====
    slide6 = presentation.create_slide("Кибербезопасность Будущего")
    _create_cybersecurity_slide(presentation, slide6, available_images)
    
    # ===== СЛАЙД 7: БИОТЕХНОЛОГИИ =====
    slide7 = presentation.create_slide("Биотехнологии и Генетика")
    _create_biotech_slide(presentation, slide7, available_images)
    
    # ===== СЛАЙД 8: БЛОКЧЕЙН =====
    slide8 = presentation.create_slide("Блокчейн и Web 3.0")
    _create_blockchain_slide(presentation, slide8, available_images)
    
    # ===== СЛАЙД 9: РОБОТОТЕХНИКА И VR =====
    slide9 = presentation.create_slide("Робототехника и Виртуальная Реальность")
    _create_robotics_vr_slide(presentation, slide9, available_images)
    
    filename = "будущее_технологий_презентация.pptx"
    presentation.save(filename)
    
    print(f"\n🎉 ПРЕЗЕНТАЦИЯ СОЗДАНА: {filename}")
    print("📊 Статистика:")
    print(f"   • Слайдов: 9")
    print(f"   • Изображений использовано: {len(available_images)}")
    print(f"   • Соотношение текст/изображения: ~50%/50%")
    
    return filename

def _create_title_slide(presentation, slide, available_images):
    """Титульный слайд"""
    # Фоновое изображение если есть
    if available_images:
        presentation.add_image_by_name(
            available_images[0],  # Первое изображение как фон
            x=Inches(0), y=Inches(0),
            width=Inches(13.33), height=Inches(7.5)
        )
        
        # Темный оверлей
        presentation.add_shape(
            "rectangle",
            x=Inches(0), y=Inches(0),
            width=Inches(13.33), height=Inches(7.5),
            background_color=RGBColor(0, 0, 0)
        )
    
    # Главный заголовок
    presentation.add_text(
        "БУДУЩЕЕ ТЕХНОЛОГИЙ",
        x=Inches(1), y=Inches(2),
        width=Inches(11), height=Inches(1.5),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        align=PP_ALIGN.CENTER,
        font_size=Pt(40)
    )
    
    # Подзаголовок
    presentation.add_text(
        "Обзор ключевых технологических трендов 2025-2035",
        x=Inches(1), y=Inches(3.8),
        width=Inches(11), height=Inches(0.8),
        text_color=RGBColor(200, 200, 200),
        align=PP_ALIGN.CENTER,
        font_size=Pt(20)
    )
    
    # Автор
    presentation.add_text(
        "Технологический обзор\nПодготовлен с использованием ИИ",
        x=Inches(1), y=Inches(6),
        width=Inches(11), height=Inches(0.8),
        text_color=RGBColor(150, 150, 150),
        align=PP_ALIGN.CENTER,
        font_size=Pt(14)
    )
    
    slide.render()

def _create_ai_slide(presentation, slide, available_images):
    """Слайд про ИИ"""
    presentation.add_text(
        "Искусственный Интеллект и Нейросети",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(41, 128, 185),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Изображение ИИ если есть
    ai_image = "ai_brain_network"
    if ai_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            ai_image,
            x=Inches(1), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    # Текст про ИИ
    ai_text = """🧠 Революция в обработке данных:

• Глубокое обучение превосходит человеческие возможности
• Генеративные модели создают контент
• Персонализированные ИИ-ассистенты

📈 К 2030 году:
- ИИ добавит $15 трлн к мировой экономике
- Автоматизирует 30% рабочих задач
- Станет неотъемлемой частью медицины"""

    presentation.add_text(
        ai_text,
        x=Inches(6.5), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    slide.render()

def _create_data_slide(presentation, slide, available_images):
    """Слайд про анализ данных"""
    presentation.add_text(
        "Большие Данные и Аналитика",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(39, 174, 96),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Текст про данные
    data_text = """📊 Данные - новая валюта:

• Объем данных растет экспоненциально
• AI-driven аналитика в реальном времени
• Predictive analytics для бизнеса

🔮 Тренды до 2030:
- Квантовые базы данных
- Федеративное обучение
- Explainable AI для прозрачности"""

    presentation.add_text(
        data_text,
        x=Inches(1), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    # Изображение анализа данных если есть
    data_image = "data_analysis_dashboard"
    if data_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            data_image,
            x=Inches(6.5), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    slide.render()

def _create_quantum_slide(presentation, slide, available_images):
    """Слайд про квантовые вычисления"""
    presentation.add_text(
        "Квантовые Вычисления",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(142, 68, 173),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Изображение квантовых вычислений если есть
    quantum_image = "quantum_computing_core"
    if quantum_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            quantum_image,
            x=Inches(1), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    # Текст про квантовые вычисления
    quantum_text = """⚛️ Квантовая революция:

• Решение недоступных классическим компьютерам задач
• Квантовое превосходство достигнуто
• Криптография и оптимизация

🎯 Применение:
- Молекулярное моделирование
- Квантовая химия
- Финансовое моделирование
- Логистическая оптимизация"""

    presentation.add_text(
        quantum_text,
        x=Inches(6.5), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    slide.render()

def _create_smart_city_slide(presentation, slide, available_images):
    """Слайд про умные города"""
    presentation.add_text(
        "Умные Города и IoT",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(230, 126, 34),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Текст про умные города
    city_text = """🏙️ Города будущего:

• 70% населения будет жить в городах к 2050
• IoT устройства для управления инфраструктурой
• Умные сети энергоснабжения

🏗️ Технологии:
- Автономный транспорт
- Умные здания
- Цифровые двойники городов
- Устойчивая энергетика"""

    presentation.add_text(
        city_text,
        x=Inches(1), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    # Изображение умного города если есть
    city_image = "smart_city_future"
    if city_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            city_image,
            x=Inches(6.5), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    slide.render()

def _create_cybersecurity_slide(presentation, slide, available_images):
    """Слайд про кибербезопасность"""
    presentation.add_text(
        "Кибербезопасность Будущего",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(231, 76, 60),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Изображение кибербезопасности если есть
    security_image = "cybersecurity_shield"
    if security_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            security_image,
            x=Inches(1), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    # Текст про безопасность
    security_text = """🛡️ Защита в цифровую эпоху:

• AI-powered системы обнаружения угроз
• Квантовая криптография
• Zero-trust архитектуры

🔒 Новые вызовы:
- Защита IoT устройств
- Безопасность ИИ систем
- Квантовые атаки
- Privacy-preserving технологии"""

    presentation.add_text(
        security_text,
        x=Inches(6.5), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    slide.render()

def _create_biotech_slide(presentation, slide, available_images):
    """Слайд про биотехнологии"""
    presentation.add_text(
        "Биотехнологии и Генетика",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(39, 174, 96),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Текст про биотехнологии
    bio_text = """🧬 Медицина будущего:

• Персонализированная медицина на основе генома
• Генная терапия и редактирование
• Бионические импланты

💊 Прогресс к 2030:
- Лечение наследственных заболеваний
- Искусственные органы
- Антиэйдж терапия
- Цифровые двойники пациентов"""

    presentation.add_text(
        bio_text,
        x=Inches(1), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    # Изображение биотехнологий если есть
    bio_image = "biotech_dna_helix"
    if bio_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            bio_image,
            x=Inches(6.5), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    slide.render()

def _create_blockchain_slide(presentation, slide, available_images):
    """Слайд про блокчейн"""
    presentation.add_text(
        "Блокчейн и Web 3.0",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(52, 152, 219),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Изображение блокчейна если есть
    blockchain_image = "blockchain_network"
    if blockchain_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            blockchain_image,
            x=Inches(1), y=Inches(1.5),
            width=Inches(5), height=Inches(4)
        )
    
    # Текст про блокчейн
    blockchain_text = """⛓️ Децентрализованное будущее:

• Web 3.0 - семантическая паутина
• Децентрализованные приложения (dApps)
• Цифровая идентичность

🌐 К 2030 году:
- Токенизация активов
- DeFi заменит традиционные финансы
- DAO для управления организациями
- Metaverse экономики"""

    presentation.add_text(
        blockchain_text,
        x=Inches(6.5), y=Inches(1.5),
        width=Inches(5), height=Inches(4),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(14)
    )
    
    slide.render()

def _create_robotics_vr_slide(presentation, slide, available_images):
    """Слайд про робототехнику и VR"""
    presentation.add_text(
        "Робототехника и Виртуальная Реальность",
        x=Inches(0.5), y=Inches(0.5),
        width=Inches(12), height=Inches(0.6),
        background_color=RGBColor(155, 89, 182),
        text_color=RGBColor(255, 255, 255),
        bold=True,
        font_size=Pt(20)
    )
    
    # Два изображения на одном слайде
    robotics_image = "robotics_automation"
    vr_image = "virtual_reality_metaverse"
    
    if robotics_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            robotics_image,
            x=Inches(1), y=Inches(1.5),
            width=Inches(5.5), height=Inches(2.5)
        )
    
    if vr_image in presentation.media_manager.image_cache:
        presentation.add_image_by_name(
            vr_image,
            x=Inches(7), y=Inches(1.5),
            width=Inches(5.5), height=Inches(2.5)
        )
    
    # Текст про робототехнику
    robotics_text = """🤖 Робототехника:
• Коллаборативные роботы (cobots)
• Автономные системы
• Роботы в повседневной жизни"""

    presentation.add_text(
        robotics_text,
        x=Inches(1), y=Inches(4.2),
        width=Inches(5.5), height=Inches(1.5),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(12)
    )
    
    # Текст про VR
    vr_text = """👓 Виртуальная Реальность:
• Метавселенные
• Иммерсивное обучение
• Удаленная коллаборация"""

    presentation.add_text(
        vr_text,
        x=Inches(7), y=Inches(4.2),
        width=Inches(5.5), height=Inches(1.5),
        text_color=RGBColor(255, 255, 255),
        font_size=Pt(12)
    )
    
    slide.render()

if __name__ == "__main__":
    create_future_tech_presentation()