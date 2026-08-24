import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial conditioning term
        poly_term = np.sum(x_scaled**6 - 3*x_scaled**4 + 2*x_scaled**2)
        
        # Nested hyperbolic tangent oscillations
        tanh_term = np.sum(np.tanh(5 * x_scaled) * np.tanh(3 * x_scaled))
        
        # Adaptive Gaussian peaks with varying heights and widths
        gaussian_peaks = 0
        for i in range(1, 6):
            peak_height = 1.0 / i
            peak_width = 0.5 / i
            peak_center = np.sin(i * np.pi / 6) * 0.8
            gaussian_peaks += peak_height * np.exp(-((x_scaled - peak_center)**2) / (2 * peak_width**2))
        
        # Combined function with adaptive weights
        return 0.4 * poly_term + 0.3 * tanh_term + 0.3 * gaussian_peaks