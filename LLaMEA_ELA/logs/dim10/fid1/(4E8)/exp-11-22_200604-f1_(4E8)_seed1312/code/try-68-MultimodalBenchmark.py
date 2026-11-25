import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with random coefficients
        exp_terms = np.sum(np.exp(-np.abs(x_norm)) * np.random.rand(self.dim))
        
        # Gaussian hill clustering with varying centers and widths
        gaussian_hills = 0.0
        for i in range(10):
            center = np.random.uniform(-1, 1, self.dim)
            width = np.random.uniform(0.1, 0.5)
            gaussian_hills += np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Logarithmic barrier terms to prevent boundary crossing
        log_barrier = np.sum(np.log(1.0 + np.abs(x_norm)))
        
        # Multi-scale sinusoidal modulations with varying frequencies
        sin_modulation = 0.0
        for i in range(5):
            freq = np.random.randint(1, 10)
            sin_modulation += np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm)
        
        # Cross-dimensional coupling with polynomial interactions
        poly_coupling = 0.0
        for i in range(self.dim - 1):
            poly_coupling += (x_norm[i] * x_norm[i+1])**3
        
        # Inverse distance weighted potential fields
        inv_distance = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - np.random.rand(self.dim))**2)
            inv_distance += 1.0 / (dist + 1e-8)
        
        # Combine all components with adaptive weights
        result = exp_terms + gaussian_hills * 0.5 + log_barrier * 0.3 + \
                 sin_modulation * 0.2 + poly_coupling * 0.1 + inv_distance * 0.4
        
        return result