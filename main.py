from PIL import Image
import time
import os

# Символы и настройки
chars = ["T", ".", "B", "C", "M", "N", "R", "W"]
map_size = 60  # Размер карты (максимум 60x60 для Brawl Stars)

# Ввод пути изображения
file = input("Enter the image directory: ")
start = time.time()
image = Image.open(file).convert("L")

# Масштабирование изображения до 60x60
image = image.resize((map_size, map_size), Image.Resampling.LANCZOS)
width, height = image.size

# Предварительная загрузка блоков
blocks = {char: Image.open(f"block/block_{char}.png") for char in chars}

# Создаем новое изображение
res = Image.new('RGB', (width * 20, height * 20))

# Обработка изображения
pixels = list(image.getdata())  # Получаем все пиксели как массив
for y in range(height):
    for x in range(width):
        # Если середина карты, добавляем линию толщиной в 2 клетки
        if map_size // 2 - 1 <= y <= map_size // 2:
            char = "R"  # Символ для линии, замените на нужный блок
        else:
            pixel_value = pixels[y * width + x]
            char_index = int((pixel_value / 255) * (len(chars) - 1))
            char = chars[char_index]
        res.paste(blocks[char], (x * 20, y * 20))  # Добавляем блок на изображение

# Запрос пути для сохранения изображения
save_path = input("Enter the directory where you want to save the image (or just the folder name): ")

# Если путь не абсолютный, добавляем к нему путь Pictures
if not os.path.isabs(save_path):
    save_path = f"/storage/emulated/0/Pictures/{save_path}"

# Убедимся, что папка существует, и создадим ее, если нужно
os.makedirs(save_path, exist_ok=True)

# Сохранение результата в указанную папку
name = f"{time.time():.0f}.png"
full_path = os.path.join(save_path, name)
res.save(full_path)

# Вывод информации о сохранении
end = time.time()
print(f"Image saved to {full_path}\nTotal time: {round((end - start), 3)} seconds!")