from PIL import Image
import time

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

# Сохранение результата в папку Pictures
name = f"/storage/emulated/0/Pictures/{time.time():.0f}.png"
res.save(name)

# Вывод информации о сохранении
end = time.time()
print(f"Image saved to {name}\nTotal time: {round((end - start), 3)} seconds!")