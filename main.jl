include("hist_eq.jl")

using .Hist
using TestImages, ImageTransformations, Colors, Plots

img = testimage("cameraman")
img_resized =  imresize(img, (200, 200))
img_int = round.(Int, Float64.(img_resized) .* 255)

display(img_resized)

L = 256

hist = Hist.image_hist(img_int, L)
img_eq = Hist.hist_equalization(img_int, hist, L)
eq_hist = Hist.image_hist(img_eq, L)

display(plot(
    plot(img_resized, title="Original"),
    plot(Gray.(img_eq ./ (L-1)), title="Equalizada"),
    bar(hist, title="Histograma", label=""),
    bar(eq_hist, title="Histograma Equalizado", label=""),
    layout=(2,2)
))