import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced high-frequency sinusoidal oscillations with adaptive growth
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x) * np.cos(5.0 * x))
        
        # Adaptive polynomial corruption with variable degrees
        f3 = 0.02 * np.sum((x**8 + 0.7 * x**7 + 0.4 * x**6 + 0.2 * x**5 + 0.05 * x**4) * (1 + 0.5 * np.sin(x)))
        
        # Saddle point structure with stronger cross-term interactions
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)) * (1 + 0.3 * np.cos(2.0 * x)))
        
        # Chaotic component with modified nonlinearity
        f5 = 0.08 * np.sum(np.sin(np.exp(0.5 * x)) * np.cos(np.log(np.abs(x) + 1e-6)) * np.tanh(x))
        
        # Cross-term interaction to increase complexity
        f6 = 0.1 * np.sum((x[:-1] ** 2) * np.sin(x[1:]) * np.cos(x[:-1]))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6