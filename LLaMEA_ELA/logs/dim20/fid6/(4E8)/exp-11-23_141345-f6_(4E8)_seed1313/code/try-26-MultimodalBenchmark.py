import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Enhanced multimodal terms with multiple local minima and chaotic behavior
        f2 = 0.2 * np.sum(np.sin(9 * np.pi * x_normalized)**6 * np.cos(3 * np.pi * x_normalized)**4)
        
        # Additional high-frequency oscillatory term to increase complexity
        f3 = 0.12 * np.sum(np.sin(15 * np.pi * x_normalized) + np.cos(8 * np.pi * x_normalized) + 
                          np.sin(5 * np.pi * x_normalized**2) * np.cos(2 * np.pi * x_normalized))
        
        # Higher-order polynomial interaction terms with chaotic cross-terms
        f4 = 0.08 * np.sum((x_normalized**5) * np.sin(3 * np.pi * x_normalized) * 
                          np.cos(7 * np.pi * x_normalized) + (x_normalized**3) * np.sin(4 * np.pi * x_normalized))
        
        # Chaotic cross-term interactions
        f5 = 0.06 * np.sum(np.sin(np.pi * x_normalized) * np.cos(np.pi * x_normalized) * 
                          np.sin(2 * np.pi * x_normalized**3) * np.cos(5 * np.pi * x_normalized))
        
        return f1 + f2 + f3 + f4 + f5