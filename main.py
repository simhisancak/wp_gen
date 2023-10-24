import argparse
from PIL import Image
import os.path

def put_center(size, color, img_path, out_path):
    im2 = Image.open(img_path)
    if not color:
        color = im2.getpixel((0, 0))
    im1 = Image.new("RGB" ,size , color=color)
    im1_width, im1_height = im1.size
    im2_width, im2_height = im2.size
    back_im = im1.copy()
    back_im.paste(im2, (int((im1_width/2)-(im2_width/2)), int((im1_height/2)-(im2_height/2))))
    back_im.save(out_path + '.jpg', quality=100)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path', type=str)
    parser.add_argument('--size', '-s', help='size', type=str)
    parser.add_argument('--color', '-c', help='color', type=str)
    parser.add_argument('--out_path', '-o', help='out_path', type=str)
    args = parser.parse_args()

    path = args.path
    size = (1920, 1080)
    color = None
    out_path = 'output'

    if not os.path.isfile(args.path):
        raise Exception('File not exist or wrong path')

    if args.size:
        pos = args.size.find('x')
        if pos == -1 :
            raise Exception('Wrong size arg')
        size = (int(args.size[:pos]), int(args.size[pos+1:]))
   

    if args.color:
        color_len = len(args.color)
        if args.color.find('#') == -1:
            args.color = '#' + args.color
        else:
            color_len -= 1

        if color_len < 3 or color_len > 6:
            raise Exception('Wrong hex color len')
        color = args.color

    if args.out_path:
        if args.out_path.find('.') != -1:
            raise Exception('.')
        out_path = args.out_path

    put_center(size, color, path, out_path)

    



