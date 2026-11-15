import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with higher-order terms
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(9 * x) * np.cos(5 * x) * np.exp(-0.1 * np.abs(x)))
        term3 = 0.2 * np.sum(x**7 * np.sin(4 * x) * np.cos(2 * x))
        term4 = 0.5 * np.sum(np.exp(-0.3 * x**2) * np.sin(18 * x) * np.cos(6 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        
        # Enhanced interaction terms between dimensions with multi-scale modulation
        interaction = 0.05 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(9 * (x[:-1] + x[1:])) * np.cos(3 * (x[:-1] - x[1:])))
        
        # Cross-dimensional polynomial coupling with adaptive scaling
        cross_term = 0.08 * np.sum(x[:-1] * x[1:] * np.sin(5 * (x[:-1]**2 + x[1:]**2)) * np.cos(2 * (x[:-1] * x[1:])))
        
        # Adaptive exponential decay barriers with multi-scale sinusoidal modulation
        barrier = 0.25 * np.sum(np.exp(-1.5 * np.abs(x)) * np.cos(10 * x) * np.sin(5 * x))
        
        # Novel multi-scale sinusoidal modulation term
        modulation = 0.15 * np.sum(np.sin(12 * x) * np.cos(8 * x) * np.sin(3 * x**2))
        
        # Additional chaotic component with polynomial coupling
        chaotic = 0.1 * np.sum(np.exp(-0.5 * x**4) * np.sin(20 * x) * np.cos(7 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier + modulation + chaotic
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result