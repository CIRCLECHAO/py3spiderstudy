import tesserocr
from PIL import Image

image = Image.open('../pic/CheckCode.jpg')
# image = image.convert('1')
image = image.convert('L')
threshold = 165
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)