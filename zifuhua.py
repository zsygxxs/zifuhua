import os
try:
	from PIL import Image
except Exception:
	os.system("pip install pillow")
import sys


def load():
	file = sys.argv[1]
	image = Image.open(file)
	w,h = image.size
	image_RGB = Image.new('RGB', size=(w,h), color=(255, 255, 255))
	image_RGB.paste(image, (0,0), mask=image)
	image_L = image_RGB.convert('L')
	image_L = image_L.rotate(90)
	return image_L
def gray(pix):
	all = r"""@B%8&amp;WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~&lt;&gt;i!lI;:,"^`' """
	char = all[int(len(all)*pix/256)]
	return char
def main():
	l = load()
	size = l.size
	f = open(sys.argv[2], mode='w')
	for x in range(size[0]):
		for y in range(size[1]):
			f.write(gray(l.getpixel((x, y))))
			f.write(' ')
		f.write('\n')
	f.close()
main()