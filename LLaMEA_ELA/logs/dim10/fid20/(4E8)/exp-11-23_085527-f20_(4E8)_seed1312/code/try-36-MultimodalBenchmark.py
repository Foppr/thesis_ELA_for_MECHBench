import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_scaled**2)
        
        # Exponentially decaying harmonic terms with varying frequencies
        harmonics = 0.0
        for i in range(1, self.dim + 1):
            freq = i * 4 * np.pi
            decay = np.exp(-0.05 * i)
            harmonics += decay * np.sin(freq * x_scaled[i-1])**2
        
        # Add Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        for i in range(1, min(6, self.dim + 1)):
            peak_height = i * 2.0
            peak_width = 0.5 / (i * 0.5 + 1)
            peak_center = np.sin(i) * 0.8
            gaussian_peaks += peak_height * np.exp(-0.5 * ((x_scaled[i-1] - peak_center) / peak_width)**2)
        
        # Non-separable cross-terms for increased complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.3 * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j)
        
        # Adaptive conditioning with higher-order terms
        conditioning = 0.3 * (self.dim - 1) * np.sum(np.abs(x_scaled)**4)
        
        # Combine all components
        return quadratic + 15 * harmonics + gaussian_peaks + cross_terms + conditioning