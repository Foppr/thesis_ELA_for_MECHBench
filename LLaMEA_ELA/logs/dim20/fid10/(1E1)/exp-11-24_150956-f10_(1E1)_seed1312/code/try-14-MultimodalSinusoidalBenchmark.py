import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak terms with varying centers and widths
        peaks = 0.0
        centers = np.linspace(-1, 1, 9)
        widths = np.logspace(-2, 0, 9)
        
        for i in range(9):
            peak = np.exp(-0.5 * np.sum(((x_scaled - centers[i]) / widths[i])**2))
            peaks += peak
        
        # Sinusoidal modulation with multiple frequencies
        sin_mod = np.sum(np.sin(10 * x_scaled) + 0.5 * np.sin(20 * x_scaled) + 0.3 * np.sin(30 * x_scaled))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_scaled[i] - x_scaled[i+1])**2 * np.sin(x_scaled[i] * x_scaled[i+1])
        
        # Polynomial and exponential components
        poly_term = np.sum(0.1 * x_scaled**4 + 0.5 * x_scaled**3 + 0.2 * x_scaled**2)
        exp_term = np.sum(np.exp(-x_scaled**2) * np.cos(5 * x_scaled))
        
        # Combine all components
        return 2.0 * peaks + 1.5 * sin_mod + 0.5 * cross_term + 0.3 * poly_term + 0.2 * exp_term + 1.0