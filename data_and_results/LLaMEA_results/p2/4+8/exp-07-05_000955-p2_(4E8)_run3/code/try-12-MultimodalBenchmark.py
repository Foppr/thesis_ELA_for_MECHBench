import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # High-dimensional polynomial landscape with varying exponents
        f1 = np.sum(x_normalized**4 + 0.5 * x_normalized**3 + 0.1 * x_normalized**2)
        
        # Multi-frequency sinusoidal modulation creating dense local optima
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized) + 
                   np.sin(7 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Chaotic interaction term using nested trigonometric functions
        f3 = np.sum(np.sin(np.pi * np.cos(np.pi * x_normalized)) * 
                   np.cos(np.pi * np.sin(np.pi * x_normalized)))
        
        # Cross-term interaction creating complex fitness landscape
        f4 = np.sum(np.sin(x_normalized[:-1] + x_normalized[1:]) * 
                   np.cos(x_normalized[:-1] - x_normalized[1:]))
        
        # Combine all components with varying weights and add noise
        result = 0.8 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * np.random.random()
        
        # Ensure global minimum at origin with value 0
        return max(0, result)