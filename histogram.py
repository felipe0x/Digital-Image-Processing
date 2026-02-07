import numpy as np
import matplotlib.pyplot as plt

def image_hist(img, L):
    hist = np.zeros(L)

    for pixel in img:
        hist[pixel] += 1

    norm_hist = hist / len(img)

    return norm_hist

def create_lut(pr, L):
    lut = np.zeros(L)
    cdf = 0.0

    for i in range(L):
        cdf += pr[i]
        val = (L - 1) * cdf
        lut[i] = round(val)

    return lut

def equalization(img, pr, L):
    lut = create_lut(pr, L)
    new_img = np.zeros(img.size)

    for i, j in np.ndindex(img.shape):
        val = img[i, j]
        new_img[i, j] = lut[val] 
    
    return new_img

def lut_matching(G, s):
    L = len(s)
    z_lut = np.zeros(L)

    for k in range(L):
        diff_min = np.inf
        z = 0

        for q in range(L):
            diff = np.abs(G[q] - s[k])

            if diff < diff_min:
                z = q
                diff_min = diff

        z_lut[k] = z

    return z_lut

    def matching(img, G, s):
        new_img = np.zeros(img.shape)
        z_lut = lut_matching(G, s)
        L = len(z_lut)

        for i, j in np.ndindex(img.shape):
            val = img[i, j]
            new_img[i, j] = z_lut[val]

        return new_img