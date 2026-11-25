import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Enhanced multimodal term with multiple frequencies and amplitudes
        f2 = 0.3 * np.sum(np.cos(15 * np.pi * x_norm) + 0.4 * np.cos(25 * np.pi * x_norm) + 0.2 * np.cos(35 * np.pi * x_norm))
        
        # Higher-order polynomial penalty with adaptive weights
        f3 = 0.03 * np.sum(x_norm**6 + 0.15 * x_norm**7 + 0.05 * x_norm**8)
        
        # Composite multimodal term with radial symmetry and trigonometric coupling
        f4 = 0.2 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * np.exp(-0.3 * np.sum(x_norm**2)))
        
        # Additional coupled oscillatory term with radial dependence
        f5 = 0.1 * np.sum(np.sin(20 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) * (1 + 0.1 * np.sum(x_norm**2)))
        
        # New sinusoidal coupling term between dimensions
        f6 = 0.05 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * np.sin(4 * np.pi * np.sum(x_norm**2)))
        
        # Add a radial penalty term to encourage convergence to global minimum
        radial_penalty = 0.05 * np.sum(x_norm**4) * np.exp(-0.1 * np.sum(x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + radial_penalty