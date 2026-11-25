import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure
        fractal_term = 0.0
        for i in range(self.dim):
            # Hierarchical sinusoidal pattern with varying frequencies
            freq = 2 ** (i % 4 + 1)
            fractal_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5) * \
                           np.exp(-0.1 * abs(x_norm[i]))
        
        # Power-law interaction terms with multiple scaling exponents
        power_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_norm[i] - x_norm[j])
                # Multiple power-law interactions with different exponents
                power_term += (dist ** 1.5 + dist ** 2.5 + dist ** 3.5) * \
                             np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
        
        # Nested optimization basins with varying depths
        basin_term = 0.0
        for i in range(self.dim):
            # Create nested structure using multiple sinusoidal components
            basin_term += (np.sin(2 * np.pi * x_norm[i]) ** 2 + 
                          0.5 * np.sin(4 * np.pi * x_norm[i]) ** 2 +
                          0.25 * np.sin(8 * np.pi * x_norm[i]) ** 2) * \
                         (1 + 0.1 * x_norm[i]**2)
        
        # Cross-dimensional coupling with fractal scaling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with scaling factor
                scale_factor = 1.0 / (1.0 + abs(i - j) * 0.1)
                coupling_term += scale_factor * np.sin(3 * (x_norm[i] + x_norm[j])) * \
                               np.cos(2 * (x_norm[i] - x_norm[j]))
        
        # Combine all terms with adaptive weights
        result = 0.3 * np.sum(x_norm**4) + 0.4 * fractal_term + 0.3 * power_term + \
                 0.5 * basin_term + 0.2 * coupling_term
        
        return result