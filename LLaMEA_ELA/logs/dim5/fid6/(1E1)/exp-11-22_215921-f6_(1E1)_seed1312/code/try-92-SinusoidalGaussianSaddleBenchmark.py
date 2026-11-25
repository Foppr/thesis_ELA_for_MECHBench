import numpy as np

class SinusoidalGaussianSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal wave component with varying frequencies
        sin_wave = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Gaussian peaks with adaptive positioning and widths
        gaussian_peaks = np.sum(0.5 * np.exp(-2 * (x_norm - 0.3 * np.sin(5 * x_norm))**2) + 
                               0.3 * np.exp(-3 * (x_norm + 0.2 * np.cos(4 * x_norm))**2))
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle = np.sum(np.tanh(2 * x_norm[:-1]) * np.tanh(2 * x_norm[1:]) * 
                       (x_norm[:-1]**2 - x_norm[1:]**2))
        
        # Cross-dimensional coupling with cosine interaction
        coupling = 0.7 * np.sum(np.cos(5 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # High-frequency oscillation component
        high_freq = 0.8 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm))
        
        # Combine all terms with proper weighting
        return condition_factor * (sin_wave + gaussian_peaks + saddle + coupling + high_freq)