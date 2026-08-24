import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components
        term1 = np.sum(x**2)
        term2 = 0.8 * np.sum(np.sin(7 * x) * np.cos(4 * x))
        term3 = 0.15 * np.sum(x**6 * np.sin(3 * x))
        term4 = 0.4 * np.sum(np.exp(-0.5 * x**2) * np.sin(15 * x))
        term5 = 0.08 * np.sum(np.abs(x) ** 4.2)
        
        # Enhanced interaction terms between dimensions
        interaction = 0.03 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(7 * (x[:-1] + x[1:])))
        
        # Add cross-dimensional polynomial coupling
        cross_term = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(4 * (x[:-1]**2 + x[1:]**2)))
        
        # Add adaptive exponential decay barriers
        barrier = 0.2 * np.sum(np.exp(-2 * np.abs(x)) * np.cos(8 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result