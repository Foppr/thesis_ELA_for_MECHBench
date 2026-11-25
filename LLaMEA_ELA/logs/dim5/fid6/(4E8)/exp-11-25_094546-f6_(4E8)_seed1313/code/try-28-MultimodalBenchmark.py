import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic polynomial term for smooth landscape
        quad_term = np.sum(x_norm**2)
        
        # High-frequency sine wave terms creating multiple local minima
        sine_term = np.sum(np.sin(10 * np.pi * x_norm))
        
        # Cubic polynomial term to increase complexity and nonlinearity
        cubic_term = np.sum(x_norm**3)
        
        # Additional quartic polynomial term for further landscape complexity
        quartic_term = 0.05 * np.sum(x_norm**4)
        
        # Adaptive weighting to balance different components
        adaptive_weight = 1.0 + 0.5 * np.abs(np.sin(np.sum(x_norm)))
        
        return adaptive_weight * (quad_term + sine_term + cubic_term + quartic_term)