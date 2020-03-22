from PIL import Image
import os

class ImgPx:

    def __init__(self, path = os.getcwd()):
        self.path = path

    def createFolder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def destinationFile(self, source_img, des_format, des_folder):
        base_name = os.path.basename(source_img)
        filename = os.path.splitext(base_name)[0]
        file_ext = filename + "." + des_format
        return os.path.join(des_folder, file_ext)

    def saveImage(self, source_img, des_format, des_folder):
        try:
            self.createFolder(des_folder)
            image = Image.open(source_img)
            new_image = self.destinationFile(source_img, des_format, des_folder)
            image.save(new_image)
        except Exception:
            pass

    def typeConvert(self, des_format, des_folder = "Converted"):
        self.createFolder(des_folder)
        for file in os.listdir(self.path):
            file_path = os.path.join(self.path, file)
            self.saveImage(file_path, des_format, des_folder)
            #print(file_path)

    def test(self):
        print(self.path)