import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like chaotic components with self-similarity
        term1 = np.sum(np.sin(13 * x) * np.cos(7 * x))
        term2 = 0.5 * np.sum(np.sin(23 * x) * np.sin(11 * x))
        term3 = 0.3 * np.sum(np.cos(17 * x) * np.sin(9 * x))
        
        # Polynomial chaos interactions with varying exponents
        term4 = 0.2 * np.sum((x**3 + x**5) * np.sin(5 * x))
        term5 = 0.1 * np.sum((x**4 - x**2) * np.cos(3 * x))
        
        # Dynamic gradient modulation using fractal-like sinusoidal patterns
        grad_mod = np.sum(np.sin(29 * x) * np.cos(13 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale chaotic interference terms
        interference = 0.15 * np.sum(np.sin(37 * x) * np.cos(19 * x) * np.sin(11 * x))
        
        # Adaptive exponential barrier with fractal scaling
        barrier = 0.25 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(25 * x) * np.cos(15 * x))
        
        # Cross-dimensional coupling with fractal scaling
        cross_dim = 0.1 * np.sum(np.sin(13 * (x[:-1] + x[1:])) * np.cos(7 * (x[:-1] - x[1:])))
        
        # Add noise for increased complexity
        noise = 0.001 * np.random.random()
        
        result = term1 + term2 + term3 + term4 + term5 + grad_mod + interference + barrier + cross_dim + noise
        
        return result