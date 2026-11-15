import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like self-similar structure using recursive polynomial mapping
        fractal = np.sum(np.power(np.abs(x_norm), 3.2) * np.sin(np.pi * np.abs(x_norm)) + 
                         np.power(np.abs(x_norm), 2.8) * np.cos(np.pi * np.abs(x_norm)) * 
                         np.exp(-2 * np.abs(x_norm)))
        
        # Adaptive polynomial chaos with dimension-dependent exponents
        poly_chaos = 0
        for i in range(self.dim):
            poly_chaos += np.sum((x_norm[i] ** (5 + i % 3) - 3 * x_norm[i] ** (3 + i % 2) + 
                                2 * x_norm[i] ** (2 + i % 4)) ** 2)
        
        # Dynamic gradient field component with varying spatial frequency
        gradient_field = 0
        for i in range(self.dim):
            freq = 10 + i * 2
            gradient_field += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Multi-scale Gaussian peaks with fractal-like spacing
        peaks = 0
        scales = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0]
        for scale in scales:
            for i in range(self.dim):
                center = np.full(self.dim, scale * np.sin(i * np.pi / 3))
                peaks += np.exp(-20 * np.sum((x_norm - center)**2)) * (1 + 0.5 * np.sin(5 * i))
        
        # Cross-dimensional coupling with non-linear interaction terms
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] * x_norm[i+1] * np.sin(15 * x_norm[i] + 10 * x_norm[i+1])) ** 2
        
        # Time-varying harmonic component with chaotic phase modulation
        time_component = np.sum(np.sin(20 * x_norm + np.sin(5 * x_norm)) * 
                               np.cos(15 * x_norm + np.cos(3 * x_norm)) * 
                               np.exp(-0.3 * np.abs(x_norm)))
        
        # Combine all components with dynamic weighting based on input magnitude
        magnitude = np.sum(np.abs(x_norm))
        weights = [0.25 + 0.05 * np.sin(magnitude), 
                   0.30 + 0.03 * np.cos(magnitude),
                   0.20 + 0.02 * np.sin(2 * magnitude),
                   0.15 + 0.04 * np.cos(2 * magnitude),
                   0.10 + 0.01 * np.sin(3 * magnitude)]
        
        result = (weights[0] * fractal + 
                 weights[1] * poly_chaos + 
                 weights[2] * gradient_field + 
                 weights[3] * peaks + 
                 weights[4] * coupling + 
                 0.05 * time_component)
        
        # Add controlled dynamic noise
        noise = 0.02 * (1 + 0.3 * np.sin(np.sum(x_norm**3))) * np.random.normal(0, 0.5)
        
        return result + noise