import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                         np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x)) / self.dim
        
        # Polynomial terms with dynamic exponents based on dimension
        poly_term = np.sum((1.5 + 0.5 * np.sin(self.dim * 0.5)) * x**4 + 
                          (2.0 + 0.3 * np.cos(self.dim * 0.7)) * x**3 + 
                          (1.2 + 0.4 * np.sin(self.dim * 0.9)) * x**2 + 
                          (0.8 + 0.2 * np.cos(self.dim * 1.1)) * x) / self.dim
        
        # Exponential decay with dimension-dependent scaling
        exp_term = np.sum(np.exp(-0.5 * x**2 / (1.0 + 0.1 * self.dim)) * 
                         np.sin(2 * np.pi * x / (1.0 + 0.05 * self.dim))) / self.dim
        
        # Cross-dimensional coupling with dynamic weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 0.5 + 0.3 * np.sin(i * 0.7 + self.dim * 0.3)
                cross_term += weight * np.abs(x[i] - x[i+1]) * np.exp(-0.1 * np.abs(x[i] - x[i+1]))
        cross_term /= (self.dim - 1)
        
        # Multi-modal component with multiple local minima
        modal_term = np.sum(np.sin(10 * x) * np.cos(5 * x) * 
                           (1 + 0.3 * np.sin(self.dim * 0.8)) * 
                           np.exp(-0.1 * x**2)) / self.dim
        
        # Dynamic scaling factor based on dimension
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.6)
        
        # Combine all terms with dynamic weighting
        weights = [0.3 * scale_factor, 0.25 * scale_factor, 0.2 * scale_factor, 0.15 * scale_factor, 0.1 * scale_factor]
        
        result = (weights[0] * sin_term + 
                 weights[1] * poly_term + 
                 weights[2] * exp_term + 
                 weights[3] * modal_term + 
                 weights[4] * cross_term)
        
        # Add small random noise
        noise = 0.001 * np.random.rand()
        
        return result + noise