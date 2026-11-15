import numpy as np

class FractalDeceptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like self-similar structure using sine waves with diminishing amplitudes
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = 2 ** i
            fractal += (1.0 / freq) * np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm)
        
        # Deceptive multimodal component with overlapping basins
        deceptive = 0.0
        for i in range(self.dim):
            # Create overlapping deceptive valleys
            valley1 = np.sin(5 * np.pi * x_norm[i]) ** 2
            valley2 = np.cos(3 * np.pi * x_norm[i]) ** 2
            deceptive += valley1 * valley2
        
        # Parameter dependency component with exponential interaction
        param_dep = 0.0
        for i in range(self.dim - 1):
            param_dep += np.exp(-np.abs(x_norm[i] - x_norm[i+1])) * np.sin(10 * (x_norm[i] + x_norm[i+1]))
        
        # High-frequency oscillation with amplitude modulation
        high_freq = np.sum(np.sin(50 * x_norm) * np.cos(30 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.8 * fractal + 1.2 * deceptive + 0.9 * param_dep + 1.5 * high_freq