from PIL import Image
class Componts:
    def __init__(self):
        self.lister = tuple()

    def add(self, values):
        self.lister.insert(values)
        pass

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
img.show()