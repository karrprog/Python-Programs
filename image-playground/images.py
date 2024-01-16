from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.convert('L')
filtered_img = img.filter(ImageFilter.DETAIL)
filtered_img.save("detail.png", 'png')
# filtered_img.show()
resize = filtered_img.resize((300, 300))
resize.save("resized.png", 'png')