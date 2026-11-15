import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified exponents and amplitudes
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(8 * x) * np.cos(5 * x))
        term3 = 0.2 * np.sum(x**7 * np.sin(4 * x))
        term4 = 0.3 * np.sum(np.exp(-0.3 * x**2) * np.sin(18 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        
        # Enhanced interaction terms between dimensions with modified coupling
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(8 * (x[:-1] + x[1:])))
        
        # Add cross-dimensional polynomial coupling with higher-order terms
        cross_term = 0.06 * np.sum(x[:-1]**2 * x[1:]**2 * np.sin(5 * (x[:-1]**2 + x[1:]**2)))
        
        # Add adaptive exponential decay barriers with different scaling
        barrier = 0.25 * np.sum(np.exp(-1.5 * np.abs(x)) * np.cos(10 * x))
        
        # Add a new chaotic component for increased complexity
        chaotic = 0.15 * np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.exp(-0.1 * x**2))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier + chaotic
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result