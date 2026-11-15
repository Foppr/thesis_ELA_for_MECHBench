import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with increased complexity
        term1 = np.sum(x**2)
        term2 = 1.2 * np.sum(np.sin(9 * x) * np.cos(5 * x))
        term3 = 0.2 * np.sum(x**7 * np.sin(5 * x))
        term4 = 0.6 * np.sum(np.exp(-0.3 * x**2) * np.sin(20 * x))
        term5 = 0.12 * np.sum(np.abs(x) ** 5.0)
        
        # Enhanced interaction terms between dimensions with higher-order coupling
        interaction = 0.05 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(9 * (x[:-1] + x[1:])))
        
        # Add cross-dimensional polynomial coupling with multi-scale interactions
        cross_term = 0.08 * np.sum(x[:-1] * x[1:] * np.sin(6 * (x[:-1]**2 + x[1:]**2)) * np.cos(3 * x[:-1]))
        
        # Add adaptive exponential decay barriers with enhanced modulation
        barrier = 0.3 * np.sum(np.exp(-3 * np.abs(x)) * np.cos(12 * x) * np.sin(2 * x**2))
        
        # Add multi-scale sinusoidal modulation
        modulation = 0.15 * np.sum(np.sin(25 * x) * np.cos(10 * x) * np.exp(-0.1 * x**2))
        
        # Add higher-order polynomial coupling across all dimensions
        poly_coupling = 0.04 * np.sum(np.prod(x.reshape(-1, 1) - x.reshape(1, -1), axis=1) ** 2)
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier + modulation + poly_coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result