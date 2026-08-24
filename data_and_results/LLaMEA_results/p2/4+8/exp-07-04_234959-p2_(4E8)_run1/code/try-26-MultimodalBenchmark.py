import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal term with multiple local minima using different frequencies
        f2 = 0.2 * np.sum(np.sin(9 * np.pi * x_normalized)**8)
        
        # Additional cosine interaction term to create more complex landscape
        f3 = 0.1 * np.sum(np.cos(5 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized))
        
        # Shifted global minimum to increase difficulty
        f4 = 0.05 * np.sum((x_normalized - 0.25)**6)
        
        # Additional radial penalty term to increase landscape complexity
        f5 = 0.1 * np.sum((x_normalized**2 + 0.1 * np.sin(4 * np.pi * x_normalized))**2)
        
        # Cross-term interaction to increase algorithmic challenge
        f6 = 0.08 * np.sum(np.sin(6 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        return f1 + f2 + f3 + f4 + f5 + f6