# model_downloader_public.py
import os
import subprocess
from huggingface_hub import snapshot_download
import sys
import shutil

class PublicModelDownloader:
    def __init__(self, download_dir="/home/nic/МоиФайлы/Учеба/Вуз/Нейросеть для презентаций/presentation_generator/models/Model_Next_Generetion"):
        self.download_dir = download_dir
        
        # ПУБЛИЧНЫЕ МОДЕЛИ, КОТОРЫЕ РАБОТАЮТ БЕЗ АВТОРИЗАЦИИ
        self.models_to_download = {
            "text": {
                "mistral_7b_instruct": "mistralai/Mistral-7B-Instruct-v0.2",  # Отличная инструктивная модель
                "openchat_3.5": "openchat/openchat-3.5-1210",  # Хорошо следует инструкциям
                "zephyr_7b": "HuggingFaceH4/zephyr-7b-beta",  # Качественная инструктивная модель
            },
            "image": {
                "sdxl_base": "stabilityai/stable-diffusion-xl-base-1.0",
                "sd_2.1": "stabilityai/stable-diffusion-2-1",
                "kandinsky_2.2": "kandinsky-community/kandinsky-2-2-decoder",
            }
        }
        
        # Создаем целевую директорию
        os.makedirs(self.download_dir, exist_ok=True)
        print(f"📁 Модели будут скачаны в: {self.download_dir}")
        
    def download_model(self, model_type, model_name, hf_repo):
        """Скачивание одной модели"""
        print(f"📥 Начинаю загрузку {model_name}...")
        
        try:
            target_dir = os.path.join(self.download_dir, model_type, model_name)
            os.makedirs(target_dir, exist_ok=True)
            
            print(f"🎯 Целевая директория: {target_dir}")
            print(f"🔗 Репозиторий: {hf_repo}")
            
            # Используем токен None для публичных репозиториев
            snapshot_download(
                repo_id=hf_repo,
                local_dir=target_dir,
                local_dir_use_symlinks=False,
                resume_download=True,
                max_workers=4,
                token=None  # Явно указываем None для публичных репозиториев
            )
            
            print(f"✅ {model_name} успешно загружена!")
            
            # Проверяем размер
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(target_dir):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            
            print(f"📦 Размер модели: {total_size / (1024**3):.2f} GB")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка загрузки {model_name}: {e}")
            return False
    
    def download_priority_models(self):
        """Загрузка приоритетных моделей"""
        print("🚀 Загрузка приоритетных моделей...")
        
        # Текстовые модели (приоритет)
        print("\n📝 ТЕКСТОВЫЕ МОДЕЛИ:")
        self.download_model("text", "mistral_7b_instruct", 
                          self.models_to_download["text"]["mistral_7b_instruct"])
        
        # Графические модели (приоритет)  
        print("\n🎨 ГРАФИЧЕСКИЕ МОДЕЛИ:")
        self.download_model("image", "sdxl_base",
                          self.models_to_download["image"]["sdxl_base"])
        
        print("\n🎉 Основные модели загружены!")
    
    def download_additional_models(self):
        """Загрузка дополнительных моделей"""
        print("\n📦 Загрузка дополнительных моделей...")
        
        self.download_model("text", "openchat_3.5",
                          self.models_to_download["text"]["openchat_3.5"])
        self.download_model("image", "kandinsky_2.2",
                          self.models_to_download["image"]["kandinsky_2.2"])
        
        print("✅ Дополнительные модели загружены!")
    
    def check_disk_space(self):
        """Проверка свободного места на диске"""
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)
        print(f"📊 Свободно на диске: {free_gb} GB")
        
        required_gb = 40
        if free_gb < required_gb:
            print(f"⚠️  Внимание: требуется минимум {required_gb}GB свободного места")
            return False
        return True

def main():
    target_directory = "/home/nic/МоиФайлы/Учеба/Вуз/Нейросеть для презентаций/presentation_generator/models/Model_Next_Generetion"
    
    downloader = PublicModelDownloader(target_directory)
    
    print("🤖 СИСТЕМА ЗАГРУЗКИ ПУБЛИЧНЫХ МОДЕЛЕЙ")
    print("=" * 60)
    print(f"🎯 Целевая директория: {target_directory}")
    print("=" * 60)
    
    # Проверка доступного места
    if not downloader.check_disk_space():
        return
    
    # Загрузка приоритетных моделей
    downloader.download_priority_models()
    
    # Предложение загрузить дополнительные
    choice = input("\nЗагрузить дополнительные модели? (y/n): ")
    if choice.lower() == 'y':
        downloader.download_additional_models()
    
    print(f"\n📋 ЗАГРУЖЕННЫЕ МОДЕЛИ:")
    print("Текстовые:")
    print("  - Mistral 7B Instruct (основная)")
    print("  - OpenChat 3.5 (дополнительная)")
    print("\nГрафические:")
    print("  - SDXL Base (основная)")
    print("  - Kandinsky 2.2 (резервная)")

if __name__ == "__main__":
    main()