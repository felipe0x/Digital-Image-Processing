include("histogram.jl")

using .Hist
using TestImages, Colors, ImageTransformations, Plots

img = testimage("cameraman")
img2 = testimage("bark_512.tiff")

img_resized =  imresize(img, (200, 200))
img_int = round.(Int, Float64.(img_resized) .* 255)

img2_resized =  imresize(img2, (200, 200))
img2_int = round.(Int, Float64.(img2_resized) .* 255)

L = 256

hist = Hist.image_hist(img_int, L)
spec_hist = Hist.image_hist(img2_int, L)

img_eq = Hist.hist_equalization(img_int, hist, L)

eq_hist = Hist.image_hist(img_eq, L)
gz_lut = Hist.create_lut(spec_hist, L)

display(plot(
    plot(img_resized, title="Original"),
    plot(Gray.(img_eq ./ (L-1)), title="Equalizada"),
    bar(hist, title="Histograma", label=""),
    bar(eq_hist, title="Histograma Equalizado", label=""),
    layout=(2,2)
))