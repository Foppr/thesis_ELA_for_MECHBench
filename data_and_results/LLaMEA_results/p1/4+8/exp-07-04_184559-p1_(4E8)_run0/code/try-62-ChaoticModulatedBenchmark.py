import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Multi-frequency sinusoidal modulation
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Enhanced exponential barrier with higher power
        barriers = np.exp(-0.2 * np.sum(np.abs(x_norm)**4))
        
        # Novel chaotic component using piecewise logistic-like behavior
        logistic_like = np.sum(np.sin(np.pi * x_norm) * np.tanh(2 * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Additional ruggedness term with sine-cosine interaction
        ruggedness = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Combine all components with adjusted weights
        return 1.5 * f1 + 1.8 * f2 + 0.7 * barriers + 0.4 * logistic_like + 0.3 * ruggedness