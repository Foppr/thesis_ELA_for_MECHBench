import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-frequency chaotic sinusoidal components with varying amplitudes
        freqs = [2, 3, 5, 7, 11, 13, 17, 19]
        sin_term = 0
        for i, freq in enumerate(freqs):
            sin_term += (i + 1) * np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm)
        
        # Radial complexity with multiple concentric peaks and valleys
        radius = np.sqrt(np.sum(x_norm**2))
        radial_term = np.sin(10 * radius) * np.exp(-radius**2) + 0.5 * np.cos(5 * radius)
        
        # Multi-scale quadratic penalty with directional bias
        quad_penalty = np.sum((x_norm**2) * (1 + 0.5 * np.sin(3 * np.pi * x_norm)))
        
        # Exponential coupling with chaotic phase shifts
        exp_term = np.sum(np.exp(-5 * x_norm**2) * np.sin(3 * np.pi * x_norm + np.pi * radius))
        
        # Cross-dimensional coupling with non-linear interaction terms
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_term += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Add a global scaling factor to increase landscape complexity
        return 2.0 * sin_term + 0.3 * radial_term + 0.8 * quad_penalty + 0.2 * exp_term + 0.1 * cross_term