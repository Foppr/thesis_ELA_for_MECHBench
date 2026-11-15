import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with varying rates
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.cos(2 * np.pi * x) * np.sin(3 * np.pi * x)) / self.dim
        
        # Trigonometric coupling between dimensions
        coupling_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling_term += np.sin(np.pi * (x[i] + x[i+1])) * np.cos(np.pi * (x[i] - x[i+1]))
        coupling_term /= (self.dim - 1)
        
        # Adaptive noise with dimension-dependent amplitude
        noise_amplitude = 0.1 * (1 + 0.2 * np.sin(self.dim * 0.5))
        noise = np.random.normal(0, noise_amplitude)
        
        # Polynomial modulation with adaptive exponents
        poly_mod = np.sum((1.0 + 0.3 * np.sin(self.dim * 0.7)) * x**4 + 
                         (0.8 + 0.2 * np.cos(self.dim * 0.9)) * x**3 + 
                         (0.6 + 0.1 * np.sin(self.dim * 1.1)) * x**2 + 
                         (0.4 + 0.05 * np.cos(self.dim * 1.3)) * x) / self.dim
        
        # Multi-scale harmonic interference
        harmonic_term = np.sum(np.sin(10 * x + 0.5 * np.sin(self.dim * 0.3)) * 
                              np.cos(8 * x + 0.3 * np.cos(self.dim * 0.6)) * 
                              np.sin(6 * x + 0.2 * np.sin(self.dim * 0.9)) * 
                              np.cos(4 * x + 0.1 * np.cos(self.dim * 1.2))) / self.dim
        
        # Cross-dimensional interaction with dynamic weights
        cross_interaction = 0
        if self.dim > 1:
            for i in range(self.dim):
                weight = 1.5 + 0.5 * np.sin(i * 0.8 + self.dim * 0.4)
                cross_interaction += weight * np.abs(x[i])**1.5
        cross_interaction /= self.dim
        
        # Combine all terms with dynamic scaling
        result = (0.8 * exp_term + 
                 0.6 * coupling_term + 
                 0.4 * poly_mod + 
                 0.5 * harmonic_term + 
                 0.3 * cross_interaction + 
                 0.2 * np.sum(x**2) / self.dim)
        
        return result + noise