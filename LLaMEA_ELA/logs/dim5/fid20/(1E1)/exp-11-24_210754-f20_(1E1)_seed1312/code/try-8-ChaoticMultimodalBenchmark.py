import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for conditioning
        f1 = np.sum(x**2)
        
        # Nested sinusoidal components with chaotic modulation
        f2 = np.sum(np.sin(10.0 * np.sin(3.0 * x)) * np.cos(7.0 * np.cos(2.0 * x)))
        
        # Polynomial corruption with varying coefficients
        f3 = 0.02 * np.sum(x**8 + 0.5 * x**7 + 0.2 * x**6 + 0.05 * x**5)
        
        # Gradient-induced saddle points via cross-terms
        f4 = 0.1 * np.sum((x[:-1] - x[1:])**2 * np.sin(x[:-1] + x[1:]))
        
        # Chaotic component with exponential scaling
        f5 = 0.08 * np.sum(np.sin(np.exp(0.5 * x)) * np.cos(np.pi * np.abs(x)))
        
        # Add a global distortion term for increased complexity
        f6 = 0.03 * np.sum(np.sin(20.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all terms with varying weights
        return f1 + f2 + f3 + f4 + f5 + f6