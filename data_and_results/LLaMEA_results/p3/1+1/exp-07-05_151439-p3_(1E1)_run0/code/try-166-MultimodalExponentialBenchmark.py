import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with adaptive scaling
        exp_term = np.sum(np.exp(-np.abs(x) / (1.5 + 0.5 * np.sin(self.dim * 0.7))) * 
                         np.cos(2.1 * x + 0.3 * np.sin(self.dim * 1.2)) * 
                         np.sin(1.8 * x + 0.4 * np.cos(self.dim * 1.5)) * 
                         np.cos(1.2 * x + 0.2 * np.sin(self.dim * 1.8))) / self.dim
        
        # Trigonometric coupling with dynamic phase shifts
        coupling_term = np.sum(np.sin(3.2 * x + 0.5 * np.cos(self.dim * 0.9)) * 
                              np.cos(2.7 * x + 0.4 * np.sin(self.dim * 1.1)) * 
                              np.sin(1.9 * x + 0.3 * np.cos(self.dim * 1.3)) * 
                              np.cos(1.4 * x + 0.2 * np.sin(self.dim * 1.6)) * 
                              np.sin(1.1 * x + 0.1 * np.cos(self.dim * 1.9))) / self.dim
        
        # Adaptive dimensional scaling with polynomial modulation
        scale_term = np.sum((1.0 + 0.3 * np.sin(self.dim * 0.5)) * x**4 + 
                           (0.8 + 0.2 * np.cos(self.dim * 0.8)) * x**3 + 
                           (0.6 + 0.1 * np.sin(self.dim * 1.0)) * x**2 + 
                           (0.4 + 0.05 * np.cos(self.dim * 1.2)) * x) / self.dim
        
        # Cross-dimensional interaction with variable coupling strength
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling_strength = 0.7 + 0.3 * np.sin(i * 0.8 + self.dim * 0.6)
                cross_term += coupling_strength * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        cross_term /= (self.dim - 1)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multi_scale_term = np.sum(np.sin(5.0 * x + 0.2 * np.sin(self.dim * 0.4)) * 
                                 np.cos(3.5 * x + 0.15 * np.cos(self.dim * 0.6)) * 
                                 np.sin(2.0 * x + 0.1 * np.sin(self.dim * 0.8)) * 
                                 np.cos(1.5 * x + 0.05 * np.cos(self.dim * 1.0))) / self.dim
        
        # Add noise component
        noise = 0.01 * np.random.rand()
        
        # Combine all terms with adaptive weights
        weights = [0.25 + 0.05 * np.sin(self.dim * 0.3),
                  0.20 + 0.04 * np.cos(self.dim * 0.5),
                  0.25 + 0.05 * np.sin(self.dim * 0.7),
                  0.15 + 0.03 * np.cos(self.dim * 0.9),
                  0.15 + 0.03 * np.sin(self.dim * 1.1)]
        
        result = (weights[0] * exp_term + 
                 weights[1] * coupling_term + 
                 weights[2] * scale_term + 
                 weights[3] * cross_term + 
                 weights[4] * multi_scale_term)
        
        return result + noise