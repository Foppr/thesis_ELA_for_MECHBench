import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base with exponential scaling
        f1 = np.sum(np.exp(2 * x_norm**2) - 1)
        
        # High-frequency sine waves with varying amplitudes
        f2 = np.sum((np.sin(5 * np.pi * x_norm) + 0.5 * np.sin(10 * np.pi * x_norm))**2)
        
        # Product of cosine terms with exponential decay
        f3 = np.prod(np.cos(3 * x_norm) * np.exp(-x_norm**2))
        
        # Cross-dimensional interaction with polynomial coupling
        f4 = np.sum((x_norm[:-1]**2) * (x_norm[1:]**3))
        
        # Additional complex interaction term
        f5 = np.sum(np.sin(x_norm[:-2]) * np.cos(x_norm[1:-1]) * np.sin(x_norm[2:]))
        
        # Stochastic perturbation component
        noise = 0.1 * np.random.standard_normal()
        
        return 0.5 * f1 + 0.8 * f2 + 0.3 * f3 + 0.4 * f4 + 0.6 * f5 + noise