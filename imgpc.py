from imgpx import *
import argparse as ag

parser = ag.ArgumentParser()
parser.add_argument("-d", "--dir", help="Directory containing images", type=str)
parser.add_argument("-a", "--act", help="Action to take for image processing", type=str)
parser.add_argument("-f", "--format", help="Target format of the images", type=str)
parser.add_argument("-df", "--destination", help="Destination directory of the processes images", type=str)
parser.add_argument("-w", "--width", help="Maximum width", type=int)
parser.add_argument("-ht", "--height", help="Maximum height", type=int)
parser.add_argument("-fx", "--fixed", help="Keep the aspect ratio", type=bool)
parser.add_argument("-s", "--size", help="Maximum image size in bytes", type=int)

args = parser.parse_args()
directory = args.dir
action = args.act
des_format = args.format
destination = args.destination
width = args.width
height = args.height
fixed_size = args.fixed
size = args.size

img = ImgPx() if directory is None else ImgPx(directory)

if action == "convert":
    if destination is None:
        img.typeConvert(des_format)
    else:
        img.typeConvert(des_format, destination)

elif action == "resize":
    aspect_ratio = True if fixed_size is None else False
    if destination is None:
        img.resize(width, height, aspect_ratio, des_format)
    else:
        img.resize(width, height, aspect_ratio, des_format, destination)

elif action == "sizeup":
    if destination is None:
        img.resizeBySize(size)
    else:
        img.resizeBySize(size, destination)

else:
    print("Action is not recognised!")