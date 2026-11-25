import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Logarithmic barrier components creating sharp gradients near boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += -np.log(1.0 - x_scaled[i]**2 + 1e-10) * (1.0 + 0.1 * np.sin(i))
        
        # Spherical harmonics with varying degrees and angular frequencies
        spherical_harmonics = 0.0
        for i in range(1, min(5, self.dim + 1)):
            degree = i
            freq = i * (2.0 + 0.5 * np.cos(i))
            spherical_harmonics += (degree * 0.3) * np.sin(freq * x_scaled[i-1]) * np.cos(freq * x_scaled[i-1])
        
        # Skew-symmetric tensor interactions creating non-linear coupling
        skew_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                skew_interaction += (x_scaled[i] * x_scaled[j] - x_scaled[j] * x_scaled[i]) * np.exp(-0.1 * (i + j))
        
        # Exponentially growing condition number via recursive polynomial terms
        cond_growth = 0.0
        for i in range(self.dim):
            cond_growth += (i + 1) * (x_scaled[i] ** (2 * (i + 1)))
        
        # Chaotic modulation using logistic map-like behavior
        chaotic_modulation = 0.0
        r = 3.8
        for i in range(min(4, self.dim)):
            chaotic_modulation += np.sin(r * x_scaled[i] * (1 - x_scaled[i])) * np.cos(r * x_scaled[i])
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian_peaks = 0.0
        for i in range(min(6, self.dim + 1)):
            peak_height = 1.0 / (i * (1.0 + 0.2 * np.sin(i)))
            peak_width = 0.1 + 0.05 * np.cos(i)
            gaussian_peaks += peak_height * np.exp(-0.5 * ((x_scaled[i-1] - 0.5 * np.sin(i)) / peak_width) ** 2)
        
        # Combine all components with carefully tuned weights
        return barrier + 0.4 * spherical_harmonics + 0.3 * skew_interaction + 0.2 * cond_growth + 0.1 * chaotic_modulation + 0.05 * gaussian_peaks + 0.001 * np.sum(x_scaled**8)