import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term with varying coefficients
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = 0.4 * np.sum(np.sin(12 * np.pi * x_norm))
        
        # Add a quartic penalty term to create deeper valleys
        f3 = 0.06 * np.sum(x_norm**4)
        
        # Add an additional cubic term with non-uniform weights
        f4 = 0.1 * np.sum(x_norm**3)
        
        # Add a secondary trigonometric component with different frequency and amplitude
        f5 = 0.2 * np.sum(np.cos(9 * np.pi * x_norm**2))
        
        # Add a cross-term interaction with higher-order polynomial coupling
        f6 = 0.04 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**3 + x_norm[1:]**3))
        
        # Add a fifth-order polynomial term to increase complexity
        f7 = 0.02 * np.sum(x_norm**5)
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result