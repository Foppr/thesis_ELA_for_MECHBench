import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base sinusoidal valley term
        result = np.sum(np.sin(0.5 * x) ** 2)
        
        # Add multiple Gaussian peaks with varying heights and widths
        peak_heights = [2.0, 3.5, 1.8, 4.2, 2.7]
        peak_widths = [0.8, 1.2, 0.6, 1.0, 0.9]
        peak_positions = [
            np.array([2.0, -1.5, 0.5, -3.0, 1.0][:self.dim]),
            np.array([-2.5, 1.0, -1.2, 2.8, -0.8][:self.dim]),
            np.array([1.5, 2.2, -2.0, 0.7, 3.1][:self.dim]),
            np.array([-1.8, -2.5, 1.9, -0.6, 2.4][:self.dim]),
            np.array([0.9, -0.8, 2.6, -2.1, 1.3][:self.dim])
        ]
        
        for i in range(min(5, len(peak_heights))):
            peak_pos = peak_positions[i]
            width = peak_widths[i]
            height = peak_heights[i]
            gaussian_term = height * np.exp(-0.5 * np.sum(((x - peak_pos) / width) ** 2))
            result += gaussian_term
        
        # Add coupling terms between dimensions to increase interdependence
        coupling_strength = 0.3
        for i in range(self.dim - 1):
            result += coupling_strength * np.sin(x[i]) * np.cos(x[i+1])
        
        # Add a global minimum at the origin with additional noise
        result += 0.1 * np.sum(x**4) + 0.05 * np.sum(np.sin(20 * x))
        
        return result