from typing import List

from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

image = Image.open('zaba.png')  # wczytanie obrazka (format obojętny)
data = np.asarray(image)  # zamiana obrazka na tablicę numpy
print(data.shape)  # np. (128, 128, 3), lub (128, 128, 4) jeśli jest alpha


class Transform:
    @staticmethod
    def transform(img: Image) -> Image:
        pass


class CropTransform(Transform):
    @staticmethod
    def transform(img: Image) -> Image:
        crop = Image.open(img)
        width, height = crop.size
        left = width / 4
        top = height / 4
        right = 3 * width / 4
        bottom = 3 * height / 4
        cropped = crop.crop((left, top, right, bottom))
        return cropped

class BrightenTransform(Transform):
    @staticmethod
    def transform(img: Image) -> Image:
        brighter = Image.open(img)
        enhance = ImageEnhance.Brightness(brighter)

        factor = 1.5
        brighter_final = enhance.enhance((factor))
        return brighter_final


class BlackWhiteTransform(Transform):
    @staticmethod
    def transform(img: Image) -> Image:
        dark = Image.open(img)
        dark = dark.convert("L")
        return dark


class Transformer:
    transforms: List[Transform]

    # @staticmethod
    # def batch_transforms(images: List[Image]) -> List[Image]:
    #     pass


img1 = Image.fromarray(data, 'RGB')  # lub 'RGBA' jeśli jest alpha, lub pominąć jeśli jest czarno-biały
img1.show()

img2 = BlackWhiteTransform.transform("zaba.png")
img2.show()