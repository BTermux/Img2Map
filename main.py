from PIL import Image
import time
import os

chars = ["T", ".", "B", "C", "M", "N", "R", "W"]
map_size = 60

file = input("Enter the image directory: ")
start = time.time()
image = Image.open(file).convert("L")

image = image.resize((map_size, map_size), Image.Resampling.LANCZOS)
width, height = image.size

blocks = {char: Image.open(f"block/block_{char}.png") for char in chars}

res = Image.new('RGB', (width * 20, height * 20))

pixels = list(image.getdata())
for y in range(height):
    for x in range(width):
        if map_size // 2 - 1 <= y <= map_size // 2:
            char = "R"
        else:
            pixel_value = pixels[y * width + x]
            char_index = int((pixel_value / 255) * (len(chars) - 1))
            char = chars[char_index]
        res.paste(blocks[char], (x * 20, y * 20))

save_path = input("Enter the directory where you want to save the image (or just the folder name): ")

if not os.path.isabs(save_path):
    save_path = f"/storage/emulated/0/Pictures/{save_path}"

os.makedirs(save_path, exist_ok=True)

name = f"{time.time():.0f}.png"
full_path = os.path.join(save_path, name)
res.save(full_path)

end = time.time()
print(f"Image saved to {full_path}\nTotal time: {round((end - start), 3)} seconds!")