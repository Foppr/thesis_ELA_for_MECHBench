import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Multi-frequency sinusoidal components
        sin1 = np.sum(np.sin(2 * np.pi * x_norm))
        sin2 = np.sum(np.sin(5 * np.pi * x_norm))
        sin3 = np.sum(np.sin(10 * np.pi * x_norm))
        
        # Polynomial interaction terms
        poly2 = np.sum(x_norm**4)
        poly3 = np.sum(x_norm**3)
        
        # Cross-dimensional interaction with gradient-like behavior
        grad_interaction = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Attraction term that pulls towards specific points
        attraction = np.sum(np.exp(-5 * (x_norm - 0.5)**2) + np.exp(-5 * (x_norm + 0.5)**2))
        
        # Combined nonlinear component
        nonlinear = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Exponential decay with varying rate
        decay = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Add small noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Weighted combination of all terms
        return (0.4 * quadratic + 
                0.3 * (sin1 + sin2 + sin3) + 
                0.1 * (poly2 + poly3) + 
                0.05 * grad_interaction + 
                0.05 * attraction + 
                0.03 * nonlinear + 
                0.02 * decay + 
                noise)