import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import os

# Настройки
MODEL_NAME = "IlyaGusev/saiga_yandexgpt_8b"
SAVE_PATH = "./models/russian/saiga_yandexgpt_8b"

print(f"🚀 Загружаем {MODEL_NAME}...")

try:
    # Создаем папку
    os.makedirs(SAVE_PATH, exist_ok=True)
    
    # Конфигурация квантования для экономии памяти
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )
    
    # Загружаем модель
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=True
    )
    
    print("✅ Модель загружена! Тестируем...")
    
    # Тестируем на простом промпте
    prompt = "Создай план презентации о искусственном интеллекте:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            repetition_penalty=1.2
        )
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"📝 Результат:\n{result}")
    
    # Сохраняем
    print(f"💾 Сохраняем в: {SAVE_PATH}")
    model.save_pretrained(SAVE_PATH)
    tokenizer.save_pretrained(SAVE_PATH)
    
    print("✅ Модель успешно сохранена!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print("Пробуем следующую модель...")