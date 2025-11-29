# Создаем виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Обновляем pip
pip install --upgrade pip

# Для GPU с CUDA 11.8:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# ИЛИ для CPU (если нет GPU):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Основные библиотеки
pip install transformers accelerate bitsandbytes
pip install diffusers python-pptx pillow
pip install requests beautifulsoup4
pip install tiktoken protobuf
#pip install bitsandbytes
pip install peft


