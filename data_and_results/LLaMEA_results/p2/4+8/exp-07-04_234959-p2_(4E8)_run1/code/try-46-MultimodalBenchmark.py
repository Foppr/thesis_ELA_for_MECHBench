import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal terms with varying amplitudes
        f2 = np.sum(np.sin(20.0 * x) * np.cos(7.0 * x))
        
        # Additional cosine interactions to create more complex landscape
        f3 = np.sum(np.cos(15.0 * x) * np.sin(4.0 * x))
        
        # Exponential decay terms with adaptive scaling
        f4 = np.sum(np.exp(-0.15 * x**2) * np.sin(8.0 * x))
        
        # Cubic polynomial interactions to increase complexity
        f5 = np.sum(x**3 * np.sin(3.0 * x))
        
        # Quartic polynomial interactions for higher-order complexity
        f6 = np.sum(x**4 * np.cos(2.0 * x))
        
        # Shifted global minimum to increase challenge
        shift = np.ones(self.dim) * 1.5
        f7 = np.sum((x - shift)**2)
        
        # Dynamic weighting based on dimensionality
        weights = np.array([0.12, 0.22, 0.18, 0.20, 0.12, 0.10, 0.06])
        
        # Combine all terms with dynamic weights
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5 + weights[5] * f6 + weights[6] * f7