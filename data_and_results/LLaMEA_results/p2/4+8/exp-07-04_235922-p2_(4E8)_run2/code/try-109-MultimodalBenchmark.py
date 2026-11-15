import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with higher-order terms
        term1 = np.sum(x**2)
        term2 = 1.2 * np.sum(np.sin(9 * x) * np.cos(5 * x))
        term3 = 0.2 * np.sum(x**8 * np.sin(5 * x))
        term4 = 0.6 * np.sum(np.exp(-0.3 * x**2) * np.sin(20 * x))
        term5 = 0.12 * np.sum(np.abs(x) ** 5.1)
        
        # Enhanced interaction terms between dimensions with cubic coupling
        interaction = 0.05 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(9 * (x[:-1] + x[1:])))
        
        # Novel cross-dimensional polynomial coupling with trigonometric modulation
        cross_term = 0.08 * np.sum(x[:-1] * x[1:] * np.sin(5 * (x[:-1]**3 + x[1:]**3)) * np.cos(3 * (x[:-1] + x[1:])))
        
        # Adaptive exponential decay barriers with multi-scale modulation
        barrier = 0.3 * np.sum(np.exp(-1.5 * np.abs(x)) * np.cos(10 * x) * np.sin(2 * x))
        
        # Additional chaotic modulation with fourth-order polynomial coupling
        chaotic_mod = 0.04 * np.sum((x**4 + x**3) * np.sin(6 * x) * np.cos(3 * x))
        
        # Multi-scale sinusoidal interference
        multiscale = 0.1 * np.sum(np.sin(12 * x) * np.cos(7 * x) * np.sin(4 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier + chaotic_mod + multiscale
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result