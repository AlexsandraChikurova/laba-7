from PIL import Image, ImageFilter
import os
def pug1():
    image = Image.open('pug.jpg')
    image.show()
    print("Размер изображения:", image.size)

    print("Формат изображения:", image.format)

    print("Цветовая модель изображения:", image.mode)
def pug2():
    image = Image.open('pug.jpg')
    image.save("pug0.jpg")

    res_img = image.resize((245, 245))
    res_img.save("pug4.jpg")

    res = image.transpose(Image.FLIP_TOP_BOTTOM)
    res.save("pug2.jpg")

    res_i=image.transpose(Image.FLIP_LEFT_RIGHT)
    res_i.save("pug1.jpg")
    print("Обработка изображений завершена.")
def pug3():
    nach = 'D:/Чикурова Александра 1-МД-4'
    obrabot = 'D:/Чикурова Александра 1-МД-4/pugpug'
    if not os.path.exists(  obrabot):
        os.makedirs(  obrabot)

    imag = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for image_name in imag:
        image = Image.open(os.path.join(nach, image_name))

        image_filtered = image.filter(ImageFilter.CONTOUR)

        new_image_name = 'filtered_' + image_name
        image_filtered.save(os.path.join(obrabot, new_image_name))

    print("Обработка изображений завершена.")
def pug4():
    pyt = 'D:/Чикурова Александра 1-МД-4'
    water = 'D:/Чикурова Александра 1-МД-4/watermark.png'
    obrabotan = 'D:/Чикурова Александра 1-МД-4/gupgup'

    if not os.path.exists(obrabotan ):
        os.makedirs(obrabotan )

    image_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for image_name in image_names:
        image = Image.open(os.path.join(pyt, image_name))

        watermark = Image.open(water)
        size = (100, 100)
        watermark = watermark.resize(size)

        watermark_width, watermark_height = watermark.size

        image_width, image_height = image.size

        wtyt = (image_width - watermark_width, image_height - watermark_height)

        image.paste(watermark, wtyt, watermark)

        new_image_name = 'watermarked_' + image_name
        image.save(os.path.join(obrabotan , new_image_name))
    print("Добавление водяного знака завершено.")
while True:
    print('1. показ картинки')
    print('2. транспортировать')
    print('3. 5 фото')
    print('4. водяной знак')
    print('5. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        pug1()
    elif a == 2:
        pug2()
    elif a == 3:
        pug3()
    elif a == 4:
        pug4()
    elif a == 5:
        break
    else:
        print('Неверное действие')