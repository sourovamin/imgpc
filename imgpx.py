from PIL import Image
import os

class ImgPx:

    def __init__(self, path = os.getcwd()):
        self.path = path

    def createFolder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def destinationFile(self, source_img, des_folder, des_format = None):
        base_name = os.path.basename(source_img)
        filename = os.path.splitext(base_name)[0]
        extention = os.path.splitext(base_name)[1]
        if des_format is None:
            file_ext = filename + extention
        else:
            file_ext = filename + "." + des_format
        return os.path.join(des_folder, file_ext)

    def saveImage(self, source_img, des_format, des_folder):
        try:
            image = Image.open(source_img)
            new_image = self.destinationFile(source_img, des_folder, des_format)
            image.save(new_image)
        except Exception:
            pass

    def typeConvert(self, des_format, des_folder = "Converted"):
        self.createFolder(des_folder)
        for file in os.listdir(self.path):
            file_path = os.path.join(self.path, file)
            self.saveImage(file_path, des_format, des_folder)

    def resizeImage(self, source_img, width, height, des_folder, aspect_ratio, des_format ):
        try:
            self.createFolder(des_folder)
            size = width, height
            image = Image.open(source_img)
            if aspect_ratio:
                image.thumbnail((width, height), Image.ANTIALIAS)
            else:
                image = image.resize(size)
            new_image =  self.destinationFile(source_img, des_folder, des_format)
            image.save(new_image)
        except Exception:
            pass

    def resize(self, width, height, des_folder = "Resized", aspect_ratio = True, des_format = None):
        self.createFolder(des_folder)
        for file in os.listdir(self.path):
            file_path = os.path.join(self.path, file)
            self.resizeImage(file_path, width, height, des_folder, aspect_ratio, des_format)
