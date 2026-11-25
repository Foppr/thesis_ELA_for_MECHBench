import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with exponential scaling
        freq_scaler = np.arange(1, self.dim + 1)
        sinusoidal_term = np.sum(np.sin(freq_scaler * np.pi * x_norm) ** 2 * np.exp(freq_scaler))
        
        # Polynomial barrier terms creating narrow valleys
        polynomial_barrier = np.sum((x_norm**4 - 2*x_norm**2 + 1)**2)
        
        # Global dependency through product of transformed variables
        global_dep = np.prod(np.sin(0.3 * np.pi * x_norm) + 0.5)
        
        # Additional complex interaction term
        interaction_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Combine all terms with varying weights to create a challenging landscape
        return quadratic_term + 0.2 * sinusoidal_term + 0.15 * polynomial_barrier - 0.1 * global_dep + 0.05 * interaction_term