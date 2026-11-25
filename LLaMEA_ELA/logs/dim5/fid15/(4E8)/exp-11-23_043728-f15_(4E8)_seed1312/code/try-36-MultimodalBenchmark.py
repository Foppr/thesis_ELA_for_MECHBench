import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Enhanced quadratic term with variable scaling
        quadratic_term = np.sum(x_norm**2 * (1 + 0.5 * np.abs(x_norm)))
        
        # Highly oscillatory sinusoidal terms with exponential frequency growth
        freqs = np.exp(np.arange(1, self.dim + 1) * 0.5)
        sin_term = np.sum(np.sin(freqs * x_norm)**4)
        
        # High-order polynomial terms for increased complexity and flat regions
        poly_term = np.sum(x_norm**6) + 0.2 * np.sum(x_norm**8)
        
        # Chaotic coupled interaction terms with nonlinear coupling
        coupling_weights = np.exp(-np.abs(np.arange(self.dim - 1) - (self.dim - 1) / 2) / 5)
        interaction_term = np.sum(coupling_weights * (x_norm[:-1]**2 + x_norm[1:]**2)**2)
        
        # Shifted minima with chaotic positioning
        shift = np.sin(np.arange(self.dim) * np.pi / 3) * 0.3
        shifted_term = np.sum(np.sin(5 * np.pi * (x_norm + shift))**3)
        
        # Additional chaotic cross-dimensional interaction
        cross_term = np.sum(np.sin(x_norm * np.cos(np.arange(self.dim)))**2)
        
        # Combine all terms with dynamic weights
        return (1.0 * quadratic_term + 
                0.8 * sin_term + 
                0.02 * poly_term + 
                0.5 * interaction_term + 
                0.6 * shifted_term + 
                0.3 * cross_term)