from PIL import Image
from random import *
import os
# by default windows terminal -> 30 x 120
def scatter_weights(n):
    if n == 1:
        return [0.0]
    return [i / (n - 1) for i in range(n)]

def find_weight(n):
    left, right = 0, len(weights) - 1
    if n <= weights[left]:
        return left
    if n >= weights[right]:
        return right

    while left <= right:
        mid = (left + right) // 2
        if weights[mid] == n:
            return mid
        elif weights[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    if (weights[left] - n) < (n - weights[right]):
        return left
    else:
        return right

def shrink(img, max_width=120, max_height=30, aspect_correction=0.55):
    original_width, original_height = img.size
    adjusted_height = int(original_height * aspect_correction)
    scale_w = max_width / original_width
    scale_h = max_height / adjusted_height
    scale = min(scale_w, scale_h)

    new_width = int(original_width * scale)
    new_height = int(original_height * scale * aspect_correction)

    return img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)

def rgb_color(r, g, b):
    return f'\033[38;2;{r};{g};{b}m' # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def textify(img: Image):
    img = shrink(img).convert("RGB")
    pixels = img.load()
    width, height = img.size
    text = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r_norm = r / 255.0
            g_norm = g / 255.0
            b_norm = b / 255.0
            density = 0.2126 * r_norm + 0.7152 * g_norm + 0.0722 * b_norm
            char = charset[find_weight(density)]
            color = rgb_color(r, g, b)
            text += color + char + '\033[0m'
        text += '\n'

    return text

charset =  " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"[::-1]
weights = scatter_weights(len(charset))

