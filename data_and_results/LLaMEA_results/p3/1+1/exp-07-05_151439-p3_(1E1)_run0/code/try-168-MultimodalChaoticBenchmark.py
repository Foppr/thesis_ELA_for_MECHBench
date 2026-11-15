import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with varying rates
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x)) / self.dim
        
        # Trigonometric coupling with adaptive frequencies
        coupling_term = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * 
                              np.sin(2 * np.pi * x * np.cos(np.pi * x)) * 
                              np.cos(2 * np.pi * x * np.sin(np.pi * x))) / self.dim
        
        # Adaptive dimensional scaling with sinusoidal modulation
        scaling_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5)
        scaled_term = np.sum((x**2 + 0.1 * np.sin(self.dim * x)) * scaling_factor) / self.dim
        
        # Multi-scale harmonic interference
        harmonic_term = np.sum(np.sin(5 * x + np.cos(2 * x)) * np.cos(3 * x + np.sin(2 * x)) * 
                              np.sin(7 * x + np.cos(3 * x)) * np.cos(4 * x + np.sin(3 * x))) / self.dim
        
        # Cross-dimensional interaction with exponential weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = np.exp(-0.1 * (i + 1)) * (1 + 0.2 * np.sin(i * 0.7))
                cross_term += weight * np.abs(x[i] - x[i+1])**3
        cross_term /= (self.dim - 1)
        
        # Add noise with adaptive amplitude
        noise = 0.01 * np.random.rand() * (1 + 0.1 * np.sin(self.dim))
        
        # Combine terms with dynamic weights
        weights = [0.35 + 0.05 * np.sin(self.dim * 0.3), 
                  0.25 + 0.05 * np.cos(self.dim * 0.4),
                  0.20 + 0.05 * np.sin(self.dim * 0.5),
                  0.15 + 0.05 * np.cos(self.dim * 0.6),
                  0.05 + 0.05 * np.sin(self.dim * 0.7)]
        
        result = (weights[0] * exp_term + 
                 weights[1] * coupling_term + 
                 weights[2] * scaled_term + 
                 weights[3] * harmonic_term + 
                 weights[4] * cross_term)
        
        return result + noise