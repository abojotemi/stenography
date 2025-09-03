from PIL import Image
import numpy as np


def encode(img1, img2, img_size):
    img1 = Image.open(img1).resize(img_size).convert("RGB")
    img2 = Image.open(img2).resize(img_size).convert("RGB")
    img1_arr = np.array(img1, dtype=np.uint8)
    img2_arr = np.array(img2, dtype=np.uint8)
    new_img = (img1_arr & 0xF0) | (img2_arr >> 4)
    return new_img


def decode(img, img_size):
    img = Image.open(img).resize(img_size)
    img_arr = np.array(img, dtype=np.uint8)
    decode_img = (img_arr & 0xF) << 4

    return decode_img
