from PIL import Image
import numpy as np
# with Image.open("landscape.jpg") as im:
with Image.open("landscape.jpg") as im:
    # im.rotate(45).show()
    widh, height = im.size
    print("The shape of image is:",(height, widh , im.mode))
    a = np.zeros((5, 5))
    iim = Image.fromarray(a)
    first= np.asarray(im)[0][0:3]
    last = np.asarray(im)[-1][-3:]
    print(type(first))