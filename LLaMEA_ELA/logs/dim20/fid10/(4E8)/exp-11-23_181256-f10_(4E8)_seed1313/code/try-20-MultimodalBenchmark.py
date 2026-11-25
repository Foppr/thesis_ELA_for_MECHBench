import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic_term = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with exponential scaling
        freq_scale = np.exp(np.arange(1, self.dim + 1) * 0.5)
        sinusoidal_term = np.sum(np.sin(freq_scale * np.pi * x_norm) ** 2)
        
        # Polynomial coupling between dimensions
        poly_coupling = np.sum((x_norm[:-1] * x_norm[1:]) ** 4)
        
        # Exponentially decaying Gaussian-like terms for additional local minima
        gaussian_term = np.sum(np.exp(-5.0 * (x_norm**2)) * np.cos(10.0 * np.pi * x_norm))
        
        # Combine all terms to create a highly complex landscape
        return 0.5 * quadratic_term + 0.3 * sinusoidal_term + 0.1 * poly_coupling - 0.02 * gaussian_term