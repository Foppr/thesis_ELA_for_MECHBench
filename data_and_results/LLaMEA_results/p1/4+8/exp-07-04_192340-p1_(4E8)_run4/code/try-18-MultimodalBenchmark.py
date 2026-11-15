import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Highly multimodal term with chaotic distribution of local minima
        f2 = 0.5 * np.sum(np.cos(10 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Saddle point enhancement with alternating signs
        f3 = 0.3 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Chaotic penalty term with variable exponent
        f4 = 0.2 * np.sum(np.abs(x_norm)**(1.5 + np.sin(2 * np.pi * x_norm)))
        
        # Cross-term interaction for increased complexity
        f5 = 0.1 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Additional noise-like term for robustness testing
        noise = 0.05 * np.sum(np.sin(13 * x_norm) * np.cos(17 * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + noise