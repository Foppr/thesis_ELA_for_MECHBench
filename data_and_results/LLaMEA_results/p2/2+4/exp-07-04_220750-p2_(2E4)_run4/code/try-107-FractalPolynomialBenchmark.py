import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with varying degrees and fractal-like interactions
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x_norm[i]**3 + 0.5 * x_norm[i]**4 + 0.3 * x_norm[i]**5) * np.sin(2 * np.pi * x_norm[i])
        
        # Fractal sinusoidal component with recursive frequency modulation
        fractal_sine = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1) * (1 + 0.2 * np.sin(3 * x_norm[i]))
            fractal_sine += np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi)
        
        # Adaptive conditioning component with exponential scaling
        conditioning = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 2.0 * np.exp(-0.5 * x_norm[i]**2)
            conditioning += condition_factor * x_norm[i]**2
        
        # Cross-dimensional coupling with recursive fractal structure
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin(3 * (x_norm[i] + x_norm[j]))
                cross_coupling += coupling_strength * np.sin(2 * x_norm[i] * x_norm[j]) * np.cos(2 * x_norm[i] * x_norm[j])
        
        # Multimodal component with polynomial interactions and chaotic modulation
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x_norm[i]**6 + 0.8 * x_norm[i]**7 + 0.5 * x_norm[i]**8) * np.cos(4 * x_norm[i] * np.pi)
        
        # Hybrid chaotic component with logistic map and sine modulation
        chaotic_hybrid = 0.0
        for i in range(self.dim):
            logistic_input = 3.8 * x_norm[i] % 1.0
            chaotic_hybrid += np.sin(logistic_input * 8 * np.pi) * np.tanh(2 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combined fitness function with adaptive weights
        return 0.3 * poly_chaos + 0.25 * fractal_sine + 0.2 * conditioning + 0.15 * cross_coupling + 0.05 * multimodal + 0.05 * chaotic_hybrid