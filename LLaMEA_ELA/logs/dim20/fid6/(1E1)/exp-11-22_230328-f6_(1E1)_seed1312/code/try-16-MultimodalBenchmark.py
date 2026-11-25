import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with exponentially increasing frequencies
        f2 = 0.3 * np.sum(np.sin(2**(np.arange(self.dim)) * np.pi * x_norm) * 
                          np.cos(2**(np.arange(self.dim)+1) * np.pi * x_norm))
        
        # Add a chaotic-like interaction term using logistic map inspired components
        f3 = 0.25 * np.sum(np.sin(10 * np.pi * x_norm) * 
                           np.sin(15 * np.pi * x_norm) * 
                           np.cos(20 * np.pi * x_norm))
        
        # Introduce a quartic term for increased non-convexity
        f4 = 0.03 * np.sum(x_norm**4)
        
        # Add a cross-term interaction with exponentially decaying weights
        f5 = 0.1 * np.sum(np.exp(-np.arange(self.dim-1)) * 
                          x_norm[:-1] * x_norm[1:] * 
                          np.sin(8 * np.pi * x_norm[:-1]))
        
        # Add a high-frequency oscillation component to create many local minima
        f6 = 0.2 * np.sum(np.sin(50 * np.pi * x_norm) * 
                          np.cos(30 * np.pi * x_norm) * 
                          np.sin(40 * np.pi * x_norm))
        
        # Combine all terms with different weights to control difficulty
        return f1 + f2 + f3 + f4 + f5 + f6