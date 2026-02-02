module Hist

    using LinearAlgebra, ImageTransformations

    function image_hist(img::Matrix{Int}, L::Int)
        hist = zeros(Int, L)

        for pixel in img
            hist[pixel + 1] += 1
        end

        norm_hist = hist / length(img)
    
        return norm_hist
    end

    function create_lut(pr::Vector{Float64}, L::Int)
        lut = zeros(Int, L)
        cdf = 0.0

        for i in 1:L
            cdf += pr[i]
            val = (L - 1) * cdf
            lut[i] = round(Int, val)
        end

        return lut
    end

    function hist_equalization(img::Matrix{Int}, pr::Vector{Float64}, L::Int)
        lut = create_lut(pr, L)
        new_img = zeros(Int, size(img))

        for i in eachindex(img)
            val = img[i]
            new_img[i] = lut[val + 1]
        end

        return new_img
    end

    function eq_to_spec_mapping(gz_lut::Vector{Int}, s_lut::Vector{Int})
        z_lut = zeros(Int, L)

        for i in 1:size(s_lut)
            
        end
    end
end

