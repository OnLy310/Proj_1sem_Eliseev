# 1. Создайте класс Image
#
# 2. У каждого экземпляра класса должно быть три собственных атрибута
# -resolution
# -title
# -extension
#
# 3. В классе должен быть метод resize, с помощью которого можно поменять разрешение изображения.
#
# 4*. В классе должен быть метод title_upper, с помощью которого можно имя файла записать в верхнем регистре.
#
# 5. Создать несколько экземпляров класса Image и вызовите для каждого метод resize


class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution

    def title_upped(self):
        self.title = self.title.upper()


image1 = Image('4k', 'helloworld', '.jpg')
image2 = Image('1080p', 'imagecool', '.png')


print(image1.__dict__)
print(image2.__dict__)

image1.resize('1080p')
image2.resize('4k')

print(image1.__dict__)
print(image2.__dict__)

image1.title_upped()
print(image1.__dict__)
