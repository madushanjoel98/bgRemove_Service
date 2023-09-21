import base64
from rembg import remove
from PIL import Image
import requests
from datetime import datetime
import io
class BGRemover:
    def __init__(self):
        self.outputpath = "e.png"

    def timeAsString(self):
        today = datetime.now().strftime("%Y%m%d%H%M%S")
        print(today)
        return today

    def removeBg_file(self, filepath):
        input_image = Image.open(filepath)
        output_image = remove(input_image)
        output_image.save(self.outputpath)

    def removeBg_baseTO_base(self, base64w):
        # Decode the base64-encoded image and convert it to bytes
        image_bytes = base64.b64decode(base64w)    
        # Create a PIL Image object from the decoded bytes
        input_image = Image.open(io.BytesIO(image_bytes))
        # Process the image and save the output
        output_image = remove(input_image)
        with io.BytesIO() as buffer:
            output_image.save(buffer, format="PNG")
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
        return image_base64

    def removeBGURL(self, url):
        input_image = Image.open(requests.get(url, stream=True).raw)
        output_image = remove(input_image)
        output_image.save(self.outputpath)

    def removeBGURL_BASE64(self, url):
        input_image = Image.open(requests.get(url, stream=True).raw)
        output_image = remove(input_image)
        # Convert the output image to base64 encoding
        with io.BytesIO() as buffer:
            output_image.save(buffer, format="PNG")
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
        return image_base64



