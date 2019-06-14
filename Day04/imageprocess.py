# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:05:19 2019

@author: ANISHKA
"""

# Code Challenge : Image Processing using PIL

from PIL import Image
import os

img = Image.open('sample.jpg').convert('L')
img.save('greyscale.png')

img_rotate=img.transpose(Image.ROTATE_90)
crop_im = img.crop(box=(80, 120, 160, 240))
img.thumbnail((75, 75))
print(img.width, img.height)
img.show()
