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

    for i in range(0, L):
        cdf += pr[i]
        val = (L - 1) * cdf
        lut[i] = round(val)

    return lut

def equalization(img, pr, L):
    lut = create_lut(pr, L)
    new_img = np.zeros()

    function equalization(img::Matrix{Int}, pr::Vector{Float64}, L::Int)
        lut = create_lut(pr, L)
        new_img = zeros(Int, size(img))

        for i in eachindex(img)
            val = img[i]
            new_img[i] = lut[val + 1]
        end

        return new_img
    end

    function lut_matching(G::Vector{Int}, s::Vector{Int})
        L = length(s)
        z_lut = zeros(Int, L)

        for k in 1:L
            diff_min = Inf
            z = 1

            for q in 1:L
                diff = abs(G[q] - s[k])

                if diff < diff_min
                    z = q - 1
                    diff_min = diff
                end
            end

            z_lut[k] = z
        end

        return z_lut
    end

    function matching(img::Matrix{Int}, G::Vector{Int}, s::Vector{Int})
        new_img = zeros(Int, size(img))
        z_lut = lut_matching(G, s)
        L = length(z_lut)

        for i in eachindex(img)
            val = img[i]
            new_img[i] = z_lut[val + 1]
        end

        return new_img
    end