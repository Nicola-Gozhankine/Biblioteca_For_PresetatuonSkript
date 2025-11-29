from diffusers import StableDiffusionPipeline

def download_image_model():
    print("🎨 Загружаем графическую модель в полной точности...")
    
    model_name = "runwayml/stable-diffusion-v1-5"
    
    # ЗАГРУЖАЕМ БЕЗ ЭКОНОМИИ ПАМЯТИ
    pipe = StableDiffusionPipeline.from_pretrained(model_name)
    
    pipe.save_pretrained("./models/image_full")
    
    print("✅ Графическая модель загружена в полной точности")

if __name__ == "__main__":
    download_image_model()