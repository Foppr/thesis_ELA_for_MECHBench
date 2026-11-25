import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine terms with exponential frequency growth
        f2 = np.sum(np.sin(2**(np.arange(self.dim)) * np.pi * x_norm)**2)
        
        # Nested cosine product with diminishing frequencies
        f3 = np.prod(np.cos(2 * x_norm * np.linspace(1, 0.1, self.dim)))
        
        # Polynomial interaction term between adjacent dimensions with exponential weights
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**2 * np.exp(-np.arange(self.dim-1)))
        
        # Modified Rosenbrock-like term with chaotic coupling
        f5 = np.sum((x_norm[:-1]**2 - x_norm[1:])**2 * np.sin(np.pi * x_norm[:-1]))
        
        # Fractal-like harmonic interaction with cubic terms and self-similarity
        f6 = np.sum(x_norm**3 * np.sin(3 * np.pi * x_norm) * np.cos(0.5 * np.pi * x_norm))
        
        # Cubic polynomial interaction with chaotic phase shifts
        f7 = np.sum((x_norm[:-1] ** 3 - x_norm[1:] ** 3) ** 2 * np.sin(np.pi * (x_norm[:-1] + x_norm[1:])**2))
        
        # Additional chaotic coupling between all dimensions
        f8 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-np.abs(x_norm)))
        
        # Add fractal-like noise pattern
        noise = 0.01 * np.random.random() * np.prod(np.sin(np.pi * x_norm / 2))
        
        return 0.5 * f1 + 1.2 * f2 + 0.3 * f3 + 0.6 * f4 + 0.8 * f5 + 0.4 * f6 + 0.3 * f7 + 0.2 * f8 + noise