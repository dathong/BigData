from PIL import Image
import numpy as np
from scipy import misc


def gen(x, n=5):
    s = ""
    s1 = str(x)
    for i in range(len(s1), n):
        s += '0'
    s += s1
    return s


for c in range(1, 100):
    img1 = misc.imread('/Users/dathong/Downloads/Original/train/im' + gen(c) + '.jpg')
    img2 = misc.imread('/Users/dathong/Downloads/Skin/train/im' + gen(c) + '_s.bmp')

    height, width, d = img1.shape

    k = 3

    Y = np.empty([height, width], dtype=object)

    for h in range(height):
        for w in range(width):
            p = img1[h, w]
            p1 = img2[h, w]
            X = np.empty([2 * k + 1, 2 * k + 1], dtype=object)
            for i in range(2 * k + 1):
                for j in range(2 * k + 1):
                    x = h - k + i
                    y = w - k + j
                    if x < 0 or x >= height: x = h
                    if y < 0 or y >= width: y = w

                    X[i, j] = img1[x, y]
            if p1[0] == 255 and p1[1] == 255 and p1[2] == 255:
                Y[h, w] = (X, 0)
            else:
                Y[h, w] = (X, 1)

    l = []
    l1 = []
    for h in range(height):
        for w in range(width):
            l.append(Y[h, w][0].flatten())
            l1.append(Y[h, w][1])

    print("for c = " + str(c) + " saving files ....")
    np.savetxt("./big_data_files/x" + gen(c) + ".csv", l, fmt='%s', delimiter=' ', newline='\n', )
    np.savetxt("./big_data_files/y" + gen(c) + ".csv", l1, fmt='%s', delimiter=' ', newline='\n', )

print("Done")
