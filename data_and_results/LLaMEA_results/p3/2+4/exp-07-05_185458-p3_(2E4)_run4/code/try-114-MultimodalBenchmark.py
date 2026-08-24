import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Dynamic Gaussian peaks with sinusoidally shifted centers
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 4.0) * 0.9
            sigma = 0.3 + 0.2 * np.cos(i * np.pi / 3.0)
            gaussian += np.exp(-0.5 * ((x_norm[i] - center) / sigma)**2) * np.cos(10 * (x_norm[i] - center))
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * np.pi / 5.0)
            amp = 1.0 + 0.5 * np.cos(i * np.pi / 2.0)
            sin_component += amp * np.sin(freq * x_norm[i] + np.cos(freq * x_norm[i]))
        
        # Polynomial chaos with cross-dimensional coupling
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x_norm[i]**4 + 0.3 * x_norm[i]**6) * np.sin(x_norm[(i+1) % self.dim])
        
        # Cross-dimensional interaction with exponential modulation
        cross_exp = 0.0
        for i in range(self.dim - 1):
            cross_exp += np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2) * np.cos(5 * x_norm[i] * x_norm[i+1])
        
        # Additional chaotic modulation using logistic map
        logistic_mod = 0.0
        r = 3.9
        for i in range(self.dim):
            logistic_mod += np.sin(2 * np.pi * (r * x_norm[i] * (1 - x_norm[i]) + 0.1 * np.sin(i)))
        
        # Combine all components with different weights
        return 0.6 * gaussian + 0.5 * sin_component + 0.4 * poly_chaos + 0.3 * cross_exp + 0.2 * logistic_mod + 0.03 * np.sum(x_norm**2)