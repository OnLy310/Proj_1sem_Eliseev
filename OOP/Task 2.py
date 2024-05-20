#


class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution

    def title_upped(self):
        self.title = self.title.upper()

image1 = Image('2048*1080', 'kartinka', '.png')
image2 = Image('800*600', 'kartinka2', '.jpeg')

print(image1.__dict__)
print(image2.__dict__)

image1.resize('Full HD')
image2.resize('700*500')

print(image1.__dict__)
print(image2.__dict__)

image1.title_upped()
print(image1.__dict__)
